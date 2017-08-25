#!/usr/bin/env python
# coding = utf-8

import os,sys,signal
#import global_settings

import json

import auto_ip_config, auto_ospf_all, auto_ospf_exclude, auto_ospf_ips, auto_rip_ips, auto_rip_exclude, auto_bgp
import web_server

import read_json

def main():
    if read_json.js_data == None:
        auto_ip_config.auto_ip_config('127.0.0.1','2601')
        auto_ospf_all.auto_ospf_all('127.0.0.1','2604')
        print 'there no json file in the dir!!'
	print 'auto_ospf_all'

    elif read_json.js_data['Auto'] == 'True':
        if 'OSPF' in read_json.d:
            if 'ExcludeIP' in read_json.js_data['OSPF']:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_ospf_exclude.auto_ospf_exclude('127.0.0.1','2604')
                print 'auto_ospf_exclude'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp'

	    elif 'All' in read_json.js_data['OSPF']:
		auto_ip_config.auto_ip_config('127.0.0.1','2601')
		auto_ospf_all.auto_ospf_all('127.0.0.1','2604')
		print 'auto_ospf_all'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp'
		
            else:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_ospf_ips.auto_ospf_ips('127.0.0.1','2604')
                print 'auto_ospf_ips.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'

        elif 'RIP' in read_json.d:
            if 'ExcludeIP' in read_json.js_data['RIP']:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_rip_exclude.auto_rip_exclude('127.0.0.1','2602')
                print 'auto_rip_exclude.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'
    
            else:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_rip_ips.auto_rip_ips('127.0.0.1','2602')
                print 'auto_tip_ips.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'


        else:
            auto_ip_config.auto_ip_config('127.0.0.1','2601')
            auto_ospf_all.auto_ospf_all('127.0.0.1','2604')
            print 'there no ospf/rip/bgp in the json file!!'
            print 'auto_ospf_all.py'

    elif read_json.js_data['Auto'] == 'False':
        if 'OSPF' in read_json.d:
            if 'ExcludeIP' in read_json.js_data['OSPF']:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_ospf_exclude.auto_ospf_exclude('127.0.0.1','2604')
                print 'auto_ospf_exclude.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'
	    
	    elif 'All' in read_json.js_data['OSPF']:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_ospf_all.auto_ospf_all('127.0.0.1','2604')
                print 'auto_ospf_all'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp'

            else:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_ospf_ips.auto_ospf_ips('127.0.0.1','2604')
                print 'auto_ospf_ips.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'
        
        elif 'RIP' in read_json.d:
            if 'ExcludeIP' in read_json.js_data['RIP']:                            
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_rip_exclude.auto_rip_exclude('127.0.0.1','2602')
                print 'auto_rip_exclude.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'
    
            else:
                auto_ip_config.auto_ip_config('127.0.0.1','2601')
                auto_rip_ips.auto_rip_ips('127.0.0.1','2602')
                print 'auto_tip_ips.py'
                if 'BGP' in read_json.js_data:
                    auto_bgp.auto_bgp('127.0.0.1','2605')
                    print 'auto_bgp.py'
  
    
        else:
            auto_ip_config.auto_ip_config('127.0.0.1','2601')
            auto_ospf_all.auto_ospf_all('127.0.0.1','2604')
            print 'there no ospf/rip/bgp in the json file!!'
            print '  auto_ospf_all.py' 
        
        os.system('nohup python /root/zebra_config/stackconfig/main/web_server.py > /root/server.log 2>&1 &')
	print 'web server already running'

    else:
        print 'The json file if error!!!'

    
if __name__ == '__main__':
    main()



