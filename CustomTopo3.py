# High-level API: Toplogy templates

class SingleSwitchTopo( Topo ):
    "Single Switch Topology"
    def build( self, count=1):
        hosts = [ self.addHost( 'h%d' % i )
                 for i in range( 1, count + 1 ) ]
        s1 = self.addSwitch( 's1')
        for h in hosts:
            self.addLink( h, s1)

net = Mininet( topo=SingleSwitchTopo( 3 ))
net.start()
CLT( net ) 
net.stop()

### Creating networks 
### Adding controller
### Adding hosts: h1 h2 h3
