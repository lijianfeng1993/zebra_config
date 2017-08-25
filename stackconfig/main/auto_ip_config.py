#!/usr/bin/env python
#coding = utf-8

import pexpect
import iface

def auto_ip_config(ip,port):
    child = pexpect.spawn('telnet %s %s' % (ip,port))
    child.expect('Password:')
    child.sendline('ubuntu\n')   
    child.expect('>')
    child.sendline('enable\n') 
    child.expect('Password:')
    child.sendline('ubuntu\n')
    child.expect('#')

    # config mode
    child.sendline('conf t\n')
    child.expect('#')

    for iface_name in iface.get_physical_ifaces():
        # addresses
        addresses = iface.get_addresses(iface_name)
        if addresses:
            # interface config mode
            child.sendline('int {}\n'.format(iface_name).encode('utf-8'))  
            child.expect('#')
            
            # configure each address
            for addr in addresses:
                child.sendline('ip add {}\n'.format(addr.with_prefixlen).encode('utf-8'))
                child.expect('#')
    
            # fire up interface
            child.sendline('no sh\n')
            child.expect('#')
    
            # prepare for next interface
            child.sendline('ex\n')
            child.expect('#')    
        
            continue

        # current interface has no address
        pass
    
    # exit session
    child.sendline('ex\n')
    child.expect('#')
    child.sendline('ex\n')
