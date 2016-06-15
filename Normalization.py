import random
import math

# generate_random Function
# Takes three integer as input -> returns list of tuples
# Purpose -> Generate random tuple list
# Parameters
    # start -> Min value of element of tuple
    # end -> Max value of element of tuple
    # number -> number of tuples
# Example
# generate_random(1,5,5) -> [(3, 3), (5, 5), (5, 4), (2, 2), (5, 1)]

def generate_random(start,end,number):
        random_list = []
        for i in range(number):
                x = random.randint(start,end)
                random_list.append(x)
        return random_list

a = generate_random(1,5,5)
print (a)

data = [416, 388, 186, 273, 164, 426, 444, 232, 304, 
434, 184, 442, 337, 285, 430, 488, 409, 284, 399, 410, 
331, 438, 173, 343, 496, 345, 252, 222, 391, 134, 405, 
365, 174, 428, 420, 223, 202, 481, 303, 202, 301, 134, 
163, 163, 125, 111, 247, 276, 302, 125]



# rescaling Function
# Takes list of numbers as input -> return list of numbers
# Purpose -> Apply rescaling method of Normalization 

def rescaling(lon):
	rescaling_list = []
	for i in lon:
		rescal = float(i - min(lon)) / float(max(lon) - min(lon))
		rescaling_list.append(float(rescal))
	return rescaling_list

print (rescaling(data))

# find_mean Function
# takes list of numbers as input -> returns number 
# Purpose -> finding mean of the list

def find_mean(lon):
	result = sum(lon) / float(len(lon))
	return result

# find_std Function
# takes list of numbers as input -> returns number 
# Purpose -> finding standard deviation of the list

def find_std(lon):
	toplam = 0
	for i in lon:
		toplam += (i-find_mean(lon))**2
		result = math.sqrt(toplam / len(lon))
	return result
		
# standardization Function
# Takes list of numbers as input -> return list of numbers
# Purpose -> Apply standardization method of Normalization 

def standardization(lon):
	standardization_list = []
	for i in lon:
		item = float(i - find_mean(lon)) / find_std(lon)
		standardization_list.append(item)
	return standardization_list

print (standardization(data))
