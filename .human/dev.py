#!/usr/bin/env python3
import click
import sh

import helpers.helpers


@click.command("up", help='Rebases current local branch and all "stacked" branches onto the target or default branch and optionally update them (git push -f).')
@click.option('--target-branch', default=None, help='The branch to rebase other branches onto. Auto-detected if not specified.')
@click.option('--push', is_flag=True, help='Push changes after rebase.')
@click.option('--dry-run', is_flag=True, help='Simulate the actions without making any changes.')
def up(target_branch, push, dry_run):
    current_branch = sh.git('rev-parse', '--abbrev-ref', 'HEAD').strip()

    if not target_branch:
        target_branch = helpers.get_default_branch()

    # TODO: check if operation in progress
    # TODO: check if dirty and return

    stacked_branches = helpers.detect_stacked_branches(
        current_branch, target_branch)

    if dry_run:
        click.echo(f"Would rebase {current_branch} onto {target_branch}")
        for branch in stacked_branches:
            click.echo(
                f"Would also rebase stacked branch {branch} onto {target_branch}")
        if push:
            click.echo("Would push changes to remote")
        return

    helpers.rebase_stack(target_branch, stacked_branches, push)


@click.command()
@click.option('--username', prompt='GitHub username', help='GitHub username whose ghstack branches will be deleted.')
def delete_ghstack_branches(username):
    """
    Deletes all ghstack branches for a specified GitHub username.
    """
    try:
        # Disable Git color output for individual commands
        noc = ['-c', "color.ui=never"]

        # Fetch the latest branch info
        sh.git(*noc, 'fetch', 'origin')

        # Get list of all remote branches
        branches = sh.git(*noc, 'branch', '-r').strip().split('\n')

        # Filter out ghstack branches for the specific user
        ghstack_branches = [
            branch.strip() for branch in branches if f'origin/gh/{username}/' in branch]

        # Delete each ghstack branch
        for branch in ghstack_branches:
            branch_name = branch.replace('origin/', '')
            print(f"Deleting branch: {branch_name}")
            sh.git(*noc, 'push', 'origin', '--delete', branch_name)

        print("Deletion complete.")

    except sh.ErrorReturnCode as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    delete_ghstack_branches()
