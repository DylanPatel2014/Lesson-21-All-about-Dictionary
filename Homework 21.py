dictionary = {'Strawberry' : 7, 'Dylan' : 4, 'Homework' : 2, 'Codingal' : 3, 'Sadeya' : 6}
print("The original dictionary : " +  str(dictionary))
t = 2
res = 0
for i in dictionary:
    if dictionary[i] == t:
        res = res + 1
print("Frequency of t is : " + str(res))