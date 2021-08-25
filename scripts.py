import subprocess
import sys

ANSI_COLORS = True


def title(s):
    if ANSI_COLORS:
        print(f"\x1b[6;30;42m    {s}    \x1b[0m")
    else:
        print(f"**** {s} ****")
    print()


def cmd(cli):
    subprocess.run(cli, shell=True, check=True, executable="/bin/bash")


def run_pytest(*args):
    title("Testing with pylint")
    TEST_DEFAULTS = ["--doctest-modules", "--ignore=scripts.py"]
    cli_args = TEST_DEFAULTS + list(args) + sys.argv[1:]
    print(f"RUNNING WITH ARGS: {cli_args}")
    cmd(f"pytest {' '.join(cli_args)}")


# For devmode
def devtest(*args):
    run_pytest(
        "-v",
        "-x",  # exit on first failure
        "--new-first",  # test newer files first
        "--color=yes",
        "--code-highlight=yes",
        "--log-level=DEBUG",
        *args,
    )


def typecheck():
    title("Type Checking with mypy")
    cmd("mypy --warn-unreachable -m feedshepherd")


def lint(black_check_only=False):
    if black_check_only:
        title("Checking for black formatting")
        opts = "--check"
    else:
        title("Formatting with black")
        opts = ""
    cmd(f"python -m black {opts} scripts.py feedshepherd")

    title("Linting with pylint")
    cmd("pylint feedshepherd")


def check():
    lint()
    typecheck()
    devtest("--cov")


# For ci mode
def ci():
    global ANSI_COLORS
    ANSI_COLORS = False
    typecheck()
    lint(black_check_only=True)
    run_pytest(
        "--color=no",
        "--cache-clear",  # ditch any test caches lying around
        "--log-level=WARNING",
        "--cov",
    )


def run_main():
    print("NOT IMPLEMENTED")
