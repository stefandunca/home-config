FROM ubuntu:20.04

ENV USER=username
ARG USER=$USER
ARG DEBIAN_FRONTEND=noninteractive

RUN groupadd -r $USER && useradd --no-log-init -d /home/$USER/ -m -r -G sudo -g $USER $USER && echo "$USER:$USER" | chpasswd 

# Install prerequisities for Ansible
RUN apt-get update
RUN apt-get -y install software-properties-common ansible git

# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
RUN echo '#!/bin/bash\ngit --work-tree=$HOME --git-dir=$HOME/.home "$@"' > /usr/bin/home && chmod +x /usr/bin/home

USER $USER

ENV HOME_REPO=git@github.com:stefandunca/home-config.git
ARG HOME_REPO=$HOME_REPO

# DEV: remove
COPY --chown=$USER . /home/$USER/.ssh/

RUN ls -la ~/.ssh

# Bring saved configuration files from the repository
RUN home init && home remote add origin $HOME_REPO && home fetch && home checkout master

# Trigger customized configuration on bash interactive startup
RUN echo "[[ -f $HOME/.human/.env_vars ]] && . $HOME/.human/.env_vars" >> $HOME/.bashrc

USER root

RUN apt-get -y install sudo

USER $USER

# Restart terminal or `source $HOME/.bashrc`
# Install required dependencies
RUN cd $HOME && ansible-playbook -e 'ansible_python_interpreter=/usr/bin/python3' --connection=local --inventory 127.0.0.1, --limit 127.0.0.1 .human/ansible/local.yml --extra-vars "run_as_user=$USER"

