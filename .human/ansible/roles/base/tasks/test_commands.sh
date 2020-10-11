#!/bin/bash

ANSIBLE_DISTRIBUTION="$1"

if [[ "$ANSIBLE_DISTRIBUTION" == "Archlinux" ]]; then
  yay --version
fi

[[ $? == 0 ]] && htop --version && python3 --version && pip3 --version
