"""mdview_tui is a terminal-based markdown viewer built with Textual."""

import sys

from .app import MarkdownViewerApp


def main() -> None:
    """Entry point for the mdview_tui application."""
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        path = sys.argv[1]
        with open(path) as f:  # noqa: PTH123
            text = f.read()
        title = path
    else:
        if sys.stdin.isatty():
            print("Usage: mdview <file.md>", file=sys.stderr)  # noqa: T201
            print("       cat file.md | mdview", file=sys.stderr)  # noqa: T201
            sys.exit(1)
        text = sys.stdin.read()
        title = "stdin"

    MarkdownViewerApp(text, title=title).run()
