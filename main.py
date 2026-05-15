import argparse
from src.github_api import search_github
from rich.status import Status
from src.utils import console
from src.banner import show_banner,show_help_screen
from src.reddit_api import search_reddit
from src.utils import (
    create_table,
    print_error,
    print_success,
    print_header
)

def process_topic(topic):
    with console.status(
            "[bold green] cooking..."
        ):
            repos=search_github(topic)
            if not repos:
                print_error("No repositories found")
                return

            github_table=create_table(
                "Github Repositories"
            )
            for index, repo in enumerate(repos,start=1):  
                github_table.add_row(
                    str(index),
                    repo['full_name'],
                    repo['clone_url']
                )
            console.print(github_table)
            posts = search_reddit(topic)
            reddit_table=create_table("Reddit posts")
            if not posts:
                print_error("No Reddit posts found")
            for index, post in enumerate(posts,start=1):
                post_data=post["data"]
                reddit_table.add_row(
                    str(index),
                    post_data['title'],
                    f"https://reddit.com{post_data['permalink']}"
                )
            console.print(reddit_table)
def interactive_mode():
    while True:
        try:
            topic=console.input(
                "\n[bold cyan] linkd> [/]"
                ).strip()
            #EXIT COMMAND
            if topic.lower() in [
                "quit",
                "exit"
            ]:
                console.print("\n[bold red] goodbye![/]")
                break 
            if not topic:
                continue
            process_topic(topic)   
        except (KeyboardInterrupt,EOFError):
            console.print("\n[bold red] keyboard interupted, try again")
            interactive_mode()    
def main():
    show_help_screen()
    # show_banner()
    parser=argparse.ArgumentParser(
        description= " Linkd Developer research cli tool"
    )

    parser.add_argument("topic",
    nargs="?",
    help="Search topic"
    )
    args=parser.parse_args()
    topic=args.topic
    if topic:
        process_topic(topic)
    interactive_mode()    
        


if __name__=="__main__":
    main()    
