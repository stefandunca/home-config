#!/bin/bash

echo "Running base tests"; ./base.sh
[[ $? -eq 0 ]] && echo "Running dev tests" && ./dev.sh

if [ $? -ne 0 ]; then # If: last exit code is non-zero
    echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    echo Tests failed!
    echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fi
