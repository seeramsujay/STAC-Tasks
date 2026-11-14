import requests
import rich


def fetch():
    try:
        return requests.get(
            "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,racist,explicit&type=single"
        ).json()
    except requests.RequestException as e:
        rich.print(f"[red]{e}[/red]")
        return None


def display(json):
    if not json["error"]:
        rich.print(f"[bold magenta]{json['joke']}[/bold magenta]\n")
        rich.print("-" * 80)


ch = "y"
rich.print("[bold green]Welcome to Joker![/bold green]")
while ch in "yY":
    rich.print("[bold blue]Here's a joke for you:[/bold blue]")
    display(fetch())
    rich.print("[bold green]Do you want another joke? (y/n)[/bold green]")
    ch = input()
rich.print("[bold red]Thank you for using Joker![/bold red]")
