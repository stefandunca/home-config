#!/bin/bash
#

# Disable pager if not needed in Git commands: https://stackoverflow.com/a/14118014
git config --global --replace-all core.pager "less -F -X"
