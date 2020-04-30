
print("Hello")

### read data

##f=open("abc.txt","r")
##
####x=f.readline()
##x=f.read(6)
##
##print("Data stored in file")
##print(x)
##
##f.close()



### write multiple data
##f= open("guru99.txt","w+")
##
##
##for i in range(10):
##     f.write("This is line %d\r\n" % (i+1))
##
##
##
##f.close()



###  append data
##f=open("abc.txt","a")
##

##f.write("HELLO@")
##f.write("BYE")
##f.write("Siya")
##
####print("Data stored in file")
####print(x)
##
##f.close()


##### append or write data by taking input
##f=open("abc.txt","a")
##
##name=input("Enter the name")
##mon=input("Enter the mob")
##data=name+":"+mon
##
##f.write(data)
##
##
##f.close()


##f=open("abc.txt","r")
##
##x=f.read()
##
##print("Data stored is")
##print(x)


f=open("abc.txt","r+")

data=f.read()
print("Content in the file is ")
print(data)

name=input("Enter the name")
mon=input("Enter the mob")
data="\n"+name+":"+mon+"\n"
f.write(data)


f.close()






