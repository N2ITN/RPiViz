""" Install system dependencies """
import os
from subprocess import call
try:
    import sh
except ImportError: 
    pip.main(["install", sh])

    
def main():
    path = __file__.replace('deps.py','run.sh')
    print('installing system dependencies..')
    chmod = sh.Command('chmod')
    chmod('+x', path)
    run = sh.Command(path)
    with open(path,'r') as run:
        for line in run:
            print call(line.split())
            

main()

