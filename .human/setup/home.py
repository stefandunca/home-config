#!/usr/bin/env python3
import sh
import click

# Manual entry: `alias home='git --work-tree=$HOME --git-dir=$HOME/.home'`
# Create an alias command for git commands with set work dir to home and ".git" dir as ".home"
git_params={'--work-tree':'$HOME', '--git-dir':'.', '-C': "$HOME/.home"}

#if [ ! -d "$HOME/.home" ]; then
#    printf "\n... cloning home-setup\n\n"

    # Ensure the main branch is used
#    git config --global init.defaultBranch main

    # Bring saved configuration files from the repository
#    home init && home remote add origin git@github.com:stefandunca/home-config.git
#    home fetch && home checkout main && home submodule update --init --recursive
#else
#    # ensure code is up to date
#    home pull --ff-only origin main && home submodule update --init --recursive
#fi

#printf "\n... install fzf\n\n"
#git --git-dir $HOME/tools/fzf/.git pull --ff-only origin master && $HOME/tools/fzf/install --key-bindings --completion --update-rc

# TODO: ensure zsh is the default shell if not install it

#if [ ! -d ~/.oh-my-zsh ]; then
    #sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

    # Trigger customized configuration on bash interactive startup
    # printf "\n... add home-setup scripts at bash login\n\n"
    # if [[ -z "$ZSH_VERSION" ]]; then
    #     echo "[[ -f $HOME/.human/shellrc ]] && . $HOME/.human/shellrc" >> $HOME/.bashrc && . $HOME/.bashrc
    # else
    #     echo "[[ -f $HOME/.human/shellrc ]] && . $HOME/.human/shellrc" >> $HOME/.zshrc && . $HOME/.zshrc
    # fi

# if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/}" ]; then
#     printf "\n... setup powerlevel10k\n\n"
#     if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
#         git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
#     else
#         # Setup process alters files
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/themes/powerlevel10k/.git fetch --all
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/themes/powerlevel10k/.git reset --hard origin/master
#     fi

#     if [[ ${OSNAME} == 'MACOS' ]]; then
#         sed -i "" 's?^ZSH_THEME=\".*\"$?ZSH_THEME=\"powerlevel10k/powerlevel10k\"?' $HOME/.zshrc
#     else
#         sed -i 's?^ZSH_THEME=\".*\"$?ZSH_THEME=\"powerlevel10k/powerlevel10k\"?' $HOME/.zshrc
#     fi

#     printf "\n... setup zsh-autosuggestions\n\n"
#     if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions" ]; then
#         git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
#     else
#         # Setup process alters files
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions/.git fetch --all
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions/.git reset --hard origin/master
#     fi

#     printf "\n... setup zsh-history-substring-search\n\n"
#     if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search" ]; then
#         git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
#     else
#         git --git-dir ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search/.git pull
#     fi

#     printf "\n... setup zsh-completions\n\n"
#     if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-completions" ]; then
#         git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-completions
#     else
#         # Setup process alters files
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-completions/.git fetch --all
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-completions/.git reset --hard origin/master
#     fi

#     printf "\n... setup zsh-syntax-highlighting\n\n"
#     if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting" ]; then
#         git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
#     else
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting/.git fetch --all
#         git --git-dir ${ZSH_CUSTOM:=$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting/.git reset --hard origin/master
#     fi

#     #
#     # Update .zshrc if necessary 
#     #
#     grep -q '^.*.p10k.zsh.*.p10k.zsh$' $HOME/.zshrc || printf "\n\n#Custom prompt; For a new setup, run `p10k configure` or edit ~/.p10k.zsh.\n[[ ! -f $HOME/.p10k.zsh ]] || source \$HOME/.p10k.zsh" >> $HOME/.zshrc

#     grep -q '^.*.human/shellrc.*.human/shellrc$' $HOME/.zshrc || printf "\n\n#User stuff\n[[ -f $HOME/.human/shellrc ]] && . $HOME/.human/shellrc" >> $HOME/.zshrc

#     if [[ ${OSNAME} == '"Ubuntu"' || ${OSNAME} == 'Pop!_OS' ]]; then
#         printf "\n... add PIP executable dir to ZSH path\n\n"
#         grep -q '^.*path+=.*/home.*/.local/bin.*$' $HOME/.zshrc || printf "\n\n#PIP commands in ZSH\npath+=('$HOME/.local/bin')" >> $HOME/.zshrc
#     fi

#     # Custom plugins list to replace the default one
#     if [[ ${OSNAME} == 'MSYS2' ]]; then
#         # very slow: zsh-syntax-highlighting git-prompt
#         MY_OHMY_ZSH_PLUGINS="git-extras git colored-man-pages python vscode zsh-autosuggestions zsh-history-substring-search zsh-completions"
#     else
#         zsh -ic "eval $(thefuck --alias)"

#         MY_OHMY_ZSH_PLUGINS="git-prompt git-extras git archlinux colored-man-pages docker docker-compose dotenv spring thefuck python vscode zsh-syntax-highlighting zsh-autosuggestions zsh-history-substring-search zsh-completions"
#     fi

#     if [[ ${OSNAME} == 'MACOS' ]]; then
#         sed -i "" "s?^plugins=(.*)\$?plugins=(${MY_OHMY_ZSH_PLUGINS})?" $HOME/.zshrc
#     else
#         sed -i "s?^plugins=(.*)\$?plugins=(${MY_OHMY_ZSH_PLUGINS})?" $HOME/.zshrc
#     fi

#     # Update oh my zsh
#     zsh -ic "omz update"
#     zsh -ic "autoload -U compinit && compinit"
# fi
