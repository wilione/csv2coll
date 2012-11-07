#csv2coll by Andrew Willingham
#updated 11/7/2012
#www.wilhelmsound.com
#http://github.com/wilione/csv2coll

import csv

index = 0;
inputfile = "INPUT FILENAME.csv" #the name of the .csv file you want to convert
outputfile = "OUTPUT FILENAME.txt" #the desired name of the output file
blankcellreplace = "BLANK REPLACE CHARACTER" #what string you want to replace blank cells with

#calculate number of columns in .csv file
columnstemp = csv.reader(open(inputfile, "rU"), dialect=csv.excel)
columns = len(zip(*columnstemp))

#read inputfile into array/index
infile = csv.reader(open(inputfile, "rU"), dialect=csv.excel)
lines = [[0] + l for l in infile] #read the csv file into an array and create column for index value

for i in lines:
	for n in range(0, columns): #fill blank cells with black cell replace string
		if lines[index][n] == '': #find blank cells
			lines[index][n] = blankcellreplace #replace blank cells
	lines[index][columns] += ";" #adds semicolon to end of each line				
	lines[index][0] = index #fill with index value
	strindex = str(lines[index][0]) + "," #holds index as string, adds comma to end of each index as string
	lines[index][0] = strindex #put the index strings back in the array
	index +=1
	
#write text file with converted data
with open(outputfile, mode="w") as outfile:
        writer = csv.writer(outfile, delimiter=' ')
        writer.writerows(lines)