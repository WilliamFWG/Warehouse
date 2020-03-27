#!/bin/bash
X=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
a=0
i=0
m=
n=
for a in {1..8}
	do
		i=$((RANDOM%62))
		n=${X:$i:1}
		m=${m}${n}
	done
echo $m
