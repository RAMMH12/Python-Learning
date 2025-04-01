file = open('sample.txt','a')
data = input('Enter Data to insert ')
file.write(data)
file.close()

file = open('sample.txt','r')
print(file.read())
file.close()