#! /usr/bin/env python2
# -*- conding: utf-8 -*-

from mininet.net import Mininet
from mininet.net import Controller, RemoteController, OVSKernelAP
from mininet.net import CLI
from mininet.net import setLogLevel, info

""" Custom topology example """

# Declare variables
ryu_ip = '127.0.0.1'
ryu_port = 6653

def customNet():
    """Create a customNet and add devices to it"""

    net = Mininet( topo=None, build=False )

    # Add Controller
    info( 'Adding Ryu Controller\n' )

    net.addController('c0', 
                        controller=RemoteController, 
                        ip=ryu_ip,
                        port=ryu_port
                     )
    
    # Add Hosts
    info( 'Adding hosts\n' )
    h1, h2, h3 = [ net.addHost(h) for h in ('h1', 'h2', 'h3') ]

        
    # Add Swtiches
    info( 'Adding hosts\n' )
    s1, s2, s3 = [ net.addHost(h) for h in ('s1', 's2', 's3') ]


    # Add Links
    info( 'Adding Swtich links' )
    for sa, sb in [ (s1, s2), (s2, s3) ]:
        net.addLink( sa, sb)


    for h, s in [ (h1, s1), (h2, s2), (h3, s3) ]:
        net.addLink( h, s)


    info('***Starting netwprk ***\n')
    net.start()


    info('***Running CLI ***')
    CLI( net )


    info('*** Stopping network ***')
    net.stop()



if __name__== '__main__':
    setLogLevel('info')
    customNet()

exit(0)



