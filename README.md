# home-config

## TODO:
- [ ] Run tests in github
- [ ] Deploy home-setup repo


## General first steps

Use `./.human/setup/setup_home.sh` test script as reference or instead of manual steps

Sudo without a password:
 - call `sudo visudo`, go to the end of the file, press `i` to enter edit mode, add: `human ALL=(ALL) NOPASSWD:ALL` and save and exit by typing `:wq!`


## Run Ansible

Use Vagrant test files as reference: https://github.com/stefandunca/home-config/tree/master/.human/vagrant

Use optional tags (`--skip-tags <tag>` or filter with `--tags <tag>`):
  - `upgrade` do not upgrade packages
  - `setup` install update repo, stup fzf ...
Use `--syntax-check` to check syntax


### Manjaro (mediasrv)
- Command:
  - workstation: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost --extra-vars "run_as_user=$USER" $HOME/.human/ansible/workstation.local.yml`
  - mediasrv: `ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit mediasrv $HOME/.human/ansible/mediasrv.yml`

### Ubuntu

- Command: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory $HOME/.human/ansible/hosts.yml --limit localhost  --extra-vars "run_as_user=$USER" ~/.human/ansible/ubuntu.local.yml`
