from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Markdown


class MarkdownViewerApp(App):
    BINDINGS = [
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
        super().__init__()
        self._text = text
        self._title = title

    def compose(self) -> ComposeResult:
        yield Markdown(self._text)
        yield Footer()

    def on_mount(self) -> None:
        self.title = self._title
