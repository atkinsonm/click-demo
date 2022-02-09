import click


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


_list_options = [
    click.option(
        "--list-name",
        "list_name",
        type=click.STRING,
        default="todolista",
        show_default=True,
    )
]
