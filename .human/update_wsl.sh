rsync -vr --perms --chmod=u+rwX,go-rwx --chown=$USER:$USER --delete /home/$USER/.ssh/ /mnt/c/Users/$USER/.ssh
rsync -vr --perms --chmod=u+rwX,go-rwx --chown=$USER:$USER --delete /home/$USER/.keys/ /mnt/c/Users/$USER/.keys
