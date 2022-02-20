#!/bin/bash

# Source: https://techoverflow.net/2021/01/09/how-to-install-emscripten-sdk-on-ubuntu-in-1-minute/

# This script installs emscripten to ~/.emsdk
if [[ -d "~/.emsdk" ]]
then # Update
  echo "Updating emscripten SDK..."
  cd ~/.emsdk && git pull
else # Install
  echo "Installing emscripten SDK..."
  git clone https://github.com/emscripten-core/emsdk.git ~/.emsdk
fi

# Install & activate latest SDK
# See https://emscripten.org/docs/getting_started/downloads.html for more details
cd ~/.emsdk
./emsdk install latest 
./emsdk activate latest    
# Add to .bashrc and .zshrc
if [[ -f "~/.bashrc" ]]; then echo -e "\nsource ~/.emsdk/emsdk_env.sh" >> ~/.bashrc; fi
if [[ -f "~/.zshrc" ]]; then echo -e "\nsource ~/.emsdk/emsdk_env.sh" >> ~/.zshrc; fi

# Next steps:
# - [ ] To conveniently access emsdk tools from the command line,
#   consider adding the following directories to your PATH:
#     /home/stefan/.emsdk
#     /home/stefan/.emsdk/node/14.18.2_64bit/bin
#     /home/stefan/.emsdk/upstream/emscripten
# - [ ] This can be done for the current shell by running:
#     source "/home/stefan/.emsdk/emsdk_env.sh"
# - [ ] Configure emsdk in your shell startup scripts by running:
#     echo 'source "/home/stefan/.emsdk/emsdk_env.sh"' >> $HOME/.zprofile