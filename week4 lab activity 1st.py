#Function1.py
#
#@author:A.N. Other
#date:September2016

def show_hello():
    print("Hello there, this is my very first function!!!\n\n")

print("Testing my first user defined function...\n\n")



show_hello()



show_hello()




#Function2.py
#
#@author:A,N.Other
#date:September2016

def show_hello(param):
    print("Hello there, the numbers of lines"
        "function is called is{0}!!!\n\n".format(param))


#creating and setting a counter
counter =0
print("Testing my second user defined function...\n\n")


counter +=1
#invoking the function
show_hello(counter)


counter +=1
#invoking the function again
show_hello(counter)