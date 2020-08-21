
# opening and reading the file
fr = input("Enter the file name ")
f = open(fr) 
test = f.read()

# defining the enrollment number list 
enno = ['170450107001',
        '170450107002',
        '170450107003',
        '170450107004',
        '170450107005',
        '170450107006',
        '170450107007',
        '170450107008',
        '170450107009',
        '170450107010']

# defining the corrosponding names to the enrollment numbers in the dictionary
thedict = {
        '170450107001' : 'student 1',
        '170450107002' : 'student 2',
        '170450107003' : 'student 3',
        '170450107004' : 'student 4',
        '170450107005' : 'student 5',
        '170450107006' : 'student 6',
        '170450107007' : 'student 7',
        '170450107008' : 'student 8',
        '170450107009' : 'student 9',
        '170450107010' : 'student 10',                       
}

# reading and separting the words from the input file 
import re
x = re.findall(r"[\w']+", test)
x = list(dict.fromkeys(x))

# making a list of the present students  
roll = []
for i in x :
  t = i.strip()
  for j in range(0,len(enno)):
    if t == enno[j] :
      temp = t
      roll.append(temp)

# printing out the present students in ascending order
pcount = 0
print("present students are :")
roll = sorted(roll)
for i in roll : 
  t=i.strip()
  print( t+ ' : ' + thedict[t] )
  pcount = pcount+1

# removing the present students from the enno list to find out the absent students
for i in roll : 
  t2=i.strip()
  enno.remove(t2)

# priting out the absent students
count = 0
print('absent students are : ')
for i in enno:
  t = i.strip()
  print( t+ ' : '+thedict[t])
  count = count+1

# printing the totle count of the present and absent students
print("\n\nTotal present student  :  " + str(pcount))
print("Total absent student  :  " + str(count))

print('\n\nDeveloped by vijay parmar')
input('Press Enter to teminate')
