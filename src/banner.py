from rich.console import Console
from rich.panel import Panel
from src.config import (
    APP_NAME,VERSION,AUTHOR
)
console = Console()


def show_banner():

    logo = """
██╗     ██╗███╗   ██╗██╗  ██╗██████╗
██║     ██║████╗  ██║██║ ██╔╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝ ██║  ██║
██║     ██║██║╚██╗██║██╔═██╗ ██║  ██║
███████╗██║██║ ╚████║██║  ██╗██████╔╝
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝
"""

    info = """
Developer Research CLI

Version: 1.0.0

Author:  RUTA

Search:
• GitHub repositories
• Reddit discussions
• Hacker news info(TBA)
• stack overflow solution(TBA)

Built with Python + Rich
"""

    console.print(
        f"[bold cyan]{logo}[/bold cyan]"
    )

    panel = Panel(
        info,
        title="LINKD CLI",
        border_style="green"
    )

    console.print(panel)

def show_help_screen():

    info = """
[bold cyan]Developer Research CLI[/bold cyan]

LINKD CLI is a developer-focused command-line tool 
that helps users quickly search and explore programming
topics directly from the terminal.

Instead of opening a browser,
developers can type a command and
instantly get relevant results from 
GitHub repositories and Reddit discussions.

[bold green]Usage:[/bold green]

  linkd <topic>

[bold green]Examples:[/bold green]

  linkd docker
  linkd "react hooks"
  linkd python

[bold green]Features:[/bold green]

  ✓ GitHub search
  ✓ Reddit search
  ✓ Hacker news search
  ✓ stack overflow search

  ✓ Beautiful terminal UI

Built with Python + Rich
"""

    panel = Panel(
        info,
        title="LINKD CLI",
        border_style="cyan"
    )

    console.print(panel)