import requests
import rich


def fetch(category_name):
    try:
        return requests.get(
            "https://inshorts.deta.dev/news?category={category_name}"
        ).json()
    except requests.RequestException as e:
        rich.print(f"[red]{e}[/red]")
        return None


def display(news):
    for post in news["data"]:
        rich.print(f"[bold blue]{post['title']}[/bold blue]")
        rich.print(f"[blue]{post['content']}\n[/blue]")
        rich.print("-" * 80)


rich.print("[bold green]Welcome to Inshorts News Fetcher![/bold green]")
display(fetch(input("Enter category: ")))
