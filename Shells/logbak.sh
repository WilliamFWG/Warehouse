#!/bin/bash

date=`date "+%F_%H:%M:%S"`
logpath=/usr/local/nginx/logs
mv $logpath/access.log ${logpath}/access-${date}.log
mv $logpath/error.log ${logpath}/error-${date}.log
kill -10 `cat ${logpath}/nginx.pid`


