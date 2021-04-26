#!/usr/bin/env bash

for file in $(echo pwned-50-times.txt); do
    echo $file
    cat $file | wc -l
done