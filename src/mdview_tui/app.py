"""MarkdownViewerApp Textual application for viewing markdown content in the terminal."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Markdown


class MarkdownViewerApp(App):
    """A Textual application for viewing markdown content in the terminal."""

    BINDINGS = [  # noqa: RUF012
        Binding("q", "quit", "Quit"),
    ]

    CSS = """
    Markdown {
        layout: stream;
        padding: 0 2;
    }
    """

    theme = "tokyo-night"

    def __init__(self, text: str, title: str = "Markdown") -> None:
        """Initialize the MarkdownViewerApp with the given markdown text and title."""
        super().__init__()
        self._text = text
        self._title = title

    def compose(self) -> ComposeResult:
        """Compose the UI components for the application."""
        yield Markdown(self._text)
        yield Footer()

    def on_mount(self) -> None:
        """Set the application title on mount."""
        self.title = self._title
