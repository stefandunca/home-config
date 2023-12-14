#!/usr/bin/env python3
import click
import sh

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
        ghstack_branches = [branch.strip() for branch in branches if f'origin/gh/{username}/' in branch]

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
