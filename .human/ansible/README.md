# Old ansible development environment configuration

## Run Ansible

Use Vagrant test files as reference: [Vagrant Test](https://github.com/stefandunca/home-config/tree/master/.human/vagrant)

Use optional tags (`--skip-tags <tag>` or filter with `--tags <tag>`):
  - `upgrade` do not upgrade packages
  - `setup` install update repo, stup fzf ...
Use `--syntax-check` to check syntax


### Manjaro (mediasrv)
- Command:
  - workstation: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost --extra-vars "run_as_user=$USER" $HOME/.human/ansible/workstation.local.yml`
  - wsl: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost  --extra-vars '{"run_as_user":"$USER","no_ui_present":True}' $HOME/.human/ansible/workstation.local.yml`
  - mediasrv: `ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit mediasrv $HOME/.human/ansible/mediasrv.yml`

### Ubuntu

- Command: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory $HOME/.human/ansible/hosts.yml --limit localhost  --extra-vars "run_as_user=$USER" ~/.human/ansible/ubuntu.local.yml`
