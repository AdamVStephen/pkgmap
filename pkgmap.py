#!/usr/bin/env python3

import pdb
import sys

# TODO: design a data structure to collect known information.


known_packages = {
        ''
        }

yum2apt = {
        'libxml' : 'surprise'
        }


def usage():
    print("pkgmap.py package_name : will return the alternative name from another package manager if known.")

class Mapper:
    def __init__(self, _map, _from = 'yum', _to = 'apt', verbose = False):
        self._map = _map
        self._from = _from
        self._to = _to
    def lookup(self, name):
        alt = self._map.get(name)
        if alt is None:
            print("No equivalent of %s (%s) found in %s" % (name, self._from, self._to), file=sys.stderr)
            return False
        else:
            print(alt)
            return True


if __name__ == '__main__':
    mapper = Mapper(yum2apt)
    if len(sys.argv) < 2: 
        usage()
        sys.exit(1)
    name  = sys.argv[1]
    # Assume redhat to debian
    found = mapper.lookup(name)
    sys.exit(0 if found else 2)
