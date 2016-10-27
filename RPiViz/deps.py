""" Install system dependencies """
import os
from subprocess import call

print ('installing system dependencies')
    
def main():
    path = __file__.replace('deps.py','run.sh')
    print( call('chmod', '+x', path))
    print(call('run.sh'))
    
    # with open(path,'r') as run:
    #     for line in run:
    #         print 'executing',line
    #         print(call(line.split()))
            



