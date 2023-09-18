#!/usr/bin/env python3
import sh
import click
import glob
import json
import os
from dataclasses import dataclass

script_dir = os.path.dirname(os.path.abspath(__file__))
config_file = f"{script_dir}/.config.json"

@dataclass
class Config:
    notebook_workspace: str

@dataclass
class CtxObject:
    config: Config

def save_config(config: Config):
    json.dump(config.__dict__, open(config_file, 'w'), indent=2)

@click.group()
@click.pass_context
def cli(ctx):
    # Setup context object
    obj = CtxObject
    if os.path.exists(config_file):
        obj.config = Config(**json.load(open(config_file)))
    else:
        obj.config = Config(notebook_workspace=os.path.expanduser('~'))
        save_config(obj.config)

    ctx.obj = obj

    # No command, run default
    if ctx.invoked_subcommand is None:
        # TODO: update packages
        pass

out = {'_out': click.get_text_stream('stdout'), '_err': click.get_text_stream('stderr')}

@cli.command(help="Start jupyter notebook docker")
@click.option('--update', '-u', is_flag=True, help="Update docker image")
@click.option('--workspace', '-w', default=None, help="Workspace directory")
@click.option('--start_docker', '-s', is_flag=True, help="Start docker service")
@click.option('--restart_docker', '-r', is_flag=True, help="Restart docker service")
@click.pass_obj
def jupyter(obj: CtxObject, update, workspace, start_docker, restart_docker):
    if workspace is not None:
        obj.config.notebook_workspace = workspace
        save_config(obj.config)

    if start_docker or restart_docker:
        if restart_docker:
            sh.colima.restart(**out)
        else:
            try:
                output = sh.colima.status()
                return 'is running' in str(output)
            except sh.ErrorReturnCode:
                if start_docker:
                    sh.colima.start(**out)

    if update:
        sh.docker.pull('janpfeifer/gonb_jupyterlab:latest', **out)
        return

    workspace = obj.config.notebook_workspace
    # '-it'
    sh.docker.run('--rm', '-p', '8888:8888', '-v', f"{obj.config.notebook_workspace}:/home/jovyan/work", 'janpfeifer/gonb_jupyterlab:latest', **out)

def echo(message):
    click.echo(f'HUMAN: {message}')

if __name__ == '__main__':
    try:
        cli()
    except sh.ErrorReturnCode as e:
        echo(f'Command "{e.full_cmd}" failed with exit code {e.exit_code}')