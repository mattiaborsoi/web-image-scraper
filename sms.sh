#!/bin/bash 
(echo obase=16; seq 1 $((echo ibase=16; echo FF) | bc)) | bc > 1

for i1 in $(cat 1);
do 
    for i2 in $(cat 1);
    do
        for i3 in $(cat 1);
        do
            URL="http://gs.3g.cn/D/"
            URL+=$i1
            URL+=$i2
            URL+=$i3
            URL+="/w"
            python3 scraper.py $URL
        done
    done
done | tr -d " "


