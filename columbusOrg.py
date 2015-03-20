
import os, csv

path= raw_input("Please enter the file path: ")
os.chdir(str(path))

rows = int(raw_input("\n\nHow many rows would you like to include in your analysis?"))

mk_graph = raw_input("\n\nWould you like to make a graph? (Y/N) ")


def columbus():
	filelist = []
	#num = 1000
	for (dirpath, dirnames, filenames) in os.walk(path):
		for f in  filenames:
			if 'Selected' not in f and 'Population' in f:
				filelist.append(f)
	return filelist

def prismFile(files):
	container = []
	for f in files:
		csvfile = open(f, 'r')
		reader = csvfile.readlines()
		data = []
		container.append(data)
		count = 0
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
	print "\n\nFinished making a summary file! Check your folder for summary_file.csv"

def graph_summary():
	print "\n\nMaking graph..."
	import os, pandas as pd, matplotlib.pyplot as plt
	df = pd.read_csv('summary_file.csv')
	p = df.plot(kind='box')
	p.set_ylim(100,5000)
	plt.show()
											
def main():
	files = columbus()
	summary_file = prismFile(files)
	write_csv (zip(*summary_file))
	if mk_graph.upper() == 'Y':
		graph_summary()	

main()