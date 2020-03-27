#!/bin/bash
let a=$[RANDOM%11]
for i in {1..3}
	do
		read -p "Guess 0-10: " number
		echo "Round $i"
			if [ "$number" -eq "$a" ]; then
				echo '猜对啦!!'
				exit
			elif [ "$i" -ne 3 ]; then
				if [ "$number" -gt "$a" ]; then
					echo "猜大啦, 还有$((3-$i))次机会哦"
				else 
					echo "猜小啦, 还有$((3-$i))次机会哦" 
				fi
			
			else 
				echo "正确答案是: $a"
				echo '运气真差, 下次再来吧'
			fi 
	done
number=0
a=0
