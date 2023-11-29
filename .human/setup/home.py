#!/usr/bin/env python3
import os
import sh
import platform

from helpers.helpers import *

# Manual entry: `alias home='git --work-tree=$HOME --git-dir=$HOME/.home'`
home_path = os.path.expanduser('~')
# Force git to use .home instead of .git
home_git = f"--work-tree {home_path} --git-dir . -C {home_path}/.home".split(" ")

if not os.path.exists(f"{home_path}/.home"):
    echo("clone home-setup")

    # Ensure the main branch is used
    sh.git('config', '--global', 'init.defaultBranch', 'main', '-v', **out)

    # Bring saved configuration files from the repository
    sh.git(*home_git, 'init', **out)
    sh.git(*home_git, 'remote add origin git@github.com:stefandunca/home-config.git'.split(' '), **out)
    sh.git(*home_git, 'fetch', **out)
    sh.git(*home_git, 'checkout', 'main', **out)
else:
    echo("update home-setup")
    # ensure code is up to date
    sh.git(*home_git, 'pull', '--ff-only', 'origin', 'main', **out)

echo("install fzf")

fzf_path = f"{home_path}/tools/fzf"
if not os.path.exists(fzf_path):
    os.makedirs(fzf_path)
    sh.git(*(f"clone --depth 1 https://github.com/junegunn/fzf.git {fzf_path}".split(" ")), **out)

sh.git(*(f"--git-dir {fzf_path}/.git pull --ff-only origin master".split(" ")), **out)
sh.Command(f"{fzf_path}/install")(*("--key-bindings --completion --update-rc".split(" ")), **out)

ohmy_path = f"{home_path}/.oh-my-zsh"
if not os.path.exists(ohmy_path):
    download_script_and_run('https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh')

zsh_custom = f"{ohmy_path}/custom"

def update_ohmyzsh_plugin(name, url, scope):
    global zsh_custom
    if os.path.exists(zsh_custom):
        theme_path = f"{zsh_custom}/{scope}/{name}"
        if not os.path.exists(theme_path):
            echo(f'setup {scope} "{name}"')
            sh.git(*(f"clone --depth=1 {url} {theme_path}".split(' ')), **out)
        else:
            echo(f'update {scope} "{name}"')
            sh.git(*(f"--git-dir {theme_path}/.git fetch --all".split(' ')), **out)
            # Setup process alters files, cleanup
            sh.git(*(f"--git-dir {theme_path}/.git --work-tree={theme_path} reset --hard origin/master".split(' ')), **out)

if os.path.exists(ohmy_path):
    # Trigger customized configuration on bash interactive startup
    exec_custom_line = "\n# Source custom shell configuration\n[[ -f ~/.human/shellrc ]] && . ~/.human/shellrc\n"
    check_if_missing = r'.*~/.human/shellrc.*'
    if append_if_missing(f"{home_path}/.bashrc", check_if_missing, exec_custom_line):
        echo("added loading custom shellrc scripts at bash console login")
    if append_if_missing(f"{home_path}/.zshrc", check_if_missing, exec_custom_line):
        echo("added loading custom shellrc scripts at zsh console login")

    update_ohmyzsh_plugin("powerlevel10k", "https://github.com/romkatv/powerlevel10k.git", "themes")

    if replace_line_matching(f"{home_path}/.zshrc", r'^ZSH_THEME=\".*\"\n$', 'ZSH_THEME=\"powerlevel10k/powerlevel10k\"\n'):
        echo("added powerlevel10k as default theme for zsh console")

    update_ohmyzsh_plugin("zsh-autosuggestions", "https://github.com/zsh-users/zsh-autosuggestions.git", "plugins")

    update_ohmyzsh_plugin("zsh-history-substring-search", "https://github.com/zsh-users/zsh-history-substring-search.git", "plugins")

    update_ohmyzsh_plugin("zsh-completions", "https://github.com/zsh-users/zsh-completions.git", "plugins")

    update_ohmyzsh_plugin("zsh-syntax-highlighting", "https://github.com/zsh-users/zsh-syntax-highlighting.git", "plugins")

    exec_custom_line = "\n\n#Custom prompt; For a new setup, run `p10k configure` or edit ~/.p10k.zsh.\n[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh\n"
    check_if_missing = r'.*\.p10k\.zsh.*\.p10k\.zsh.*'
    if append_if_missing(f"{home_path}/.zshrc", check_if_missing, exec_custom_line):
        echo("added loading powerlevel10k prompt at zsh console login")

    if 'Ubuntu' in platform.platform() and append_if_missing(f"{home_path}/.zshrc", ".*path+=.*/home.*/.local/bin.*", "\n\n#PIP commands in ZSH\npath+=('~/.local/bin')"):
        echo("added PIP executable dir to ZSH path")

    # very slow: zsh-syntax-highlighting git-prompt for MSYS2
    # MY_OHMY_ZSH_PLUGINS="git-extras git colored-man-pages python vscode zsh-autosuggestions zsh-history-substring-search zsh-completions"

    MY_OHMY_ZSH_PLUGINS="git-prompt git-extras git archlinux colored-man-pages docker docker-compose dotenv spring python vscode zsh-syntax-highlighting zsh-autosuggestions zsh-history-substring-search zsh-completions"

    if replace_line_matching(f"{home_path}/.zshrc", r'^plugins=(.*)$', f'plugins=({MY_OHMY_ZSH_PLUGINS})\n'):
        echo(f"registered the following plugins {MY_OHMY_ZSH_PLUGINS}")

    echo("Update oh my zsh")
    sh.zsh('-ic', "omz update", **out)
    sh.zsh('-ic', "autoload -U compinit && compinit", **out)

echo("DONE")