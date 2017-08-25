#!/usr/bin/env python
# coding = utf-8

import pexpect
import iface
import read_json

def auto_ospf_ips(ip,port):
    child = pexpect.spawn('telnet %s %s' % (ip,port))
    child.expect('Password:')
    child.sendline('ubuntu\n')   
    child.expect('>')
    child.sendline('enable\n') 
    child.expect('#')
    child.sendline('conf t\n')
    child.expect('#')
    child.sendline('router ospf\n') 
    child.expect('#')

    '''
    #!/usr/bin/env python
    # coding = utf-8
    from conf import read_json
    import iface

    addrs = []
    ips = read_json.js_data['OSPF'].split(':')
    print ips

    for iface_name in iface.get_physical_ifaces():
        addrs.extend(iface.get_addresses(iface_name))
    print addrs

    enabled_addrs = [i for i in addrs if str(i.ip) in ips]
    print enabled_addrs

    '''

    addrs = []
    ips = read_json.js_data['OSPF'].split(':')

    for iface_name in iface.get_physical_ifaces():
        addrs.extend(iface.get_addresses(iface_name))
        
    enabled_addrs = [i for i in addrs if str(i.ip) in ips]

    if enabled_addrs:
        # select one as router-id
        id_addr = str(enabled_addrs[0].ip)
        child.sendline('router-id {}\n'.format(id_addr).encode('utf-8'))
        child.expect('#')

        # calculate unique netwroks for all addresses
        networks = set(str(addr.network) for addr in enabled_addrs)
        
        # declare area for each of probed networks
        for network in networks:
            child.sendline('net {} area 0\n'.format(network).encode('utf-8'))
            child.expect('#')
    
    # exit session
    child.sendline('ex\n')
    child.expect('#')
    child.sendline('ex\n')
