import argparse
from linkd.github_api import search_github
from rich.status import Status
from linkd.utils import console
from linkd.banner import show_banner,show_help_screen
from linkd.reddit_api import search_reddit
from linkd.stack_overflow_api import get_stackOverFlowData
from linkd.utils import (
    create_table,
    print_error,
    print_success,
    print_header
)

def process_topic(topic):
    with console.status(
            "[bold green] cooking..."
        ):
            # Github repositories
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

            # Reddit Posts
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

            # #Stack overflow answers
            # answers= get_stackOverFlowData(topic)
            # stackOverflow_table=create_table("Stack overflow answers")
            # stackOverflow_table.add_column("#",width=4)
            # stackOverflow_table.add_column("Title",overflow="fold"),
            # stackOverflow_table.add_column("Votes"),
            # stackOverflow_table.add_column("Answers"),
            # stackOverflow_table.add_column("Link",overflow="fold")

            # if not answers:
            #     print_error("No Stack-over-flow answers received")
            # for index,answer in enumerate(answers,start=1):
            #     stackOverflow_table.add_row(
            #         str(index),
            #         str(answer.get('title','N/A')),
            #         str(answer.get('score',0)),
            #         str(answer.get('answer_count',0)),
            #         str(answer.get('link'),'N/A')
            #     )   
            #     console.print(stackOverflow_table) 


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
