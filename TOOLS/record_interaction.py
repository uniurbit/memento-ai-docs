#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Università degli Studi di Urbino Carlo Bo
# SPDX-License-Identifier: CC-BY-4.0
"""Deterministic capture of the interactions with the model.

Appends to `REGISTERS/CONVERSATION.md` the verbatim text of the request and of
the final answer of each turn. It implements the "capture from the environment"
mode prescribed in `REGISTERS/INSTRUCTIONS.md`, §4.1.

REQUIREMENTS
    Python 3.8 or later, standard library only. Nothing to install.

INVOCATION
    The command-line tool must run this script at two moments of its own life
    cycle:

        request  — after the user has sent the request
        answer   — when the model's answer is complete

    The script accepts the event data in three forms, in this order:

        1. a JSON object on standard input          (the most common form)
        2. environment variables INTERACTION_*      (see below)
        3. command-line arguments                   record_interaction.py <event> <text>

    The type of event can always be forced as the first argument, which helps
    when the tool does not declare it in the data:

        record_interaction.py request
        record_interaction.py answer

ADAPTING IT TO A DIFFERENT TOOL
    Only the ADAPTER section below is to be modified: the field names by which
    the tool in use denotes event, text, turn identifier and working folder.
    Everything else is independent of the product.

OPERATING CONSTRAINTS
    - The script writes nothing to standard output. Some tools inject hook
      output into the model's context: any service message would end up in the
      conversation.
    - The script never fails visibly: on error it exits with code 0 without
      interrupting the session. An incomplete archive is a problem; a session
      interrupted by the archiving tool is a worse one.
    - Writing is protected by an exclusive lock and marked per turn: a
      re-execution produces no duplicates and concurrent sessions do not
      overwrite one another.

LANGUAGE OF THE RECORDS
    The markers and labels of each record are in English in every language
    version of the kit, because the script is one and the same: they are
    machine-readable scaffolding, not prose. The text recorded stays verbatim
    in the language in which it was written.
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import fcntl
except ImportError:  # platforms without fcntl: proceed without the lock
    fcntl = None

# ─── ADAPTER ─────────────────────────────────────────────────────────────────
# The only section to modify in order to adopt a different tool.
# For each entry the possible field names are listed in order of preference:
# the first one present in the event data is used.

FIELDS = {
    "event":   ("hook_event_name", "event", "event_name", "type"),
    "request": ("user_input", "prompt", "user_message", "input"),
    "answer":  ("last_assistant_message", "assistant_message", "response", "output"),
    "turn":    ("prompt_id", "turn_id", "message_id", "request_id"),
    "session": ("session_id", "conversation_id", "thread_id"),
    "folder":  ("cwd", "workspace", "project_dir"),
}

# The names by which the tool denotes the two events.
EVENTS = {
    "request": ("UserPromptSubmit", "user_prompt_submit", "on_user_message", "pre_request"),
    "answer":  ("Stop", "assistant_response_complete", "on_assistant_message", "post_response"),
}

# Path of the archive, relative to the project root. It is the same in every
# language of the kit: each language is a folder that mirrors the root with the
# same file names, and one of them is promoted to the root when the project is
# set up (README, Technical appendix 5).
ARCHIVE = Path("REGISTERS") / "CONVERSATION.md"
HEADING = "# Conversation\n"
# ─── END OF ADAPTER ──────────────────────────────────────────────────────────


def first_present(data: dict, names) -> str | None:
    """Return the first field among those given that is present and not empty."""
    for name in names:
        value = data.get(name)
        if isinstance(value, str) and value != "":
            return value
    return None


def read_event() -> dict:
    """Acquire the event data from stdin, from the environment or from the arguments."""
    data: dict = {}

    if not sys.stdin.isatty():
        raw = sys.stdin.read()
        if raw.strip():
            try:
                loaded = json.loads(raw)
                if isinstance(loaded, dict):
                    data = loaded
            except json.JSONDecodeError:
                pass

    # Environment variables: INTERACTION_EVENT, INTERACTION_TEXT, ...
    for key, variable in (
        ("event", "INTERACTION_EVENT"),
        ("text", "INTERACTION_TEXT"),
        ("turn", "INTERACTION_TURN"),
        ("session", "INTERACTION_SESSION"),
    ):
        value = os.environ.get(variable)
        if value and key not in data:
            data[key] = value

    # Arguments: <event> [text]
    if len(sys.argv) > 1:
        data["forced_event"] = sys.argv[1].strip().lower()
    if len(sys.argv) > 2:
        data.setdefault("text", sys.argv[2])

    return data


def classify(data: dict) -> str | None:
    """Determine whether the event is a request or an answer."""
    forced = data.get("forced_event")
    if forced in ("request", "answer"):
        return forced

    declared = first_present(data, FIELDS["event"]) or data.get("event") or ""
    if declared.strip().lower() in ("request", "answer"):
        return declared.strip().lower()

    for kind, names in EVENTS.items():
        if declared in names:
            return kind

    # Last criterion: the presence of one of the two text fields.
    if first_present(data, FIELDS["request"]):
        return "request"
    if first_present(data, FIELDS["answer"]):
        return "answer"
    return None


def extract_text(data: dict, kind: str) -> str | None:
    return first_present(data, FIELDS[kind]) or data.get("text")


def project_root(data: dict) -> Path:
    """Root of the repository, inferred from Git or from the script's location."""
    folder = first_present(data, FIELDS["folder"]) or os.getcwd()
    try:
        result = subprocess.run(
            ["git", "-C", folder, "rev-parse", "--show-toplevel"],
            check=True, capture_output=True, text=True, timeout=5,
        )
        return Path(result.stdout.strip()).resolve()
    except (subprocess.SubprocessError, OSError):
        return Path(__file__).resolve().parent.parent


def append_once(destination: Path, marker: str, block: str) -> None:
    """Write at the end, once only per marker, under an exclusive lock."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("a+", encoding="utf-8") as stream:
        if fcntl is not None:
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        stream.seek(0)
        existing = stream.read()
        if marker in existing:      # turn already recorded: no duplicate
            return
        if not existing.strip():
            stream.seek(0, 2)
            stream.write(HEADING)
        stream.seek(0, 2)
        stream.write(block)
        stream.flush()


def main() -> int:
    data = read_event()

    kind = classify(data)
    if kind is None:
        return 0

    text = extract_text(data, kind)
    if not isinstance(text, str) or text == "":
        return 0

    turn = first_present(data, FIELDS["turn"]) or data.get("turn")
    if not turn:
        # No identifier from the tool: one is derived from the text. It is
        # stable by content, so a re-execution does not duplicate and two
        # distinct turns do not collide on the same marker.
        turn = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    session = first_present(data, FIELDS["session"]) or data.get("session") or "unknown-session"
    moment = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

    marker = f"<!-- interaction:{session}:{turn}:{kind} -->"
    label = "Request" if kind == "request" else "Answer"
    block = (
        f"\n{marker}\n"
        f"## {label} — {moment} — capture: environment\n\n"
        f"{text}\n"
    )

    append_once(project_root(data) / ARCHIVE, marker, block)
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception:       # no error must interrupt the session
        code = 0
    raise SystemExit(code)
