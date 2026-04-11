"""MarkdownViewerApp Textual application for viewing markdown content in the terminal."""

from pathlib import Path  # noqa: TC003

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Markdown


class MarkdownViewerApp(App):
    """A Textual application for viewing markdown content in the terminal."""

    BINDINGS = [  # noqa: RUF012
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
    ]

    CSS = """
    Markdown {
        layout: stream;
        padding: 0 2;
    }
    """

    theme = "tokyo-night"

    def __init__(self, file: Path, title: str = "Markdown") -> None:
        """Initialize the MarkdownViewerApp with the given file path and title."""
        super().__init__()
        self._file = file
        self._title = title

    def compose(self) -> ComposeResult:
        """Compose the UI components for the application."""
        yield Markdown(self._file.read_text())
        yield Footer()

    def on_mount(self) -> None:
        """Set the application title on mount."""
        self.title = self._title

    async def action_refresh(self) -> None:
        """Re-read the markdown file from disk and update the display."""
        text = self._file.read_text()
        await self.query_one(Markdown).update(text)
