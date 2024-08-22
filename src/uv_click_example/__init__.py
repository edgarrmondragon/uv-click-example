import click


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def cli(name):
    click.echo(f'Hello {name}!')
