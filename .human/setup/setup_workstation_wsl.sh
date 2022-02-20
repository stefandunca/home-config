
python3 -m venv $HOME/.human/ansible/inventory_setup/.venv
. $HOME/.human/ansible/inventory_setup/.venv/bin/activate
python3 -m pip install -r $HOME/.human/ansible/inventory_setup/requirements.txt

python $HOME/.human/ansible/inventory_setup/main.py --config $HOME/.human/ansible/inventory_setup/configuration/configuration.qml --output_dir $HOME/.human/ansible/group_vars/

sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost --extra-vars "run_as_user=$USER" --extra-vars "@$HOME/.human/ansible/group_vars/workstation-wsl.yml" $HOME/.human/ansible/wsl.yml

$HOME/.human/setup/setup_home.sh

$HOME/.human/setup/install-emscripten-sdk-on-ubuntu.sh