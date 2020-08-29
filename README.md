# home-config

```bash
# Install ansible
sudo apt update
sudo apt install software-properties-common ansible git
# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
alias home='git --work-tree=$HOME --git-dir=$HOME/.home'
# Bring saved configuration files from the repository
home init && home remote add origin git@github.com:stefandunca/home-config.git
home checkout master
# Trigger customized configuration on bash interactive startup
echo "[[ -f $HOME/.human/.env_vars ]] && . $HOME/.human/.env_vars" >> $HOME/.bashrc
# Restart terminal or `source $HOME/.bashrc`
# Install required dependencies
sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory 127.0.0.1, --limit 127.0.0.1 .human/ansible/local.yml --extra-vars "run_as_user=$USER"
```
