#!/usr/bin/env bash
i3status | (read line; echo "$line"; read line ; echo "$line" ; read line; echo "$line";  while true
do
  read line
  echo $(python3 /home/eremeykin/.config/i3/myi3status.py "$line")
done)
