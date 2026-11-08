import click

from .parser import Parser



@click.command()
@click.option(
    "-c",
    "--command",
    "command",
    default=None,
    help="Expression à évaluer, par exemple : arithmp -c '1 + 2'.",
)
def main(command: str | None):
    if command is None:
        raise click.UsageError("Une expression est requise : utilise -c \"expr\".")

    result = Parser().parse(command)
    click.echo(result)


if __name__ == "__main__":
    main()
