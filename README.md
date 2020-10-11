# home-config

## TODO:
- [ ] Run tests in github
- [ ] Deploy home-setup repo

## Manjaro

```bash
# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
alias home='git --work-tree=$HOME --git-dir=$HOME/.home'
# Bring saved configuration files from the repository
home init && home remote add origin git@github.com:stefandunca/home-config.git
home fetch && home checkout master
# Trigger customized configuration on bash interactive startup
echo "[[ -f $HOME/.human/bashrc ]] && . $HOME/.human/bashrc" >> $HOME/.bashrc
# Restart terminal or `source $HOME/.bashrc`
```

Sudo without a password:
 - call `sudo visudo`, go to the end of the file, press `i` to enter edit mode, add: `human ALL=(ALL) NOPASSWD:ALL` and save and exit by typing `:wq!`

Deploy setup remotelly:
 - Command: `ansible-playbook --syntax-check --extra-vars "run_as_user=human" -e 'ansible_python_interpreter=/usr/bin/python3' --inventory mediasrv, --limit "mediasrv" mediasrv.yml`
   - Do not upgrade packages, add: `--skip-tags upgrade`
   


Use Vagrant test file as a reference: https://github.com/stefandunca/home-config/blob/384867c841f55ec8bfc4d76849bd16dcf64f91f3/.human/vagrant/manjaro/Vagrantfile#L60

## Ubuntu
```bash
# Install ansible
sudo apt update
sudo apt install software-properties-common ansible git
# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
alias home='git --work-tree=$HOME --git-dir=$HOME/.home'
# Bring saved configuration files from the repository
home init && home remote add origin git@github.com:stefandunca/home-config.git
home fetch && home checkout master
# Trigger customized configuration on bash interactive startup
echo "[[ -f $HOME/.human/bashrc ]] && . $HOME/.human/bashrc" >> $HOME/.bashrc
# Restart terminal or `source $HOME/.bashrc`
# Install required dependencies
sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory localhost, --limit localhost ~/.human/ansible/ubuntu.local.yml --extra-vars "run_as_user=$USER"
```
