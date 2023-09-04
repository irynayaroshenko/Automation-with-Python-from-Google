#!/usr/bin/env bash
# in video #!/bin/bash

echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finish at: $(date)"

# added because terminal closes immediately after execution finished
sleep 5

# executed on Windows: PS C:\pythonProject\Automation with Python\part_2> .\gether_information.sh
# BUT
# $ ./gether_information.sh
  #Starting at: Sun Jul  2 19:02:39 FLEDT 2023
  #
  #UPTIME
  #./gether_information.sh: line 8: uptime: command not found
  #
  #FREE
  #./gether_information.sh: line 12: free: command not found
  #
  #WHO
  #
  #Finish at: Sun Jul  2 19:02:39 FLEDT 2023

# Iteration 2 (open gether_information_iteration_2_result.png)
line="---------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finish at: $(date)"