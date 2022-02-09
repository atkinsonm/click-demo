import argparse
import os


FILENAME = "todo.txt"


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [SUBCOMMAND] [OPTIONS]...",
        description="Manage todo list.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} version 0.1"
    )
    # create sub-parser
    sub_parsers = parser.add_subparsers(help="sub-command help")

    # create the parser for the "add" sub-command
    parser_add = sub_parsers.add_parser("add", help="add an item to the todo list")
    parser_add.add_argument(
        "--item", required=True, type=str, help="the name of the item"
    )

    # create the parser for the "done" sub-command
    parser_done = sub_parsers.add_parser("done", help="remove an item from the list")
    parser_done.add_argument(
        "--index", required=True, type=int, help="the index of the item"
    )

    # create the parser for the "list" sub-command
    sub_parsers.add_parser("list", help="list all todo items")

    return parser


def add(item, confirm=True):
    with open(FILENAME, "a") as f:
        f.write(item)
        f.write("\n")
    if confirm:
        print(f"Added todo: {item}")


def done(index):
    to_do_list = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                to_do_list.append(line.strip())
        os.remove(FILENAME)
        del to_do_list[int(index) - 1]
        for item in to_do_list:
            add(item, confirm=False)
        print(f"Deleted item {index}")
    except FileNotFoundError:
        print("There are no pending todos!".encode("utf8"))


def list():
    try:
        with open(FILENAME, "r") as f:
            count = 1
            for line in f:
                print(f"{count}: {line}")
                count += 1
    except FileNotFoundError:
        print("There are no pending todos!".encode("utf8"))


def cli():
    parser = init_argparse()
    args = parser.parse_args()
