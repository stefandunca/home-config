
source $HOME/.human/ansible/inventory_setup/.venv/bin/activate

python $HOME/.human/ansible/inventory_setup/main.py --config $HOME/.human/ansible/inventory_setup/configuration/configuration.qml --output_dir $HOME/.human/ansible/group_vars/

sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost --extra-vars "run_as_user=$USER" --extra-vars "@$HOME/.human/ansible/group_vars/workstation-manjaro.yml" $HOME/.human/ansible/workstation.yml

$HOME/.human/setup/setup_home.sh