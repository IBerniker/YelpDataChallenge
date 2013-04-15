import json

DATA_DIR = 'e:\\data\\'

def makeDataIntoValidJsonArray(file):
	fnameParts = file.split('.')
	inputFileName = DATA_DIR+file
	outputFileName = DATA_DIR+fnameParts[0] +'-cleaned.' + fnameParts[1]
	print("Cleaning: " + inputFileName)
	print("Output: " + outputFileName)
	with open(inputFileName) as f:
		with open(outputFileName, 'w') as out:
			out.write('[\n')
			prev = f.readline()
			curr = f.readline()
			if prev and not curr.strip():
				out.write(prev+"]")
			while prev.strip():
				if curr.strip():
					out.write("\t" + prev.replace("\n",",\n"))
				else:
					out.write("\t" + prev)
				prev = curr
				curr = f.readline()
			out.write("]")
	print("Complete.")


def loadData():
	with open(DATA_DIR+'yelp_academic_dataset_checkin-cleaned.json') as f:
		checkins = json.loads(f.read())

	with open(DATA_DIR + 'yelp_academic_dataset-')