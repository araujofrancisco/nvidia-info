#!/bin/bash
script=$(realpath "$0")
scriptpath=$(dirname "$script")

mapfile -t clients < $scriptpath/clients.txt

showtitles="-B 5"
for client in "${clients[@]}"
do
    cmd="nvidia-smi | grep $showtitles -E '[0-9]C' | grep -v 'NVIDIA GeForce' | grep -v 'Phone'"
    result=$(ssh $client $cmd 2>&1)
    showtitles=""
    echo -e "$client -->\n$result"
done
