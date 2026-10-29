dictionary = {'Codingal':3,'is' :2,'best':2,'for':2,'Coding':6,'and':1,'for':4,'Sadeya':10}
print("The original dictionary : " +  str(dictionary))
j = 10
answer = 0
for i in dictionary:
    if dictionary[i] == j:
        answer = answer + 1
print("Frequency of j is : " + str(answer))