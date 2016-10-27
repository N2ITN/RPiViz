import sys

import deps
if sys.argv[1] == 'setup':
	deps.main()
elif sys.argv[1] == 'start':
	import executor
	executor()