import click
from lark.exceptions import LarkError

from .parser import Parser


@click.command()
@click.option(
    "-c",
    "--command",
    "command",
    default=None,
    help="Évalue l'expression donnée et affiche le résultat.",
)
def main(command: str | None):
    """Lance l'interpréteur interactif d'arithmp (ou évalue -c "expr")."""
    parser = Parser()

    if command is not None:
        try:
            click.echo(parser.parse(command))
        except (LarkError, ArithmeticError) as error:
            raise click.ClickException(str(error)) from error
        return

    click.echo("arithmp - interpréteur interactif (Ctrl+D ou 'exit' pour quitter)")

    while True:
        try:
            line = input(">>> ").strip()
        except EOFError:  # Ctrl+D
            click.echo()
            break
        except KeyboardInterrupt:  # Ctrl+C : on abandonne la ligne, on continue
            click.echo()
            continue

        if not line:
            continue
        if line in ("exit", "quit"):
            break

        try:
            click.echo(parser.parse(line))
        except (LarkError, ArithmeticError) as error:
            click.echo(f"Erreur : {error}", err=True)


if __name__ == "__main__":
    main()