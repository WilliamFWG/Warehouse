#!/bin/bash
if [ ! -d /etc/yum.repos.d/oldrepo ]; then
	mkdir /etc/yum.repos.d/oldrepo
fi
	mv -f /etc/yum.repos.d/*.repo /etc/yum.repos.d/oldrepo/
echo '[abc]
name=test
baseurl=http://172.25.254.254/content/rhel7.0/x86_64/dvd/
enabled=1
gpgcheck=0'> /etc/yum.repos.d/myyum.repo
