import os
import tempfile
from git import Repo


def setup_repos():
    """Set up work and remote repositories in temporary directories."""
    # Create temporary directories for the remote and work repositories
    remote_dir = tempfile.mkdtemp()
    work_dir = tempfile.mkdtemp()

    # Initialize the remote repository and make an initial commit
    remote_repo = Repo.init(remote_dir, bare=True)

    # Clone the remote repository to create the work repository
    work_repo = Repo.clone_from(remote_dir, work_dir)

    # Create an initial commit in the work repository
    file_path = os.path.join(work_dir, "README.md")
    with open(file_path, 'w') as f:
        f.write("# Test Repository")
    work_repo.index.add([file_path])
    work_repo.index.commit("Initial commit")
    work_repo.git.push("origin", "main")

    return remote_dir, work_dir, remote_repo, work_repo


def create_branches(repo, base_branch, branch_names):
    """Create multiple branches based on a base branch."""
    for branch_name in branch_names:
        new_branch = repo.create_head(branch_name, base_branch)
        new_branch.checkout()
        # Make a dummy commit to differentiate branches
        file_path = os.path.join(repo.working_dir, f"{branch_name}.txt")
        with open(file_path, 'w') as f:
            f.write(f"Commit in {branch_name}")
        repo.index.add([file_path])
        repo.index.commit(f"Commit for {branch_name}")


def test_stacked_branch_operation():
    remote_dir, work_dir, remote_repo, work_repo = setup_repos()

    # Switch to the work repository for operations
    os.chdir(work_dir)

    # Create branches off the main
    create_branches(work_repo, "main", ["feature1", "feature2"])

    # Create stacked branches off feature1
    create_branches(work_repo, "feature1", ["feature1.1", "feature1.2"])

    # Push some branches to remote to simulate a partial upstream state
    work_repo.git.push("origin", "feature1")

    # TODO: call execute_rebase

    # TODO: verify the state of branches after the operation: current branch, the commit history, and the branches present in the remote

    # Cleanup: Remove the temporary directories
    os.rmdir(remote_dir)
    os.rmdir(work_dir)

