#coding: utf-8

import sys
import csv
import os

csv_file = open(sys.argv[1])
svg_file = open(sys.argv[2])
svg_file = svg_file.read()

reader = csv.reader(csv_file)
header = reader.next()

for line in reader:
	i=0
	new_svg_str = svg_file
	for field in header:		
		new_svg_str = new_svg_str.replace(field,line[i])
		i=i+1
	new_svg_file_name = line[0]+".svg"
	new_svg_file = open(new_svg_file_name,"w")
	new_svg_file.write(new_svg_str)
	new_svg_file.close()

	os.system("inkscape -f \"%s\" -A \"%s\" && rm \"%s\"" %
				 (new_svg_file_name,
		 		  new_svg_file_name.replace("svg", "pdf"), new_svg_file_name))
