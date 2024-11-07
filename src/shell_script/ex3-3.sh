#!/bin/bash

weight=$1
height=$2

bmi=$(( (weight * 100000) / (height * height) ))
if [ $bmi -lt 185 ]; then
  echo "저체중입니다."
elif [ $bmi -ge 185 ] && [ $bmi -lt 230 ]; then
  echo "정상체중입니다."
else
  echo "과체중입니다."
fi
exit 0