import RPiViz as vz
import sys
import executor
import deps
if sys.argv[1] == 'setup':
	deps.main()
elif sys.argv[1] == 'start':
	executor()