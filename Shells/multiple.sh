#!/bin/bash

for i in {1..20}
	do
		let a=$(($i%6))	
		if [ $a -eq 0 ]; then
			let b=$(($i+10))
			echo $b
		fi	
	done



