import click
import os
from todov4.utils.utils import add_options, _list_options


@click.group()
def list():
    """Manage todo lists"""


@list.command(short_help="Add todo list")
@add_options(_list_options)
@click.pass_context
def add(ctx: click.Context, list_name: str):
    with open(f"{list_name}.txt", "w") as f:
        f.write("\n")


@list.command(short_help="Delete todo list")
@add_options(_list_options)
@click.pass_context
def delete(ctx: click.Context, list_name: str):
    try:
        os.remove(f"{list_name}.txt")
        click.echo(click.style(f"Deleted todo list {list_name}", fg="green"))
    except FileNotFoundError:
        click.echo(click.style(f"No list found named {list_name}", fg="red"))
