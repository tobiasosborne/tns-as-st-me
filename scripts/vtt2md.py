#!/usr/bin/env python3
"""Convert a YouTube (auto-)caption .vtt file to a clean timestamped
markdown transcript.

YouTube auto-caption VTT files carry rolling duplicates (each cue repeats
the previous cue's trailing line) and inline word-timing tags
(<00:00:00.000><c>word</c>). This strips tags, dedupes the rolling
window, and emits paragraphs with a [hh:mm:ss] marker roughly every
PARA_SECONDS of speech.

Usage: vtt2md.py input.vtt > transcript-body.md
"""
import re
import sys

PARA_SECONDS = 60

TAG_RE = re.compile(r"<[^>]+>")
TS_RE = re.compile(r"(\d+):(\d+):(\d+)\.(\d+)\s+-->")


def parse_cues(path):
    """Yield (start_seconds, [lines]) per cue."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    i = 0
    while i < len(lines):
        m = TS_RE.match(lines[i])
        if not m:
            i += 1
            continue
        start = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
        i += 1
        text = []
        while i < len(lines) and lines[i].strip():
            t = TAG_RE.sub("", lines[i]).strip()
            if t and t not in ("&nbsp;",):
                text.append(t)
            i += 1
        if text:
            yield start, text


def dedupe(cues):
    """Drop lines already emitted by the previous cue (rolling window)."""
    prev = []
    for start, text in cues:
        fresh = [ln for ln in text if ln not in prev]
        prev = text
        if fresh:
            yield start, " ".join(fresh)


def fmt(sec):
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def main(path):
    out, para, para_start = [], [], None
    for start, text in dedupe(parse_cues(path)):
        if para_start is None:
            para_start = start
        para.append(text)
        if start - para_start >= PARA_SECONDS:
            out.append(f"**[{fmt(para_start)}]** " + " ".join(para))
            para, para_start = [], None
    if para:
        out.append(f"**[{fmt(para_start)}]** " + " ".join(para))
    print("\n\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
