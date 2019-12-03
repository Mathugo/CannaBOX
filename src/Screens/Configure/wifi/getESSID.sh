#!/bin/bash

interface="wlp2s0"
ESSIDfileTMP="essid.tmp"
ESSIDfile="essid_list.tmp"

sudo iwlist $interface scan |grep ESSID > $ESSIDfileTMP
touch $ESSIDfile

while read line; do
line=`cut -c8- <<< $line`
line="${line::-1}"
# 7 characters then cut --> ESSID:"
# then remove --> "
echo $line >> $ESSIDfile
done < $ESSIDfileTMP
rm $ESSIDfileTMP
