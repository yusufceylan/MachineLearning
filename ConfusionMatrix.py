__author__ = 'Yusuf'

# Our data

data = {
'Dog': ['Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Cat', 'Rabbit', 'Cat'],
'Rabbit': ['Dog', 'Cat', 'Dog', 'Rabbit', 'Cat', 'Rabbit', 'Cat', 'Rabbit', 'Rabbit', 'Rabbit'],
'Cat': ['Rabbit', 'Dog', 'Cat', 'Cat', 'Rabbit', 'Dog', 'Cat', 'Cat', 'Dog', 'Cat']
}


# Helper function to get key by using value
# Takes a dict and value as input -> returns key of given value
# Purpose -> Getting key of given value

def get_Value(dic,value):
    for key in dic:
        if dic[key] == value:
            return key

print("------- CONFUSION MATRIX --------")

# ConfusionMatrix Function
# Takes a dict data as input -> returns dict as output
# Purpose -> Shows correct or wrong categorized elements

def ConfusionMatrix(data):
    son = {}
    for datavalue in data.values():
        son[get_Value(data,datavalue)] = {}
        for key in data.keys():
            son[get_Value(data,datavalue)][key] = datavalue.count(key)
    return son

print(ConfusionMatrix(data))

print("------- ACCURANCY OF CONFUSION MATRIX--------")

# Accuracy Function
# Takes a dict data as input -> returns a number as a output
# Purpose -> Giving Accuracy of given data

def acc(data):
    totalpredict = 0
    for i in data.values():
        totalpredict += len(i)

    totalcorrect = 0
    for key,value in data.items():
        for i in range(len(data[key])):
            if key == value[i]:
                totalcorrect +=1

    acc = totalcorrect / totalpredict
    acc = float(acc)
    return acc

print(acc(data))