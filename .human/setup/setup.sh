#!/bin/bash

# Eg 
# Manjaro: .human/setup/setup.sh $HOME/.human/ansible/group_vars/workstation-manjaro.yml $HOME/.human/ansible/workstation.yml
# Manjaro mobile rig: .human/setup/setup.sh $HOME/.human/ansible/group_vars/mobilerig-manjaro.yml $HOME/.human/ansible/workstation.yml
# WSL: .human/setup/setup.sh $HOME/.human/ansible/group_vars/workstation-wsl.yml $HOME/.human/ansible/wsl.yml

if [ "$#" -ne 2 ]; then
    echo "Missing Variables yml and playbook file in this order"
    exit -1
fi

export EXTRAVARS=$1
export ANSIBLEPLAYBOOK=$2

export OSNAME=$(awk -F= '/^NAME/{gsub(/"/, "", $2); print $2}' /etc/os-release)

# exit when any command fails
set -e

if [[ ${OSNAME} == '"Ubuntu"' || ${OSNAME} == 'Pop!_OS' ]]; then
    sudo apt install python3.9-venv
fi

python3 -m venv $HOME/.human/ansible/inventory_setup/.venv
. $HOME/.human/ansible/inventory_setup/.venv/bin/activate
python3 -m pip install -r $HOME/.human/ansible/inventory_setup/requirements.txt

python $HOME/.human/ansible/inventory_setup/main.py --config $HOME/.human/ansible/inventory_setup/configuration/configuration.qml --output_dir $HOME/.human/ansible/group_vars/

# Alternative parameters
#
# --inventory "<target_ip>,"
# --extra-vars "ansible_user=$USER" # to force connecting with a specific user
# --ask-pass
#
sudo ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --inventory $HOME/.human/ansible/hosts.yml --limit localhost --extra-vars "target=localhost" --extra-vars "run_as_user=$USER" --extra-vars "@${EXTRAVARS}" "${ANSIBLEPLAYBOOK}"

$HOME/.human/setup/setup_home.sh

export OSNAME=$(awk -F= '/^NAME/{gsub(/"/, "", $2); print $2}' /etc/os-release)
if [[ ${OSNAME} == '"Ubuntu"' ]]; then
    printf "\n... setup emsdk on Ubuntu\n\n"

    $HOME/.human/setup/install-emscripten-sdk-on-ubuntu.sh
fi

$HOME/.human/setup/general_settings.sh
