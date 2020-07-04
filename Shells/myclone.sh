#!/bin/bash

name=$1
imgpath=/var/lib/libvirt/images/
xmlpath=/etc/libvirt/qemu/
if [ ! -e ${imgpath}${name}.img ]; then
	qemu-img create -f qcow2 -b ${imgpath}.node_base.qcow2   ${imgpath}${name}.img 20G
	#echo_success
else
	#echo_warning
	echo "${name}.img exists"
	exit 1
fi

if [ ! -e ${xmlpath}${name}.xml ]; then
	sed "s/node_base/${name}/g" ${xmlpath}.node_base.xml > ${xmlpath}${name}.xml	
else
	#echo_warning
        echo "${name}.xml exists"
	rm -rf ${imgpath}${name}.img
        exit 2
fi
virsh define /etc/libvirt/qemu/${name}.xml 


