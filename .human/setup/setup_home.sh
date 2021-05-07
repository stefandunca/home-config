#!/bin/bash

# Install ansible
echo "Install required dependencies"
if ! command -v pacman &> /dev/null
then
    sudo pacman -Syu git ansible openssh
else
    sudo apt update
    sudo apt install -y software-properties-common ansible git
fi

# Manual entry: `alias home='git --work-tree=$HOME --git-dir=$HOME/.home'`
# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
home() {
    git --work-tree=$HOME --git-dir=$HOME/.home $*
}
export -f home

if [ ! -d "$HOME/.home" ]; then
    echo "Cloning home-setup"

    # Ensure the main branch is right
    git config --global init.defaultBranch main
    # Bring saved configuration files from the repository
    home init && home remote add origin https://github.com/stefandunca/home-config.git
    home fetch && home checkout main && home submodule update --init --recursive
    # Trigger customized configuration on bash interactive startup
    echo "Add home-setup scripts at bash login"
    if [[ -z "$ZSH_VERSION" ]]; then
        echo "[[ -f $HOME/.human/shellrc ]] && . $HOME/.human/shellrc" >> $HOME/.bashrc && . $HOME/.bashrc
    else
        echo "[[ -f $HOME/.human/shellrc ]] && . $HOME/.human/shellrc" >> $HOME/.zshrc && . $HOME/.zshrc
    fi

else
    home pull --ff-only origin master && home submodule update --init --recursive
fi

echo "Install fzf"
$HOME/tools/fzf/install --key-bindings --completion --update-rc
