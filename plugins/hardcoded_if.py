'''
ddupdate plugin providing an ip address to use a
from an interface option.

See: ddupdate(8)
'''

import subprocess
import sys

from ddupdate.ddplugin import IpPlugin, IpAddr, dict_of_opts


class HardcodedIfPlugin(IpPlugin):
    '''
    Use address on hardcoded interface

    Options:
        if=interface
    '''
    _name = 'hardcoded-if'
    _oneliner = 'Get address from an configuration option interface'

    def get_ip(self, log, options):
        opts = dict_of_opts(options)
        if 'if' not in opts:
            log.error("Required option if= missing, giving up.")
            sys.exit(2)
        if_ = opts['if']
        address = IpAddr()
        output = subprocess.getoutput('ip address show dev ' + if_)
        address.parse_ifconfig_output(output)
        return address
