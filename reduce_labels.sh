#!/bin/env/ bash

j=1
for i in $(<normal_labels.txt)
    do
        echo $j
        cut -f $((i+1)) processedMatrix.Aurora.july2015.txt > normal_${j}.txt
        j=$((j+1))
    done
exit 0
