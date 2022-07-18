#!/bin/bash
mapfile -t miners < miners.txt

for miner in "${miners[@]}"
do
    result=$(ssh $miner 'nvidia-smi | grep -E "[0-9]C"' | grep -v 'Phone' 2>&1)
    echo -e "$miner -->\n$result"
done
