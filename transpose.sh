#! /bin/env/bash

for i in normal_{1..300}.txt;
do
    awk -f tsk.awk $i >> output_normal.txt
done

