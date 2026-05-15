from rich.console import Console
from rich.table import Table 
console = Console()

def create_table(title):
    
    table=Table(title=title)

    table.add_column("#",style="cyan")

    table.add_column("Name",style="green")

    table.add_column("clone URL",style="magenta")

    return table
def print_header(title):
    console.print(f"\n[bold cyan] {title} [/bold cyan]\n")

def print_error(message):
    console.print(f"\n[bold red] {message} [/bold red]\n")

def print_success(message):
    console.print(f"[bold green] {message} [/bold green]")

