import click
from todov4.lists import commands as list_commands
from todov4.todo import commands as todo_commands


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


cli.add_command(list_commands.list)
cli.add_command(todo_commands.todo)
