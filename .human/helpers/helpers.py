
import click
import sh


def get_default_branch():
    """Get the default branch for the remote repository."""
    try:
        # Get the symbolic-ref of the remote HEAD, e.g., refs/heads/main
        remote_head = sh.git(
            "symbolic-ref", "refs/remotes/origin/HEAD").strip()
        # Extract the branch name from the full ref path
        default_branch = remote_head.split('/')[-1]
        return default_branch
    except sh.ErrorReturnCode as e:
        click.echo(f"Error determining default branch: {e}")
        return None


def detect_stacked_branches(current_branch, target_branch):
    """Detect stacked branches based on commits not merged into target."""
    all_branches = sh.git('branch', '--list',
                          '--no-merged', target_branch).split()
    stacked_branches = [branch.strip() for branch in all_branches]
    return stacked_branches


# TODO: add copy with "stack./.{stacked_branches[0]}./.{target_branch}./.{target_short_hash}./.todo/#index/" prefix to all branches before starting the operation then on success
# change the prefix to "stack./.{stacked_branches[0]}./.{target_branch}./.{target_short_hash}./.ok/#index/" so it can resume later on then overwrite the original branches
def rebase_stack(target_branch, stacked_branches, push):
    """Rebase all stacked branches onto the target branch, preserving their order."""
    try:
        if not stacked_branches:
            click.echo("No stacked branches provided.")
            return

        # TODO: add todo prefixes and copy the original branch

        # Track the last rebased branch to use as the new base for the next branch in the list
        last_rebased_branch = target_branch

        for branch in stacked_branches:
            sh.git.checkout(branch)
            sh.git.rebase('--onto', last_rebased_branch, branch)
            click.echo(f"Rebased {branch} onto {last_rebased_branch}")
            last_rebased_branch = branch

        if push:
            for branch in stacked_branches:
                sh.git.push('origin', branch, force=True)
                click.echo(f"Pushed {branch} to remote.")

    except sh.ErrorReturnCode as e:
        click.echo(f"Error during rebase or push: {e}", err=True)

# TODO: def list_open_stacks -> (name, target_branch, target_short_hash)
# TODO: def orphan_stacks
# TODO: def clean_orphan_stacks