# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import ipaddress
import threading

#import pyroute2
# for pyinstaller
# again for nuitka
from pyroute2.iproute import IPRoute


IP = IPRoute()


def _transform_attrs_inplace(result):
    for item in result:
        item['attrs'] = dict(item['attrs'])
    return result


def is_physical_iface(iface):
    device_path = os.readlink(os.path.join('/sys/class/net', iface))
    return not device_path.startswith('../../devices/virtual/')


def get_physical_ifaces():
    ifaces = os.listdir('/sys/class/net')
    return [iface for iface in ifaces if is_physical_iface(iface)]


def get_addresses(iface):
    addresses = _transform_attrs_inplace(IP.get_addr(label=iface))
    return [
        ipaddress.ip_interface(
            '{}/{}'.format(
                addr['attrs']['IFA_ADDRESS'],
                addr['prefixlen'],
            )
        )
        for addr in addresses
    ]

