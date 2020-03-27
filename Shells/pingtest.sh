#!/bin/bash
let n=0;let m=0
read -p 'please enter IP address: ' u
if [ -z $u ]; then 
	echo 'IP address needed'
	exit 1
else 
	for i in {1..10} 
		do
			ping -c 3 -i 0.2 -W 1 "$u.$i" &> /dev/null
			if [ $? -eq 0 ]; then
				echo "Ping $u.$i Success"
				let n++
			else 
				echo "Ping $u.$i Failed"
				let m++
			fi
		done
		echo "Success: $n"
		echo "Failed: $m"
fi
