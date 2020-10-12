# home-config

## TODO:
- [ ] Run tests in github
- [ ] Deploy home-setup repo


## General first steps

Use `./.human/setup/setup_home.sh` test script as reference or instead of manual steps

### Manjaro
```bash
# Install ansible
sudo pacman -Syu git ansible openssh

```

### Ubuntu
```bash
# Install ansible
sudo apt update
sudo apt install software-properties-common ansible git
```

## General home setup

```bash
# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
alias home='git --work-tree=$HOME --git-dir=$HOME/.home'
# Bring saved configuration files from the repository
home init && home remote add origin git@github.com:stefandunca/home-config.git
home fetch && home checkout master && home submodule update --init --recursive
# Trigger customized configuration on bash interactive startup
echo "[[ -f $HOME/.human/bashrc ]] && . $HOME/.human/bashrc" >> $HOME/.bashrc && . $HOME/.human/bashrc
```

### Manjaro
```
# Trigger customized configuration on bash interactive startup
echo "[[ -f $HOME/.human/bashrc ]] && . $HOME/.human/bashrc" >> $HOME/.bashrc
# Restart terminal or `source $HOME/.bashrc`
```

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
  - workstation: `ansible-playbook "run_as_user=$USER" -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory localhost, --limit localhost ~/.human/ansible/workstation.local.yml`
  - mediasrv: `ansible-playbook --extra-vars "run_as_user=human" -e 'ansible_python_interpreter=/usr/bin/python3' --inventory mediasrv, --limit "mediasrv" ~/.human/ansible/mediasrv.yml`

### Ubuntu

- Command: `sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory localhost, --limit localhost ~/.human/ansible/ubuntu.local.yml --extra-vars "run_as_user=$USER"`
