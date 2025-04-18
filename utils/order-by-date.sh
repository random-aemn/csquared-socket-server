#!/bin/bash
#
#  Extract the ISO-8601 formatted date from the second field,
#  convert it to a *nix epoch date and write all the data
#  to an output file.  The epoch date field will be the last field 
#  in the file.
#
#  =================================================================
#  NOTE; This file should be executed in the same directory as the 
#  data files OR modify the script to change file paths.
#  =================================================================
#
#  Once complete, the new file can be sorted as follows:
#  cat r.tmp | sort -n -t "," -k 7 > rsorted.tmp
#
#  After sorting, remove the last column and overwrite the original file
#  as follows:
#
#   awk 'BEGIN{FS=OFS=","} {NF--}1' rsorted.tmp > rachel-thin.csv
#

while read data; do
#data has a CRLF -> use sed (stream editor) to remove
  data=$(echo "$data" | sed 's/\r//g')
  epoch_date=$(echo $data | awk -F '[,]' '{print $2}')
  epoch_date=$(date -d $epoch_date +%s)
  epoch_date=$(echo "$epoch_date" | sed 's/\r//g')
echo "${data},${epoch_date}" >> r.tmp
done <rachel-thin.csv
