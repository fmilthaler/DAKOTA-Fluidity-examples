#!/usr/bin/env python
import sys
import re
import os
import subprocess
import fileinput
import shutil
import stat
#sys.argv[1] is param.in
#sys.argv[2] is result.out

#The script follows that supplied with Dakota under script_interface/Python and the ones 
#supplied to be used in conjunction with OpenFoam.

#The script acts in a similar fashion to when operating with OpenFoam, each new simulation 
#is done within a new work directory created by dakota, outputting the final result in the result.out
#file


'''
helper function
'''
#creates a dictionary which holds a mapping between the name of the result and the value,
#obtained from the last line of the .stat file supplied in the argument
def extract_result_from_stat(filepath):
	#extracts the field names and store them in an array
	#directory = "/home/ks1713/fluidity/examples/driven_cavity/driven_cavity-64"
	#filepath = os.path.join(directory , "driven_cavity.stat")
	f = open(filepath,'r')

	fields_vector = []

	#this is really, really bad im sorry, but just for experiment;s sake

	whole_file = f.readlines()

	f.close()

	field_regex = '<field column=\"(\d+)\"\sname=\"(\w*)\"\sstatistic=\"(\w*)\"\s*.*/>'

	for line in whole_file:
		if re.match(r'</header>', line):
			break
		match = re.search(field_regex, line)
		if match:
		  match_2 = re.search('components=\"(\d+)\"', line)
		  if match_2:
		  	count = int(match_2.group(1))
		  	for i in range(1,count+1):
		  		fields_vector.append(match.group(2)+'_'+match.group(3)+'_'+str(i))
		  else:
		  	fields_vector.append(match.group(2)+'_'+match.group(3))

	results_vector = whole_file[-1].strip().split()
	

	#read in last line of stat file and split on space, store results in array
	#print len(results_vector)
	#iterates through the array along with the last line of the stat file
	#and saves as a dictionary
	result_dictionary = {}
	for i in range(0, len(fields_vector)):
		result_dictionary[fields_vector[i]] = float(results_vector[i])
	'''
	sorted_keys = result_dictionary.keys()
	sorted_keys.sort()
	for key in sorted_keys:
		print (key,result_dictionary[key])
		print '\n'
		'''
	#return the dictionary

	return result_dictionary


observed_value = -0.863353 


'''
PRE_PROCESSING
'''

# setup regular expressions for parameter/label matching
e = '-?(?:\\d+\\.?\\d*|\\.\\d+)[eEdD](?:\\+|-)?\\d+' # exponential notation
f = '-?\\d+\\.\\d*|-?\\.\\d+'                        # floating point
i = '-?\\d+'                                         # integer
value = e+'|'+f+'|'+i                                # numeric field
tag = '\\w+(?::\\w+)*'                               # text tag field

# regular expression for aprepro parameters format
aprepro_regex = re.compile('^\s*\{\s*(' + tag + ')\s*=\s*(' + value +')\s*\}$')
# regular expression for standard parameters format
standard_regex = re.compile('^\s*(' + value +')\s+(' + tag + ')$')

# open DAKOTA parameters file for reading
paramsfile = open(sys.argv[1], 'r')

# extract the parameters from the file and store in a dictionary
paramsdict = {}
for line in paramsfile:
    m = aprepro_regex.match(line)
    if m:
        paramsdict[m.group(1)] = m.group(2)
    else:
        m = standard_regex.match(line)
        if m:
            paramsdict[m.group(2)] = m.group(1)

paramsfile.close()

#copy over all the files required

for stuff in os.listdir('../casebase'):
	shutil.copyfile('../casebase/'+stuff, stuff)

#copy over the template file to the current directory and change suffix
os.system('pwd')

shutil.copy('../templatedir/initial_condition.py', "initial_condition.py")
for filename in os.listdir("."):
	os.chmod(filename, stat.S_IRWXU)
#substitute this value into the template file

f = fileinput.input('initial_condition.py', inplace=True)
for line in f:
	match = re.search(".*{(\w+)}.*", line.strip())
	if match:
		line = line.replace("{" + match.group(1) + "}", paramsdict[match.group(1)])
	sys.stdout.write(line)
'''
ANALYSIS
'''

#run the simulation
#os.system('make')
os.system('fluidity tsunami.flml')

'''
POST_PROCESSING
'''

os.system('pwd')

from fluidity_tools import stat_parser
detector_results = stat_parser("tsunami.detectors")
free_surface = detector_results["Water"]["FreeSurface"]["DetectorA"][-1]

outfile = open('results.out.tmp','w')
#select the right parameter from final_output and write it to the outfile. access using dictionary style
outfile.write(str(free_surface - observed_value))

print ("fluidity detector freesurface value: " + str(free_surface))

shutil.move('results.out.tmp', sys.argv[2])

print ("----finished running simulation for " + os.getcwd().split('/')[-1] + "----")