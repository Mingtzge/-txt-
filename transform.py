import sys
inputPath = str(sys.argv[1])
outputPath = str(sys.argv[2])
myfile = open(inputPath, 'r')
flags = []
bums = []
allWords = []
line1 = myfile.readline()
list1 = line1.split(',')
line2 = myfile.readline()
list2 = line2.split(',')
i=0;
for word1 in list1:
    if(word1[-1]=='\n'):
		allWords.append(word1[:-1]+':'+list2[i][:-1]+'\n')
	else:
		allWords.append(word1+':'+list2[i]+'\n')
	i=1+i
myfile.close()
myfile = open(outputPath, 'w')
myfile.writelines(allWords)
myfile.close()
print ("successed!")
