#!/bin/bash
mapfile -t clients < clients.txt

for client in "${clients[@]}"
do
    result=$(ssh $client 'nvidia-smi | grep -E "[0-9]C"' | grep -v 'Phone' 2>&1)
    echo -e "$client -->\n$result"
done
