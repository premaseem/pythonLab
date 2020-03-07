#!/bin/bash
# script for tesing
clear
echo "............script started............"
sleep 1
result=`python3 /Users/asejain/PycharmProjects/pythonPlayground/concepts/python_return_to_shell/python_file.py "hi"`
if [ "$result" == "Salaam" ]; then
    echo "script return correct response"
fi
echo $result