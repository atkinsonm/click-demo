import os
import sys

FILENAME = "todo.txt"


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


def list_items():
    try:
        with open(FILENAME, "r") as f:
            count = 1
            for line in f:
                print(f"{count}: {line}")
                count += 1
    except FileNotFoundError:
        print("There are no pending todos!".encode("utf8"))


def help():
    sa = """Usage :-
    $ todov1 add "todo item"  # Add a new todo
    $ todov1 list             # Show remaining todos
    $ todov1 done NUMBER      # Complete a todo
    $ todov1 help             # Show usage"""
    sys.stdout.buffer.write(sa.encode("utf8"))


def cli():
    # todov1 add <item string>
    # todov1 done <item index>
    # todov1 list

    valid_commands = ["add", "done", "list"]

    try:
        command = sys.argv[1]
    except IndexError:
        print(f"No command, choose one of {valid_commands}")
        sys.exit(1)

    if command == "add":
        add(sys.argv[2])
    elif command == "done":
        done(sys.argv[2])
    elif command == "list":
        list_items()
    else:
        help()
