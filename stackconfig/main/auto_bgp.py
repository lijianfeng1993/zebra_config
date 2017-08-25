#!/usr/bin/env python
# coding = utf-8

import pexpect
import iface
import read_json

def auto_bgp(ip,port):
    child = pexpect.spawn('telnet %s %s' % (ip,port))
    child.expect('Password:')
    child.sendline('ubuntu\n')
    child.expect('>')
    child.sendline('enable\n')
    child.expect('#')
    child.sendline('conf t\n')
    child.expect('#')
    child.sendline('no router bgp 7675\n')
    child.expect('#')

    # get AS number
    As = read_json.js_data['BGP']['AS']
    child.sendline('router bgp {}\n'.format(str(As)).encode('utf-8'))
    child.expect('#')

    '''
    #!/usr/bin/env python
    # coding = utf-8
    from conf import read_json

    As = read_json.js_data['BGP']['AS']
    ibgp = read_json.js_data['BGP']['IBGP'].split(':')
    ebgp_remote_ip = read_json.js_data['BGP']['EBGP']['RemoteIP']
    ebgp_remote_as = read_json.js_data['BGP']['EBGP']['RemoteAS']

    print As
    print ibgp
    print ebgp_remote_ip
    print ebgp_remote_as

    '''

    addrs = []
    for iface_name in iface.get_physical_ifaces():
        addrs.extend(iface.get_addresses(iface_name))

    enabled_addrs = [i for i in addrs]

    if enabled_addrs:

        # select one as router-id
        id_addr = str(enabled_addrs[0].ip)
        child.sendline('bgp router-id {}\n'.format(id_addr).encode('utf-8'))
        child.expect('#')

        # configure IBGP neighbor
        ibgps = read_json.js_data['BGP']['IBGP'].split(':')
        for ibgp in ibgps:
            child.sendline('neighbor {} remote-as {}\n'.format(ibgp,As).encode('utf-8'))
            child.expect('#')
            if read_json.js_data['BGP']['ER'] == 'True':
                child.sendline('neighbor {} next-hop-self\n'.format(ibgp).encode('utf-8'))
                child.expect('#')

        # configure EBGP neighbor       
        if read_json.js_data['BGP']['ER'] == 'True':
            ebgp_ip = read_json.js_data['BGP']['EBGP']['RemoteIP']
            ebgp_as = read_json.js_data['BGP']['EBGP']['RemoteAS']
            child.sendline('neighbor {} remote-as {}\n'.format(ebgp_ip,ebgp_as).encode('utf-8'))
            child.expect('#')
            child.sendline('neighbor {} ebgp-multihop 5')
            child.expect('#')

        # calculate unique netwroks for all addresses
        networks = set(str(addr.network) for addr in enabled_addrs)

        # declare area for each of probed networks
        for network in networks:
            child.sendline('net {}\n'.format(network).encode('utf-8'))
            child.expect('#')

    # exit session
    child.sendline('ex\n')
    child.expect('#')
    child.sendline('ex\n')
