'''
Udacity:
- Software Defined Networking (SDN) course
-- Assignment 7 Programming Assignment

Professor: Nick Feamster
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
from csv import DictReader


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

# Add your global variables here ...

# Note: Policy is data structure which contains a single
# source-destination flow to be blocked on the controller.
Policy = namedtuple('Policy', ('dl_src', 'dl_dst'))


class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def read_policies (self, file):
        with open(file, 'r') as f:
            reader = DictReader(f, delimiter = ",")
            policies = {}
            for row in reader:
                policies[row['id']] = Policy(EthAddr(row['mac_0']), EthAddr(row['mac_1']))
        return policies

    def _handle_ConnectionUp (self, event):
        policies = self.read_policies(policyFile)
        for policy in policies.itervalues():
        # TODO: implement the code to add a rule to block the flow
        # between the source and destination specified in each policy

        # Note: The policy data structure has two fields which you can
        # access to turn the policy into a rule. policy.dl_src will
        # give you the source mac address and policy.dl_dst will give
        # you the destination mac address

        # Note: Set the priority for your rule to 20 so that it
        # doesn't conflict with the learning bridge setup
        #    pass
		# debug to see the source and destination MAC addresses
		log.debug("~~> Source Mac is %s", policy.dl_src)
		log.debug("~~> Destination Mac is %s", policy.dl_dst)

		# define a set of headers for packets to match against
		# if the MAC address is between H1 and H2 block
		#match = of.ofp_match()
		#match.dl_src = policy.dl_src
 		#match.dl_dst = policy.dl_dst
		match = of.ofp_match(dl_src = policy.dl_src, dl_dst = policy.dl_dst)

		# install the mods to block matches
		fm = of.ofp_flow_mod()
		fm.priority = 20  
		fm.match = match
		event.connection.send(fm)

		log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
