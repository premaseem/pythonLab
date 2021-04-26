#!/usr/bin/env bash

for i in $(seq 13 50); do
    i="$(echo -e "${i}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
    echo "splitting file for $i"
    cat pwned-aa | grep ":$i" >> pwned-$i-times.txt
done