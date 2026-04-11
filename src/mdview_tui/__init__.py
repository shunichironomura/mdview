"""mdview_tui is a terminal-based markdown viewer built with Textual."""

from pathlib import Path  # noqa: TC003
from typing import Annotated

import typer
from rich.console import Console

from .app import MarkdownViewerApp

err_console = Console(stderr=True)


def _main(
    file: Annotated[
        Path,
        typer.Argument(help="Path to the markdown file to view."),
    ],
) -> None:
    """View markdown files in the terminal."""
    if not file.exists():
        err_console.print(f"[bold red]Error:[/] File not found: [yellow]{file}[/]")
        raise typer.Exit(code=1)
    if not file.is_file():
        err_console.print(f"[bold red]Error:[/] Not a file: [yellow]{file}[/]")
        raise typer.Exit(code=1)
    MarkdownViewerApp(file, title=str(file)).run()


def main() -> None:
    """Entry point for the mdview_tui application."""
    typer.run(_main)
