import RPiViz as vz
import sys

if sys.argv[1] == 'setup':
	vz.deps.main()
elif sys.argv[1] == 'start':
	vz.executor()