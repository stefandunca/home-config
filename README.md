# home-config

## General first steps

Use [setup_home.sh](./.human/setup/setup_home.sh) test script as reference or instead of manual steps

## Tips

- Sudo without a password
  - use `sudo visudo` to edit the sudoers, add the end of the file: `<username> ALL=(ALL) NOPASSWD:ALL`