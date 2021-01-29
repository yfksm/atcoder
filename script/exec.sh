#!/bin/bash
i=1
while true
do
    FILE=./sample_input/sample$i
    if [ ! -e $FILE ]; then
        break
    fi

    ./main <$FILE> ./sample_output/actual$i
    i=$((++i))
done