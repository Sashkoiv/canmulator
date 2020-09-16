import click
# import yaml
# import os


@click.command()
@click.option(
    "-c", "--can",
    required=True,
    type=click.STRING,
    help="can interface (Default: can0)",
    default="can0",
)
@click.option(
    "-p", "--pcap",
    required=True,
    type=click.STRING,
    help="pcap file address",
)
@click.option(
    "-s", "--speed",
    required=False,
    default=500000,
    type=click.INT,
    help="CAn speed in kbps",
)
def cli(**kwargs):
    """CANmulator is a tool for transmitting CAn frames from `pcap` file.
    """
    print(locals())


def main():
    try:
        cli()
    except e:
        print(f'Start failed with error: {e}')


if __name__ == "__main__":
    main()
