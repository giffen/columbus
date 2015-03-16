
import os, csv

graph = True

def columbus():
	filelist = []
	num = 1000
	path = os.path.dirname(os.path.realpath(__file__))
	for (dirpath, dirnames, filenames) in os.walk(path):
		for f in  filenames:
			if 'Selected' not in f and 'Population' in f:
				filelist.append(f)
	return filelist, num

def prismFile(files, rows):
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
			if count < rows:
				data.append(content)
				count += 1
	return container

def write_csv(data):
	with open('summary_file.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(data)

def graph_summary():
	import os, pandas as pd, matplotlib.pyplot as plt
	df = pd.read_csv('summary_file.csv')
	p = df.plot(kind='box')
	p.set_ylim(100,5000)
	plt.show()
											
def main():
	files, num = columbus()
	summary_file = prismFile(files,num)
	write_csv (zip(*summary_file))
	if graph == True:
		graph_summary()	

main()