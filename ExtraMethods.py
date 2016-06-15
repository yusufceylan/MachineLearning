import random
import math
import matplotlib.pyplot as plt

data1 = [416, 388, 186, 273, 164, 426, 444, 232, 304,
434, 184, 442, 337, 285, 430, 488, 409, 284, 399, 410, 
331, 438, 173, 343, 496, 345, 252, 222, 391, 134, 405, 
365, 174, 428, 420, 223, 202, 481, 303, 202, 301, 134, 
163, 163, 125, 111, 247, 276, 302, 125]

data2 = [416, 388, 186, -273, 164, -426, -444, -232, 304, 
434, 184, -442, 337, 285, -430, -488, 409, 284, -399, -410, 
331, -438, 173, 343, -496, -345, -252, -222, -391, -134, 405, 
365, -174, 428, -420, -223, 202, -481, -303, -202, 301, 134, 
-163, -163, 125, -111, -247, 276, 302, 125]


def find_closes(data,n):
	liste = []
	for i in data:
		liste.append(abs(i-n))
	print (data[liste.index(min(liste))])

find_closes(data1,100)
find_closes(data1,290)
find_closes(data2,100)
find_closes(data2,390)

print("---------------------------")

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
                y = random.randint(start,end)
                tup = (x,y)
                random_list.append(tup)
        return random_list

a = generate_random(1,5,5)
print (a)

# find_dist Function
# Takes one two tuple as input -> returns a number
# Purpose -> Finding distance between two point
# Parameters
    # tup -> first point
    # i -> second point
# Example
# find_dist((1,2),(8,2)) -> 7

def find_dist(tup,i):
        dist = math.sqrt(pow((tup[0]-i[0]),2)+pow((tup[1]-i[1]),2))
        return dist

print (find_dist((1,2),(8,2)))

# find_nearest Function
# Takes one tuple and list of tuples as input -> Returns a tuple
# Purpose -> Finds nearest point of given tuple
# Parameters
    # tup -> tuple
    # lon -> list of tuples
# Example
# find_nearest((1,2),[(3, 3), (5, 5), (5, 4), (2, 2), (5, 1)]) -> (2,2)
# find_nearest((1,0),[(3, 3), (5, 5), (5, 4), (2, 2), (5, 1)]) -> (2,2)

def find_nearest(tup,lon):
        distance_list = []
        for i in lon:
                distance_list.append(find_dist(tup,i))
        min_dist = min(distance_list)
        return lon[distance_list.index(min_dist)]

print (find_nearest((1,2),a))
print (find_nearest((1,0),a))


# grafical_find_nearest Function
# Takes one tuple and list of tuples as input -> Returns a grafical visualization
# Purpose -> Show points in the list and point which we give as input
# Parameters
    # tup -> tuple
    # lon -> list of tuples

def grafical_find_neares(tup,lon):
    a1 = []
    a2 = []
    for i in lon:
        a1.append(i[0])
        a2.append(i[1])
    plt.plot(a1, a2,'ro',color='red')
    plt.plot(tup[0],tup[1],'ro',color='blue')
    plt.show()

grafical_find_neares((2,2),a)

