#!/bin/bash
POSITIONAL_ARGS=()

script=$(realpath "$0")
scriptpath=$(dirname "$script")

mapfile -t clients < $scriptpath/clients.txt

showtitles=""

while [[ $# -gt 0 ]]; do
    case $1 in
      -h|--header)
        showtitles="-B 5"
        HEADERS=YES
        shift # past argument
        shift # past valu
        ;;
      --defailt)
        DEFAULT=YES
        shift # past argument
        ;;
      -*|--*)
        echo "Unknown option $1"
        exit 1
        ;;
      *)
        POSITIONAL_ARGS+=("$1") # save positional arg
        shift # past argument
        ;;
    esac
done

set -- "${POSITIONAL_ARGS[@]}" # restore positional parameters

for client in "${clients[@]}"
do
    cmd="nvidia-smi | grep $showtitles -E '[0-9]C' | grep -v 'NVIDIA GeForce' | grep -v 'Phone'"
    result=$(ssh $client $cmd 2>&1)
    showtitles=""

    if [ "$HEADERS" = "YES" ];
    then
        echo -e "$client -->\n$result"
    else
        res="$client $result"
        { echo $res; } | sed "s/| |/\n$client/g" | sed "s/|//g"
    fi
done
