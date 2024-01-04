#!/bin/bash


line_number=0
declare -A user
w | while IFS= read -r line;
do
  line_number=$[line_number+1]
  if [ $line_number -lt 3 ]
  then
    continue
  fi
  IFS=' ' read -ra temp <<< "$line"
  echo ${temp[0]}
  user["root"]="root"
  #echo "User: "$line
done
echo ${!user[*]}
