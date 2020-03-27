#!/bin/bash
if [ $# -eq 0 ]; then
	echo 'Require st|stop|restart|stat'
	exit 1
fi
case $1 in 
st|start)
	/usr/local/nginx/sbin/nginx;;
stop)
	/usr/local/nginx/sbin/nginx -s stop;;
restart)
	/usr/local/nginx/sbin/nginx -s stop
	/usr/local/nginx/sbin/nginx;;
stat)
	netstat -ntulp |grep -q nginx 
	[ $? -eq 0 ] && echo "Nginx Running" || echo "Nginx Not Running";; 
*)
	echo 'Require st|stop|restart|stat'
esac
