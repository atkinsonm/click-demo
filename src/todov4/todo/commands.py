import click
import os
from todov4.utils.utils import add_options, _list_options


@click.group()
def todo():
    """Manage todo items"""


@todo.command(short_help="Add todo item to a list")
@add_options(_list_options)
@click.argument("item", type=click.STRING)
@click.pass_context
def add(ctx: click.Context, list_name: str, item: str):
    with open(f"{list_name}.txt", "w") as f:
        f.write("\n")


@todo.command(short_help="Mark a todo item from a list as done")
@add_options(_list_options)
@click.argument("index", type=click.INT)
@click.pass_context
def done(ctx: click.Context, list_name: str, index: int):
    try:
        os.remove(f"{list_name}.txt")
        click.echo(click.style(f"Deleted todo list {list_name}", fg="green"))
    except FileNotFoundError:
        click.echo(click.style(f"No list found named {list_name}", fg="red"))
