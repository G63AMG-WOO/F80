#!/bin/bash

info=$@
file_name="DB.txt"
if [ ! -f "$file_name" ]; then
    touch "$file_name"
fi

echo "$info" >> $file_name
exit 0