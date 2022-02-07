# home-config

## General first steps

Use [setup_home.sh](./.human/setup/setup_home.sh) test script as reference or instead of manual steps

## Tips

- Sudo without a password
  - call `sudo visudo`, go to the end of the file, press `i` to enter edit mode, add: `human ALL=(ALL) NOPASSWD:ALL` and save and exit by typing `:wq!`