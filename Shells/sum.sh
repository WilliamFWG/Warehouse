#!/bin/bash
SumN=0
while :
	do
		read -p 'please enter a number: ' n
		let SumN=$(($n+$SumN))
		if [[ -z "$n" || "$n" -eq 0 ]]; then
			echo "Total Sum : $SumN"
			exit
		fi
	done
