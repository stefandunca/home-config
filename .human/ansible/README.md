# Old ansible development environment configuration

## Update tools and packages

Examples

- workstation: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost --extra-vars "run_as_user=$USER" --extra-vars "@$HOME/.human/ansible/group_vars/workstation-manjaro.yml" $HOME/.human/ansible/workstation.yml`
- wsl: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost  --extra-vars '{"run_as_user":"$USER","no_ui_present":True}' --extra-vars "@$HOME/.human/ansible/group_vars/wsl-ubuntu.yml" $HOME/.human/ansible/cmd.yml`
- wsl: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost  --extra-vars '{"run_as_user":"$USER","no_ui_present":True}' --extra-vars "@$HOME/.human/ansible/group_vars/srv-arch.yml" $HOME/.human/ansible/srv.yml`

## Running Ansible

Use optional tags (`--skip-tags <tag>` or filter with `--tags <tag>`):

- `upgrade` do not upgrade packages
- `setup` install update repo, stup fzf ...
- Use `--syntax-check` to check syntax
