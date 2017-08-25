
from bottle import Bottle, ServerAdapter, route, run,request, post
import os,signal
import pexpect
import json
import iptc

@route('/add_ip_route/<des_ip>/<mask>/<next_ip>')
def add_ip_route(des_ip,mask,next_ip):
    child = pexpect.spawn('telnet localhost 2601')
    child.expect('Password:')
    child.sendline('ubuntu\n')
    child.expect('>')
    child.sendline('enable\n')
    child.expect('Password:')
    child.sendline('ubuntu\n')
    child.expect('#')
    child.sendline('conf t\n')
    child.expect('#')
    child.sendline('ip route {}/{} {}\n'.format(des_ip,mask,next_ip))
    child.expect('#')
    child.sendline('ex\n')
    child.expect('#')
    child.sendline('ex\n')
    return 'Already add a static route'

@route('/del_ip_route/<des_ip>/<mask>/<next_ip>')
def del_ip_route(des_ip,mask,next_ip):
    child = pexpect.spawn('telnet localhost 2601')
    child.expect('Password:')
    child.sendline('ubuntu\n')
    child.expect('>')
    child.sendline('enable\n')
    child.expect('Password:')
    child.sendline('ubuntu\n')
    child.expect('#')
    child.sendline('conf t\n')
    child.expect('#')
    child.sendline('no ip route {}/{} {}\n'.format(des_ip,mask,next_ip))
    child.expect('#')
    child.sendline('ex\n')
    child.expect('#')
    child.sendline('ex\n')
    return 'Already del a static route'

@route('/route')
def show_ip_route():
    route = os.popen('route -n')
    return route

@route('/stop')
def show_ip_route():
    os.kill(os.getpid(),signal.SIGTERM)
    return 'web server has closed.'

@post('/filter')
def add_rule_packet_filter():
	src = request.json['src']
	dst = request.json['dst']
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"FORWARD")
        rule = iptc.Rule()
        rule.set_src(src)
        rule.set_dst(dst)
        target = iptc.Target(rule,"DROP")
        rule.target = target
        chain.insert_rule(rule)

@post('/nofilter')
def remove_rule_packet_filter():
	src = request.json['src']
        dst = request.json['dst']
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"FORWARD")
        rule = iptc.Rule()
        rule.set_src(src)
        rule.set_dst(dst)
        target = iptc.Target(rule,"DROP")
        rule.target = target
        chain.delete_rule(rule)

if __name__ == "__main__":
    try:
        run(host = "0.0.0.0",port = 4501)
    except Exception,ex:
        print ex
