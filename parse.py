# usage: change file to read
#        change read_in_vals if want different columns (probably shouldn't)
#        change number of iterations (line beginning 'for iter') (unnecessary for new log files)
#        change whether there was minimization or not (MINIM)
#        then run: python parse.py
import math
import numpy as np
import sys

read_in_vals = [0,1,2,3,4,5,6]

file_to_read = '../coarse_9.8/coarse_walls_9.8_npt_1atm_298K.o142062.log'
time_start=0
time_stop=200000
step_diff=100
num_lines=1
total_steps = (time_stop-time_start)/step_diff/num_lines
MINIM=False

file_to_write = '{0}.PARSED'.format(file_to_read)
data = open(file_to_read)
parse_out = open(file_to_write, 'w+')
line=data.readline()
if MINIM:
    while line[:4] != 'Step':
        line=data.readline()
    line=data.readline()
    line=data.readline()
while line[:4] != 'Step':
    line=data.readline()
cols=line.split()
print cols

for j in np.arange(len(read_in_vals)-1):
    parse_out.write('{0} '.format(cols[read_in_vals[j]]))
parse_out.write('{0}\n'.format(cols[read_in_vals[len(read_in_vals)-1]]))
for iter in np.arange(total_steps):
    for i in np.arange(num_lines):
        line=data.readline()
        #print line
        s=line.split()
        # save values
        for j in np.arange(len(read_in_vals)-1):
            parse_out.write('{0} '.format(s[read_in_vals[j]]))
        parse_out.write('{0}\n'.format(s[read_in_vals[len(read_in_vals)-1]]))
    #data.readline() # SHAKE stats
    #data.readline()
    #data.readline()
# take care of 'edge cases' in the printing
# if there is no error, change the 'while' condition
#line=data.readline()
#while line[:5] != 'ERROR':
#    #print line
#    s=line.split()
#    # save values
#    for j in np.arange(len(read_in_vals)-1):
#        parse_out.write('{0} '.format(s[read_in_vals[j]]))
#    parse_out.write('{0}\n'.format(s[read_in_vals[len(read_in_vals)-1]]))
#    line=data.readline()
