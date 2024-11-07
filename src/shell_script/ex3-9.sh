#!/bin/bash

target_name=$1

db_file="DB.txt"

if [ -f $db_file ]; then
    result=$(grep -i "$target_name" "$db_file")
    
    if [ -n "$result" ]; then
        echo "$result"
    else
        echo "이름이 존재하지 않습니다.."
    fi
else
    echo "DB.txt 파일이 존재하지 않습니다."
fi
exit 0