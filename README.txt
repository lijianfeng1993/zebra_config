1. Add path to PYTHONPATH
	export PYTHONPATH:$PYTHONPATH:/root/zebra_config/stackconfig
   or edit ~/.bashrc and add:
	 export PYTHONPATH:$PYTHONPATH:/root/zebra_config/stackconfig 
   then source ~/.bashrc

2. You need to edit the config file first so the router will know how to config
  The example of the test.json , the file in /root/zebra_config/examples

  (1). no test.json file  //config as default {"Auto":"True","OSPF":"All"}

  (2). {"Auto":"True"}     //defalt configuration is {"Auto":"True","OSPF":"All"}

  (3). {
	"Auto":"True",
	"OSPF":"192.168.253.128"
	}        
	   //need to configure 192.168.253.128 in ospf

  (4). {
	"Auto":"True",
	"OSPF":{"ExcludeIP":"192.168.144.128"}
	}        
	   //all ipaddress need to configure in ospf exclude 192.168.144.128

  (5). {
	"Auto":"True",
	"RIP":"192.168.253.128"
	}        
	   //need to configure 192.168.253.128 in rip
	  
  (6). {
	"Auto":"True",
	"RIP":{"ExcludeIP":"192.168.144.128"}
	}        
	   //all ipaddress need to configure in rip exclude 192.168.144.128
	
  (7). {
	"Auto":"True",
	"RIP":"192.168.10.3",
	"BGP":{"AS":"1",
		  "ER":"False",
		  "IBGP":"192.168.10.4"}
	}
	   // configure 192.168.10.3 in rip 
	   // the router not the ER in BGP
	   // the router in the BGP AS 1
	   // and it's IBGP neighbor is 192.168.10.4
	   // you can replace the rip with ospf
	
  (8). {
	"Auto":"True",
	"RIP":,{"ExcludeIP":"192.168.20.3},
	"BGP":{"AS":"1",
		  "ER":"True",
		  "IBGP":"192.168.10.3"}
		  "EBGP":{"RemoteIP":"192.168.20.4","RemoteAS":"2"}}
	}
	   // all ipaddress need to configure in rip exclude 192.168.20.3
	   // the router is the ER in BGP
	   // the router in the BGP AS 1
	   // and it's IBGP neighbor is 192.168.10.3
	   // it's EBGP neighbor is 192.168.20.4 in BGP AS 2
	   // you can replace the rip with ospf
	
  (9).
	if "Auto":"False"
	the router will start webserver,host:0.0.0.0 , port:4505
	other config as same as what in "Auto":'True'

3. Usage:
	/path/to/virtualenv/bin/python /path/to/stackconfig/main/main.py 

4. web api
	add static route:
		curl http://ip:port/add_ip_route/<des_net>/<mask>/<next_ip>
			example: curl http://192.168.1.11:4505/add_ip_route/192.168.30.0/24/192.168.1.21
			
	delete static route:
		curl http://ip:port/del_ip_route/<des_net>/<mask>/<next_ip>
		
	show route table:
		curl http://ip:port/route
		
	stop the webserver in remote:
		curl http://ip:port/stop
	
	
