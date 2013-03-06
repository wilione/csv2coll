#csv2coll by Andrew Willingham
#updated 3/5/2013
#www.wilhelmsound.com
#http://github.com/wilione/csv2coll

import csv
import glob
import os

#get the current directory
currentdir = os.getcwd();
os.chdir(currentdir)

#find all of the .csv files in directory
for files in glob.glob("*.csv"):
	index = 0;
	#print files
	
	#seperate file extension from filename
	Filename, fileExtension = os.path.splitext(files)
	#print Filename

	outputfile = Filename + ".txt" #the desired name of the output file
	blankcellreplace = "N/A" #what string you want to replace blank cells with

	#calculate number of columns in .csv file
	columnstemp = csv.reader(open(files, "rU"), dialect=csv.excel)
	columns = len(zip(*columnstemp))
	#print columns

	#read inputfile into array/index
	infile = csv.reader(open(files, "rU"), quoting=csv.QUOTE_NONE, dialect=csv.excel)
	lines = [[0] + l for l in infile] #read the csv file into an array and create column for index value

	for i in lines:
		for n in range(0, columns): #fill blank cells with blank cell replace string
			if lines[index][n] == '': #find blank cells
				lines[index][n] = blankcellreplace #replace blank cells
		lines[index][columns] += ";" #adds semicolon to end of each line				
		lines[index][0] = index #fill with index value
		strindex = str(lines[index][0]) + "," #holds index as string, adds comma to end of each index as string
		lines[index][0] = strindex #put the index strings back in the array
		index +=1
	#manually set the first line to ;
	lines[0] = ";"
	#print lines[0]
	
#write text file with converted data
	with open(outputfile, mode="w") as outfile:
    		writer = csv.writer(outfile, delimiter=' ')
    		writer.writerows(lines)