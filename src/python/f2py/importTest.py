#! /usr/bin/env python

import sys

modules = ['OAS_API']

for name in modules:
    print ''
    print "Testing if module %s can be imported..." % name
    import_cmd = "import %s" % name
    try:
        exec import_cmd
    except Exception, inst:
        print "Error: %s." % inst
        sys.exit(1)
    # end try

    print "OK! Module %s was successfully imported." % name

print ''
