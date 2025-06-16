awk 'BEGIN { FS="," } { arr[$1]++ } END { for( no in arr) { print no , arr[no] } } ' chesapeake-shipping.csv | sort -k2n
