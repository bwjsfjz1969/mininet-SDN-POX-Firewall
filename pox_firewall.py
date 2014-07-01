Last login: Tue Jul  1 09:33:32 on ttys000
ChristopherMini:~ cpayne$ ssh -X mininet@192.168.1.9
mininet@192.168.1.9's password: 
Welcome to Ubuntu 13.04 (GNU/Linux 3.8.0-19-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Your Ubuntu release is not supported anymore.
For upgrade information, please visit:
http://www.ubuntu.com/releaseendoflife

New release '13.10' available.
Run 'do-release-upgrade' to upgrade to it.

Last login: Tue Jul  1 06:34:55 2014 from 192.168.1.5
mininet@mininet-vm:~$ cd pox 
mininet@mininet-vm:~/pox$ cd pox
mininet@mininet-vm:~/pox/pox$ ll
total 296
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 ./
drwxrwxr-x  7 mininet mininet  4096 Jun 30 19:13 ../
-rwxrwxr-x  1 mininet mininet 14917 Sep 19  2013 boot.py*
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:43 boot.pyc
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:13 boot.pyo
-rw-rw-r--  1 mininet mininet 16914 Sep 19  2013 core.py
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:43 core.pyc
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:13 core.pyo
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 datapaths/
drwxrwxr-x  2 mininet mininet  4096 Jun 30 19:55 forwarding/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 host_tracker/
-rw-rw-r--  1 mininet mininet   845 Sep 19  2013 __init__.py
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:43 __init__.pyc
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:13 __init__.pyo
drwxrwxr-x  8 mininet mininet  4096 Jun 30 18:43 lib/
-rw-rw-r--  1 mininet mininet 35162 Sep 19  2013 license.py
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:43 license.pyc
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:13 license.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:13 log/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 messenger/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:35 misc/
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:43 openflow/
-rw-rw-r--  1 mininet mininet  3970 Sep 19  2013 py.py
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:43 py.pyc
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:13 py.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 19:18 samples/
-rw-rw-r--  1 mininet mininet  3734 Sep 19  2013 tk.py
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 topology/
drwxrwxr-x  3 mininet mininet  4096 Sep 19  2013 web/
mininet@mininet-vm:~/pox/pox$ cd ..
mininet@mininet-vm:~/pox$ ll
total 92
drwxrwxr-x  7 mininet mininet  4096 Jun 30 19:13 ./
drwxr-xr-x 22 mininet mininet  4096 Jul  1 06:36 ../
-rw-rw-r--  1 mininet mininet 35147 Sep 19  2013 COPYING
lrwxrwxrwx  1 mininet mininet     6 Sep 19  2013 debug-pox.py -> pox.py*
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 ext/
drwxrwxr-x  8 mininet mininet  4096 Sep 19  2013 .git/
-rw-rw-r--  1 mininet mininet   172 Sep 19  2013 .gitignore
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 pox/
-rwxrwxr-x  1 mininet mininet  1362 Sep 19  2013 pox.py*
-rw-rw-r--  1 mininet mininet  9055 Sep 19  2013 .pylint
-rw-rw-r--  1 mininet mininet  1286 Sep 19  2013 README
-rw-rw-r--  1 mininet mininet    87 Sep 19  2013 setup.cfg
drwxrwxr-x  5 mininet mininet  4096 Sep 19  2013 tests/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 tools/
mininet@mininet-vm:~/pox$ find . | grep forward
./pox/forwarding
./pox/forwarding/l2_learning.pyo
./pox/forwarding/l3_learning.py
./pox/forwarding/l2_learning.py
./pox/forwarding/hub.pyo
./pox/forwarding/l2_pairs.py
./pox/forwarding/__init__.pyo
./pox/forwarding/hub.py
./pox/forwarding/l2_multi.py
./pox/forwarding/__init__.py
./pox/forwarding/l2_nx.py
./pox/forwarding/l2_flowvisor.py
mininet@mininet-vm:~/pox$ vi ./pox/forwarding/hub.py
mininet@mininet-vm:~/pox$ ll
total 92
drwxrwxr-x  7 mininet mininet  4096 Jun 30 19:13 ./
drwxr-xr-x 22 mininet mininet  4096 Jul  1 06:37 ../
-rw-rw-r--  1 mininet mininet 35147 Sep 19  2013 COPYING
lrwxrwxrwx  1 mininet mininet     6 Sep 19  2013 debug-pox.py -> pox.py*
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 ext/
drwxrwxr-x  8 mininet mininet  4096 Sep 19  2013 .git/
-rw-rw-r--  1 mininet mininet   172 Sep 19  2013 .gitignore
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 pox/
-rwxrwxr-x  1 mininet mininet  1362 Sep 19  2013 pox.py*
-rw-rw-r--  1 mininet mininet  9055 Sep 19  2013 .pylint
-rw-rw-r--  1 mininet mininet  1286 Sep 19  2013 README
-rw-rw-r--  1 mininet mininet    87 Sep 19  2013 setup.cfg
drwxrwxr-x  5 mininet mininet  4096 Sep 19  2013 tests/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 tools/
mininet@mininet-vm:~/pox$ cd pox
mininet@mininet-vm:~/pox/pox$ ll
total 296
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 ./
drwxrwxr-x  7 mininet mininet  4096 Jun 30 19:13 ../
-rwxrwxr-x  1 mininet mininet 14917 Sep 19  2013 boot.py*
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:43 boot.pyc
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:13 boot.pyo
-rw-rw-r--  1 mininet mininet 16914 Sep 19  2013 core.py
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:43 core.pyc
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:13 core.pyo
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 datapaths/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:37 forwarding/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 host_tracker/
-rw-rw-r--  1 mininet mininet   845 Sep 19  2013 __init__.py
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:43 __init__.pyc
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:13 __init__.pyo
drwxrwxr-x  8 mininet mininet  4096 Jun 30 18:43 lib/
-rw-rw-r--  1 mininet mininet 35162 Sep 19  2013 license.py
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:43 license.pyc
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:13 license.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:13 log/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 messenger/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:35 misc/
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:43 openflow/
-rw-rw-r--  1 mininet mininet  3970 Sep 19  2013 py.py
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:43 py.pyc
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:13 py.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 19:18 samples/
-rw-rw-r--  1 mininet mininet  3734 Sep 19  2013 tk.py
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 topology/
drwxrwxr-x  3 mininet mininet  4096 Sep 19  2013 web/
mininet@mininet-vm:~/pox/pox$ cd samples
mininet@mininet-vm:~/pox/pox/samples$ ll
total 28
drwxrwxr-x  2 mininet mininet 4096 Jun 30 19:18 ./
drwxrwxr-x 13 mininet mininet 4096 Jun 30 18:43 ../
-rw-rw-r--  1 mininet mininet  973 Sep 19  2013 httopo.py
-rw-rw-r--  1 mininet mininet    0 Sep 19  2013 __init__.py
-rw-rw-r--  1 mininet mininet 2085 Sep 19  2013 mixed_switches.py
-rw-rw-r--  1 mininet mininet 1105 Sep 19  2013 pretty_log.py
-rw-rw-r--  1 mininet mininet 1517 Sep 19  2013 spanning_tree.py
-rw-rw-r--  1 mininet mininet 1012 Sep 19  2013 topo.py
mininet@mininet-vm:~/pox/pox/samples$ cd ..
mininet@mininet-vm:~/pox/pox$ ll
total 296
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 ./
drwxrwxr-x  7 mininet mininet  4096 Jun 30 19:13 ../
-rwxrwxr-x  1 mininet mininet 14917 Sep 19  2013 boot.py*
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:43 boot.pyc
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:13 boot.pyo
-rw-rw-r--  1 mininet mininet 16914 Sep 19  2013 core.py
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:43 core.pyc
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:13 core.pyo
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 datapaths/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:37 forwarding/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 host_tracker/
-rw-rw-r--  1 mininet mininet   845 Sep 19  2013 __init__.py
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:43 __init__.pyc
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:13 __init__.pyo
drwxrwxr-x  8 mininet mininet  4096 Jun 30 18:43 lib/
-rw-rw-r--  1 mininet mininet 35162 Sep 19  2013 license.py
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:43 license.pyc
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:13 license.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:13 log/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 messenger/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:35 misc/
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:43 openflow/
-rw-rw-r--  1 mininet mininet  3970 Sep 19  2013 py.py
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:43 py.pyc
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:13 py.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 19:18 samples/
-rw-rw-r--  1 mininet mininet  3734 Sep 19  2013 tk.py
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 topology/
drwxrwxr-x  3 mininet mininet  4096 Sep 19  2013 web/
mininet@mininet-vm:~/pox/pox$ ll
total 296
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 ./
drwxrwxr-x  7 mininet mininet  4096 Jun 30 19:13 ../
-rwxrwxr-x  1 mininet mininet 14917 Sep 19  2013 boot.py*
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:43 boot.pyc
-rw-rw-r--  1 mininet mininet 12135 Jun 30 18:13 boot.pyo
-rw-rw-r--  1 mininet mininet 16914 Sep 19  2013 core.py
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:43 core.pyc
-rw-rw-r--  1 mininet mininet 18144 Jun 30 18:13 core.pyo
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 datapaths/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:37 forwarding/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 host_tracker/
-rw-rw-r--  1 mininet mininet   845 Sep 19  2013 __init__.py
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:43 __init__.pyc
-rw-rw-r--  1 mininet mininet   309 Jun 30 18:13 __init__.pyo
drwxrwxr-x  8 mininet mininet  4096 Jun 30 18:43 lib/
-rw-rw-r--  1 mininet mininet 35162 Sep 19  2013 license.py
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:43 license.pyc
-rw-rw-r--  1 mininet mininet 35297 Jun 30 18:13 license.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:13 log/
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 messenger/
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:35 misc/
drwxrwxr-x  2 mininet mininet  4096 Jun 30 18:43 openflow/
-rw-rw-r--  1 mininet mininet  3970 Sep 19  2013 py.py
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:43 py.pyc
-rw-rw-r--  1 mininet mininet  4258 Jun 30 18:13 py.pyo
drwxrwxr-x  2 mininet mininet  4096 Jun 30 19:18 samples/
-rw-rw-r--  1 mininet mininet  3734 Sep 19  2013 tk.py
drwxrwxr-x  2 mininet mininet  4096 Sep 19  2013 topology/
drwxrwxr-x  3 mininet mininet  4096 Sep 19  2013 web/
mininet@mininet-vm:~/pox/pox$ 
mininet@mininet-vm:~/pox/pox$ cd forwarding
mininet@mininet-vm:~/pox/pox/forwarding$ ll
total 92
drwxrwxr-x  2 mininet mininet  4096 Jul  1 06:37 ./
drwxrwxr-x 13 mininet mininet  4096 Jun 30 18:43 ../
-rw-rw-r--  1 mininet mininet  1184 Sep 19  2013 hub.py
-rw-rw-r--  1 mininet mininet  1111 Jun 30 18:13 hub.pyo
-rw-rw-r--  1 mininet mininet   743 Sep 19  2013 __init__.py
-rw-rw-r--  1 mininet mininet   218 Jun 30 18:13 __init__.pyo
-rw-rw-r--  1 mininet mininet  4518 Sep 19  2013 l2_flowvisor.py
-rw-rw-r--  1 mininet mininet  6779 Sep 19  2013 l2_learning.py
-rw-rw-r--  1 mininet mininet  6307 Jun 30 19:55 l2_learning.pyo
-rw-rw-r--  1 mininet mininet 15473 Sep 19  2013 l2_multi.py
-rw-rw-r--  1 mininet mininet  4220 Sep 19  2013 l2_nx.py
-rw-rw-r--  1 mininet mininet  2846 Sep 19  2013 l2_pairs.py
-rw-rw-r--  1 mininet mininet 12555 Sep 19  2013 l3_learning.py
mininet@mininet-vm:~/pox/pox/forwarding$ vi l2_learning.py
mininet@mininet-vm:~/pox/pox/forwarding$ cd
mininet@mininet-vm:~$ skool
mininet@mininet-vm:~/gt-cs6250$ ll
total 48
drwxrwxr-x 11 mininet mininet 4096 Jun 16 14:12 ./
drwxr-xr-x 22 mininet mininet 4096 Jul  1 08:06 ../
drwxrwxr-x  3 mininet mininet 4096 Jun 16 14:12 assignment-2/
drwxrwxr-x  3 mininet mininet 4096 Jun 16 14:12 assignment-3/
drwxrwxr-x  3 mininet mininet 4096 Jun 16 14:12 assignment-4/
drwxrwxr-x  3 mininet mininet 4096 Jun 18 07:45 assignment-5/
drwxrwxr-x 10 mininet mininet 4096 Jun 26 15:00 assignment-6/
drwxrwxr-x  2 mininet mininet 4096 Jun 30 19:50 assignment-7/
drwxrwxr-x  2 mininet mininet 4096 Jun 16 14:12 assignment-8/
drwxrwxr-x  3 mininet mininet 4096 Jun 16 14:12 assignment-9/
drwxrwxr-x  8 mininet mininet 4096 Jun 30 17:15 .git/
-rw-rw-r--  1 mininet mininet   58 Jun 16 14:12 README.md
mininet@mininet-vm:~/gt-cs6250$ cd *7
mininet@mininet-vm:~/gt-cs6250/assignment-7$ ll
total 28
drwxrwxr-x  2 mininet mininet 4096 Jun 30 19:50 ./
drwxrwxr-x 11 mininet mininet 4096 Jun 16 14:12 ../
-rw-rw-r--  1 mininet mininet   53 Jun 16 14:12 firewall-policies.csv
-rw-rw-r--  1 mininet mininet 2117 Jun 30 19:50 pox_firewall.py
-rw-rw-r--  1 mininet mininet 3729 Jun 16 14:12 pyretic_firewall.py
-rw-rw-r--  1 mininet mininet 4603 Jun 30 18:56 pyretic_switch.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ cp ~/pox/pox/misc/pox_firewall.py .
mininet@mininet-vm:~/gt-cs6250/assignment-7$ cp ~/pox/pox/misc/pox_firewall.py pox_firewall.py.cp
mininet@mininet-vm:~/gt-cs6250/assignment-7$ ll
total 32
drwxrwxr-x  2 mininet mininet 4096 Jul  1 08:06 ./
drwxrwxr-x 11 mininet mininet 4096 Jun 16 14:12 ../
-rw-rw-r--  1 mininet mininet   53 Jun 16 14:12 firewall-policies.csv
-rw-rw-r--  1 mininet mininet 2412 Jul  1 08:06 pox_firewall.py
-rw-rw-r--  1 mininet mininet 2412 Jul  1 08:06 pox_firewall.py.cp
-rw-rw-r--  1 mininet mininet 3729 Jun 16 14:12 pyretic_firewall.py
-rw-rw-r--  1 mininet mininet 4603 Jun 30 18:56 pyretic_switch.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ vi pox_firewall.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ cp pox_firewall.py ~/pox/pox/misc/pox_firewall.p
mininet@mininet-vm:~/gt-cs6250/assignment-7$ vi pox_firewall.py.cp
mininet@mininet-vm:~/gt-cs6250/assignment-7$ cp ~/pox/pox/misc/pox_firewall.py pox_firewall.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ vi pox_firewall.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ vi pox_firewall.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ cp pox_firewall.py ~/pox/pox/misc/pox_firewall.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ pwd
/home/mininet/gt-cs6250/assignment-7
mininet@mininet-vm:~/gt-cs6250/assignment-7$ 
mininet@mininet-vm:~/gt-cs6250/assignment-7$ ll
total 32
drwxrwxr-x  2 mininet mininet 4096 Jul  1 10:25 ./
drwxrwxr-x 11 mininet mininet 4096 Jun 16 14:12 ../
-rw-rw-r--  1 mininet mininet   53 Jun 16 14:12 firewall-policies.csv
-rw-rw-r--  1 mininet mininet 2514 Jul  1 10:25 pox_firewall.py
-rw-rw-r--  1 mininet mininet 2412 Jul  1 08:06 pox_firewall.py.cp
-rw-rw-r--  1 mininet mininet 3729 Jun 16 14:12 pyretic_firewall.py
-rw-rw-r--  1 mininet mininet 4603 Jun 30 18:56 pyretic_switch.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ ll
total 32
drwxrwxr-x  2 mininet mininet 4096 Jul  1 10:25 ./
drwxrwxr-x 11 mininet mininet 4096 Jun 16 14:12 ../
-rw-rw-r--  1 mininet mininet   53 Jun 16 14:12 firewall-policies.csv
-rw-rw-r--  1 mininet mininet 2514 Jul  1 10:25 pox_firewall.py
-rw-rw-r--  1 mininet mininet 2412 Jul  1 08:06 pox_firewall.py.cp
-rw-rw-r--  1 mininet mininet 3729 Jun 16 14:12 pyretic_firewall.py
-rw-rw-r--  1 mininet mininet 4603 Jun 30 18:56 pyretic_switch.py
mininet@mininet-vm:~/gt-cs6250/assignment-7$ cat pox_firewall.py
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
mininet@mininet-vm:~/gt-cs6250/assignment-7$ vi pox_firewall.py

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

"pox_firewall.py" 80L, 2514C                                                      1,1           Top
