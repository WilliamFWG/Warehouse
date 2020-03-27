#!/bin/bash
a=$(who|wc -l)
[ $a -gt 3 ] && echo 'Warning : User More Than 3' | mail -s 'Warning' root
