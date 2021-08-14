# home-config

## TODO:
- [ ] Migrate work evnironment setup to python
- [ ] Run tests in github
- [ ] Deploy home-setup repo


## General first steps

Use `./.human/setup/setup_home.sh` test script as reference or instead of manual steps

Sudo without a password:
 - call `sudo visudo`, go to the end of the file, press `i` to enter edit mode, add: `human ALL=(ALL) NOPASSWD:ALL` and save and exit by typing `:wq!`