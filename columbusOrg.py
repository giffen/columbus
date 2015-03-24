
import os, csv, re

path= raw_input("Please enter the file path: ")
if ' ' in path:
	print "\nPlease remove any whitespaces from folder and filenames "
	exit()

os.chdir(str(path))

rows = int(raw_input("\nHow many rows would you like to include in your analysis? "))

mk_graph = raw_input("\nWould you like to make a graph? (Y/N) ")


def columbus():
	filelist = []
	for (dirpath, dirnames, filenames) in os.walk(path):
		for f in  filenames:
			if 'Selected' not in f and 'Population' in f:
				filelist.append(f)
	return filelist

def headers(filelist):
	header = []
	for f in filelist:
		pattern = r'(\.\w\d+)'
	 	h = re.search(pattern,f)
	 	if h:
	 		header += [h.group()]
	header = [s.replace('.','') for s in header]
	return header

def prismFile(files, header):
	container = []
	headcount = 0
	for f in files:
		count = 0
		csvfile = open(f, 'r')				
		reader = csvfile.readlines()[1:]
		data = []
		container.append(data)	
		data.append(header[headcount])	
		headcount += 1			
		for line in reader:
			array = line.split(',')
			content = array[8]			
			if count < rows + 1:				
				data.append(content)
				count += 1
	return container

def write_csv(data):
	with open('summary_file.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(data)
	print ("\n\nFinished making a summary file! Check your folder for summary_file.csv")

def graph_summary():
	print ("\n\nMaking graph...")
	import os, pandas as pd, matplotlib.pyplot as plt
	df = pd.read_csv('summary_file.csv')
	p = df.plot(kind='box')
	p.set_ylim(100,15000)
	plt.show()
											
def main():
	files = columbus()
	header = headers(files)
	summary_file = prismFile(files, header)
	write_csv (zip(*summary_file))
	if mk_graph.upper() == 'Y':
		graph_summary()	

main()