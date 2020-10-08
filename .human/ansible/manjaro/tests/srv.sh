#!/bin/bash

echo "Running base tests"; ./base.sh
[[ $? -eq 0 ]] && echo "Running nase server tests" && ./server.sh

if [ $? -ne 0 ]; then # If: last exit code is non-zero
    echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    echo Tests failed!
    echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fi
