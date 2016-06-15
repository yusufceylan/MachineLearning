
# Cross-Validation
# k-fold cross validation -> kcv
# Takes a list and number as input -> returns a list as output

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def kcv(data,k):
	for a in range(0,k):
		training = []
		test = []
		for element in data:
			if element % k == a:
				test.append(element)
			else:
				training.append(element)
		yield training,test

result = list(kcv(data,3))

# Visualiaton of k-fold cross validation

print ("Training Set - Test Set")
for i in result:
	print (i[0],i[1])

print("------------------------")

# Leave-one-out cross-validation -> lcv
# Takes a list and number as input -> returns a list as output

def lcv(data):
	for a in range(0,len(data)):
		training = []
		test = []
		for element in data:
			if element == a:
				test.append(element)
			else:
				training.append(element)
		yield training,test

result2 = list(lcv(data))

print ("Training Set - Test Set")
for i in result2:
	print (i[0],i[1])
