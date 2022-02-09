import click
import os


FILENAME = "todo.txt"


@click.group()
@click.version_option(package_name="click-demo")
@click.option(
    "--debug", type=click.BOOL, default=False, is_flag=True, help="Enable debug logging"
)
@click.pass_context
def cli(ctx: click.Context, debug: bool):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)

    ctx.obj["DEBUG"] = debug


@cli.command()
@click.argument("item", type=click.STRING)
def add(item, confirm=True):
    """Add an item to the todo list"""
    with open(FILENAME, "a") as f:
        f.write(item)
        f.write("\n")
    if confirm:
        click.echo(f"Added todo: {item}")


@cli.command()
@click.argument("index", type=click.INT)
def done(index):
    """Remove an item from the list"""
    to_do_list = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                to_do_list.append(line.strip())
        os.remove(FILENAME)
        del to_do_list[int(index) - 1]
        for item in to_do_list:
            add(item, confirm=False)
        click.echo(f"Deleted item {index}")
    except FileNotFoundError:
        click.echo("There are no pending todos!".encode("utf8"))


@cli.command
def list():
    """List all open items in the todo list"""
    try:
        with open(FILENAME, "r") as f:
            count = 1
            for line in f:
                print(f"{count}: {line}")
                count += 1
    except FileNotFoundError:
        click.echo("There are no pending todos!".encode("utf8"))
