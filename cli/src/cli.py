import click
from . swagger_editor import (
    pull,
    launch,
    template,
    remove

)
from . swagger_codegen import (
    clone,
    build,
    generate,
    interactive,
   
)
@click.group()
def cli():
    pass 

cli.add_command(pull)
cli.add_command(launch)
cli.add_command(template)
cli.add_command(clone)
cli.add_command(build)
cli.add_command(generate)
cli.add_command(interactive)
cli.add_command(remove)
