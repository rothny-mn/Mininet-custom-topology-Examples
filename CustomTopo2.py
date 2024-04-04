from mininet.topo import Topo 

class MyTopology(Topo):                         #like Linear(bus) topology

    def build(self):                            #def build(self, *args, **params):
        
        # Adding 3 hosts to the topology 
        Host1 = self.addHost("h1")
        Host2 = self.addHost("h2")
        Host3 = self.addHost("h3")

        # Adding 3 switches to the topology
        Switch1 = self.addSwitch("s1")
        Switch2 = self.addSwitch("s2")
        Switch3 = self.addSwitch("s3")

        # Adding Links or Connections between hosts and switches
        self.addLink(Host1, Switch1)
        self.addLink(Host2, Switch2)
        self.addLink(Host3, Switch3)

        # Connect all switches together to comm and topology functional 
        self.addLink(Switch1, Switch2)
        self.addLink(Switch2, Switch3)


# Create a dictionary to initialize our topology and give it name to pass as parameter to mn 
topos = {'AAAA': (lambda : MyTopology())}           

# AAAA is the name assigned to your custom topology
# (lambda : Mytopology()) defines an anonymous function (lambda function) that when called, creates an instance of the custom topology.


#  >>> Run mn in Terminal > sudo mn --custom /home/sdn-mn/mininet/custom/CustomTopo2.py --AAAA

                                                 