#!/usr/bin/env python

# Python
import json
import optparse
import os

NLAYERS = 100

def construct_groups():
    result = {}
    for i in range(NLAYERS):
        result['group_{}'.format(i)] = {
            'hosts': ['host_{}'.format(i)],
            'children': [],
        }
        if i > 0:
            result['group_{}'.format(i)]['children'].append(
                'group_{}'.format(i-1)
            )
    return result

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('--list', action='store_true', dest='list')
    parser.add_option('--host', dest='hostname', default='')
    options, args = parser.parse_args()
    if options.list:
        print json.dumps(construct_groups(), indent=4)
    elif options.hostname:
        print json.dumps({}, indent=4)
    else:
        print json.dumps({}, indent=4)
