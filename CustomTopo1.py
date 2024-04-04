# Mininet custom respository 

from mininet.topo import Topo       #this module provides classes for defining network topologies.
from mininet.net import Mininet     #used to create and manage Mininet networks.
from mininet.link import TCLink     #provides classes for defining link characteristics, such as bandwidth and delay.

class MyTopo(Topo):                        #code in Manual
    "Simple topology example"
    def __init__(self):
        "Create custom topo"

        # Initialize topology
        Topo.__init__(self)

        # Add hosts
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )

        # Add switches
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost ) 

topos = { 'mytopo': (lambda: MyTopo() ) } 
