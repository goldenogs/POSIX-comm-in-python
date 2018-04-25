#!/usr/bin/python

"""
Golden Hsu	
comm.py
Fall 2017
"""

import sys
from optparse import OptionParser

class comm:
	def __init__(self, filename):
		f = open(filename, 'r')
		self.lines = f.readlines()
		f.close()

def main():
	version_msg="%prog 0.99"
	usage_msg="%prog [OPTION]... FILE1 FILE2"

	parser = OptionParser(version=version_msg, usage=usage_msg)
	parser.add_option("-1", dest="sup1", action="store_true", default=False, help="suppress column 1")
	parser.add_option("-2", dest="sup2", action="store_true", default=False, help="suppress column 1")
	parser.add_option("-3", dest="sup3", action="store_true", default=False, help="suppress column 1")
	parser.add_option("-u", dest="inputUnsorted", action="store_true", default=False, help="compare even if the input is unsorted")

	options, args = parser.parse_args(sys.argv[1:])

	if len(args) != 2:
		parser.error("Invalid number of operands!")

	input_file1=args[0]
	input_file2=args[1]

	#putting lines into lists
	if input_file1=="-":
		col1=sys.stdin.readlines()
		col2=list(comm(input_file2).lines)
	elif input_file2=='-':
		col1=list(comm(input_file1).lines)
		col2=sys.stdin.readlines()
	elif input_file1=='-' and input_file2=='-':
		parser.error("Should only have one file through stdin!")
	else:
		col1=list(comm(input_file1).lines)		
		col2=list(comm(input_file2).lines)

	#fix if there is no new line in the last element
	if not '\n' in col1[-1]:
		col1[-1] = col1[-1]+'\n'
	if not '\n' in col2[-1]:
		col2[-1] = col2[-1]+'\n'  	
	#the third column
	common=[]

	#if input sorted
	if not options.inputUnsorted:
		#find the common lines
		for i in col1:
			if i in col2:
				common.append(i)
				col1.remove(i)
				col2.remove(i)
		#the final list for printing
		sorted_list=sorted(col1+col2+common)
		#loop through it and compare and print
		for i in sorted_list:
			if i in common and not options.sup3:
				if options.sup1 and options.sup2:
					sys.stdout.write(i)
				elif not options.sup1 and not options.sup2:
					sys.stdout.write('\t'+'\t'+i)
				else:
					sys.stdout.write('\t'+i)
				common.remove(i)
			elif i in col1 and not options.sup1:
				sys.stdout.write(i)
			elif i in col2 and not options.sup2:
				if options.sup1:
					sys.stdout.write(i)
				else:
					sys.stdout.write('\t'+i)
				
	#if input unsorted
	if options.inputUnsorted:
		for i in col1:
			#print common
			if i in col2:
				if not options.sup3:
					if not options.sup1 and not options.sup2:
						sys.stdout.write('\t'+'\t'+i)
					elif options.sup1 and options.sup2:
						sys.stdout.write(i)
					else:
						sys.stdout.write('\t'+i)
				col2.remove(i)
			#only in col1
			elif i in col1 and not i in col2:
				if not options.sup1:
					sys.stdout.write(i)
		#print out col2 (leftover)
		for i in col2:
			if not options.sup2:
				if options.sup1:
					sys.stdout.write(i)
				else:
					sys.stdout.write('\t'+i)


if __name__ == "__main__":
    main()


