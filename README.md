# home-config

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

Check Vagrant file: https://github.com/stefandunca/home-config/blob/384867c841f55ec8bfc4d76849bd16dcf64f91f3/.human/vagrant/manjaro/Vagrantfile#L60

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
sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory 127.0.0.1, --limit 127.0.0.1 .human/ansible/local.yml --extra-vars "run_as_user=$USER"
```
