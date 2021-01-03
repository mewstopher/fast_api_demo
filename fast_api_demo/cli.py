"""Console script for machine_learning_practice."""
import sys
import click


@click.group()
def main(args=None):
    """console script for machine_learning_practice."""
    return 0


@main.command()
def say_hello():
    print('hello')


if __name__ == "__main__":
    sys.exit(main()) # pragma: no cover
