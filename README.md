# home-config

## General first steps

```sh
# Install minimal dependencies
sudo apt install git python3-pip zsh curl
# Or on macOS
sudo brew install git curl uv

# set zsh as the default shell if not already
chsh -s /bin/zsh

# Add github.com-home-config an alias with read-only access key to ~/.ssh/config
#
#Host github.com-home-config
#  HostName github.com
#  User git
#  IdentityFile ~/.keys/home-config-ro

# fetch home-config sources and setup custom git
alias home='git --work-tree=$HOME --git-dir=$HOME/.home' && home init && home remote add origin git@github.com-home-config:stefandunca/home-config.git && home fetch && home checkout main && home submodule update --init --recursive && (uv venv ~/.human/.venv && source ~/.human/.venv/bin/activate && uv pip install -r ~/.human/setup/requirements.txt && python3 ~/.human/setup/home.py && python3 ~/.human/setup/tools.py)
```

## Tips

- Sudo without a password
  - use `sudo visudo` to edit the sudoers, add the end of the file: `<username> ALL=(ALL) NOPASSWD:ALL`

## TODO

- [ ] drop local ansible setup, use scripts. Should make it more user friendly and for better documentation
