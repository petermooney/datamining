import csv

def readCSVFile(filename):

	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			print ', '.join(row)
			
			
def main():
	readCSVFile("unesco.csv")
	
	
main()
