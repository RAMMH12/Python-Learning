try:
    #1st way of Reading file
    file = open('sample.txt','w')
    file.write('Line 1 :This is sample Text file \nLine 2: it contain multiple line')
    #read1 = file.read()
    file.close()

    file = open('sample.txt','r')
    filedata = file.read()
    print(filedata)
except FileNotFoundError:
    print('Error : The File "sample.txt" was not found')
