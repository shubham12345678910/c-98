def swapFileData():

    file1 = input("enter the oruginal file: ")
    file2 = input("enter the file to be swapped")
    with open(file1,'r') as a:
       data_a = a.read()
    with open (file2,'r') as b:
      data_b = b.read()

    with open(file1,'W+') as a :
         a.write(data_b)

    with open (file2,'W+') as b:
        b.write(data_a)

    swapFileData( )