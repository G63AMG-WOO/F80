#!/bin/bash

folder_name="$1"

if [ ! -d "$folder_name" ]; then
    mkdir "$folder_name"
fi

cd "$folder_name"

for i in 0 1 2 3 4; do
    mkdir -p "file$i" 
done

for i in 0 1 2 3 4; do
    touch "file$i.txt" 
    ln -s "../file$i.txt" "file$i/file$i.txt"
done

exit 0