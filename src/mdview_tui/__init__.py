import sys

from .app import MarkdownViewerApp


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] not in ("-",):
        path = sys.argv[1]
        with open(path) as f:
            text = f.read()
        title = path
    else:
        if sys.stdin.isatty():
            print("Usage: mdview <file.md>", file=sys.stderr)
            print("       cat file.md | mdview", file=sys.stderr)
            sys.exit(1)
        text = sys.stdin.read()
        title = "stdin"

    MarkdownViewerApp(text, title=title).run()
