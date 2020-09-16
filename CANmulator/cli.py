import click
from canmulator import transmit


@click.command()
@click.option(
    "-c", "--can",
    required=True,
    type=click.STRING,
    help="can interface (Default: can0)",
    default="can0",
)
@click.option(
    "-j", "--json",
    required=True,
    type=click.Path(exists=True),
    help="json file path",
)
def cli(**kwargs):
    """CANmulator is a tool for transmitting CAn frames from `json` file.
    """
    transmit(**kwargs)


def main():
    try:
        cli()
    except Exception as e:
        print(f'Start failed with error: {e}')


if __name__ == "__main__":
    main()
