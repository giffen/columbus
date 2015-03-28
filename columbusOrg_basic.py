
import os, csv, re

def info():
	p = raw_input("Please enter the file path: ")
	p = p.strip('"')
	path = r'%s'%(p)
	rows = raw_input("\nHow many rows would you like to include in your analysis? ")
	search = raw_input("\nWhat population number would you like to use to make a summary file? ")
	os.chdir(path)
	return path,rows,search

def columbus(path,search):
	filelist = []
	for (dirpath, dirnames, filenames) in os.walk(path):
		pattern = r'([\d\.[csv]])'
		pop = '[' + search + ']'
		for f in  filenames:
			if pop in f and 'Population' in f:
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

def prismFile(files, header,rows):
	container = []
	max_count = []
	pad_container = []
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
			data.append(content)
			count += 1
		max_count.append(count)
	if rows.upper() == 'MAX':
		for l in container:
			new_l = l + ['NA'] * (max(max_count) - len(l))
			pad_container.append(new_l)
		return pad_container
	elif rows.upper() == 'MIN':
		return container
	
	else:
		rows = int(rows)
		if min(max_count) < rows:
			for l in container:
				new_l = l + ['NA'] * (rows - min(max_count))				
				pad_container.append(new_l)		
		else:
			for l in container:
				new_l = l[:rows+1]
				pad_container.append(new_l)
		return pad_container	

def write_csv(data):
	with open('summary_file.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(data)
	print ("\nFinished making a summary file! Check your folder for summary_file.csv")
										
def main():
	path, rows, search = info()
	files = columbus(path,search)
	header = headers(files)
	summary_file = prismFile(files, header, rows)
	write_csv (zip(*summary_file))

if __name__ == '__main__':
	main()
