import click
import time

@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,
)
@click.option(
    "-p",
    "--pause",
    default=0,
    help="Amount of time between the greeting prints",
    show_default=True,
)
def hello(name, count, pause):
    for _ in range(count):
        print(f"Hello {name}!")
        time.sleep(pause)

if __name__ == "__main__":
    hello()