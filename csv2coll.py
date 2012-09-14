import csv

index = 0;
datalist = []
inputfile = "INPUT FILE NAME.csv" #the name of the .csv file you want to convert
outputfile = "OUTPUT FILE NAME.txt" #the desired name of the output file

infile = csv.reader(open(inputfile, "rU"), dialect=csv.excel)
lines = [[0] + l for l in infile] #read the csv file into an array and create column for index value

for i in lines:
	lines[index][5] += ";" #adds semicolon to end of each line				
	lines[index][0] = index #fill with index value
	strindex = str(lines[index][0]) + "," # ar holds index as string, adds comma to end of each index as string
	lines[index][0] = strindex #put the index strings back in the array
	index +=1
	
with open(outputfile, mode="w") as outfile:
        writer = csv.writer(outfile, delimiter=' ')
        writer.writerows(lines)	