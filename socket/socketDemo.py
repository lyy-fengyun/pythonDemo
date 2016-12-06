#!/usr/bin/python
#coding=utf-8

import socket
from urlparse import urlparse
__author__='liyy'

hostname = socket.gethostname()
print hostname
ip = socket.gethostbyname(hostname)
print ip

ohost,domain,ips = socket.gethostbyname_ex(hostname)
print 'host name: ',ohost
print 'domain: ',domain
print 'ips: ',ips

domain2 = socket.getfqdn(hostname)
print hostname +': '+ domain2

host,doma,addresses = socket.gethostbyaddr(ips[-1])
print '---------------------------'
print host,doma,addresses

for url in ['http://www.baidu.com','http://cn.bing.com']:
    parse_url = urlparse(url)
    port = socket.getservbyname(parse_url.scheme)
    print url,port

#protocols = socket.getprotobyname('IPPROTO_TCP')
#print protocols

def get_constants(prefix):
    return dict((getattr(socket,n),n)
                for n in dir(socket)
                if n.startswith(prefix))
families = get_constants('AF_')
ty = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for res in socket.getaddrinfo('www.python.org','http'):
    family,socktype,proto,canonname,sockaddr = res
    
    print 'family     :',families[family]
    print 'socktype   :',ty[socktype]
    print 'protocol   :',protocols[proto]
    print 'Canonical name:',canonname
    print 'sock addr  :',sockaddr