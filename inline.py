import pynliner

import os
import sys

if len(sys.argv) < 2:
	print("You must provide an input file.")
	sys.exit(1)

filename = sys.argv[1]
outname = os.path.splitext(filename)[0] + ".inlined"


f = open(filename, 'r')
html = f.read()
f.close()
out = pynliner.fromString(html)

of = open(outname, 'w')
of.write(out)
of.close()
