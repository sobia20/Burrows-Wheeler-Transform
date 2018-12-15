#!/usr/bin/python
def BurrowsWheelerTransformer(text):	
	arr = []
	i = 0
	while i<len(text):
	     arr.append(text[len(text)-1]+text[:len(text)-1])
	     text = arr[i]
	     i = i+1
	arr = sorted(arr)
	bwt = ''
	b=''
	for j in arr:
		small = j[len(j)-1:]
		bwt = bwt+small
	print (bwt)
	return bwt

if __name__ == '__main__':
	# text = input()
	text = 'TAG$CT'
	BurrowsWheelerTransformer(text)

