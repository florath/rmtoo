'''
 rmtoo
   Free and Open Source Requirements Management Tool

  This function implements the digraph algorithm finding the connected
  components of a digraph.

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException


class CC_Components:

    def __init__(self):
        self.cs = []

    def get_length(self):
        return len(self.cs)

    @staticmethod
    def set_as_string(cs):
        r = set()
        for c in cs:
            r.add(c.name)
        return r

    def as_string(self):
        r = []
        for cs in self.cs:
            r.append(self.set_as_string(cs))
        return r

    def add_component(self, n):
        self.cs.append(set([n]))

    def find(self, n):
        c = 0
        for i in self.cs:
            if n in i:
                return c, i
            c += 1
        # Node not found
        raise RMTException(68, "Node [%s] not found" % n)

    def contract(self, n, v):
        _, g = self.find(n)
        hi, h = self.find(v)
        if g == h:
            # Already in one component - nothing to do
            return
        # Append elements from h to g
        g |= h
        # Remove h
        del(self.cs[hi])


def connected_components(dg):
    # This hold the components:
    #  the lists of the nodes which are in one component
    components = CC_Components()

    for n in dg.nodes:
        # Each node itself is a separate component
        components.add_component(n)

    for n in dg.nodes:
        # Run through the incoming and outgoing and collect the
        # different components
        for v in n.incoming:
            components.contract(n, v)
        for v in n.outgoing:
            components.contract(n, v)

    return components
