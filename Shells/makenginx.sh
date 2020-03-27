#!/bin/bash
#yum -y install gcc openssl-devel pcre-devel
#tar -xf /root/nginx-1.12.2.tar.gz
cd nginx-1.12.2
./configure
make
make install

