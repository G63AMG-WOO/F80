#!/bin/bash

num1=$1
plusminus=$2
num2=$3

if [ "$plusminus" = "+" ]; then
    result=$((num1 + num2))
elif [ "$plusminus" = "-" ]; then
    result=$((num1 - num2))
else
    echo "error"
    exit 1
fi

echo $result
exit 0