#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — Mizzlewick.

Writes a single-line weather forecast for the invented city of
Mizzlewick into /output/entry.txt. The joke is the weather itself:
one stubborn cloud keeps circling the same block, so the rain is
booked in by the hour, in the flat phrasing of an official bulletin.
"""

from pathlib import Path

CITY = "Mizzlewick"
ENTRY = "Mizzlewick: rain at 3pm, 4pm and 5pm, as the same cloud keeps circling the block."

MAX_CHARS = 120
OUT_FILE = Path("/output/entry.txt")


def validate(entry):
    """The gate needs UTF-8 text of 1-120 chars, one line, not blank.

    The judge's first criterion is that the line forecasts weather
    for a city that does not exist, so the invented city's name must
    be in the line — a forecast with no invented city in it loses to
    any forecast that has one.
    """
    if not entry.strip():
        raise SystemExit("entry must not be only whitespace")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(entry)}")
    if "\n" in entry.strip():
        raise SystemExit("entry must be a single line")
    if CITY not in entry:
        raise SystemExit(f"entry must name the invented city {CITY}")
    return entry


def run():
    entry = validate(ENTRY)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(entry, encoding="utf-8")
    print(f"wrote {len(entry)} chars to {OUT_FILE}")


run()
