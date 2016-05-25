#!/usr/bin/python
​
import sys
​
keywords = ['collaboration', 'mobile', 'forge', 'cloud']
​
if len(sys.argv) != 3:
	print("Usage: searchwords [input-file] [output-file]")
	sys.exit(1)
​
in_filename = sys.argv[1];
out_filename = sys.argv[2];
​
in_file = open(in_filename,'r+')
wordcount={}
​
for keyword in (keywords):
	wordcount[keyword] = 0
​
for word in in_file.read().split():
​
	word = word.lower()
	isKeyword = False
​
	for cand_key in (keywords):
		if cand_key == word:
			isKeyword = True
	
	if isKeyword:
		wordcount[word] += 1
​
in_file.close()
out_file = open(out_filename, 'w')
​
for k,v in wordcount.items():
	out_file.write(k)
	out_file.write(' ')
	out_file.write(str(v))
	out_file.write('\r\n')
	
out_file.close()
