# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1761197
# Date: 2019/11/29

fail=0
passes=0
defer=0
print("\n~~~~~~~~~~~~~~~Welcome to student version~~~~~~~~~~~~~~~\n")
def start():
    global selection
    while True:    
        selection=input("Press 'S' to start the progarm.\nPress 'Q' to execute the program.\n")
        if selection=='s' or selection=='S':
            inputs()
        elif selection=='q' or selection=="Q":
            execute()
        else:
            print("\n~~~~~~~~~~Invalid selection~~~~~~~~~~\n")
            continue
def inputs():
    global fail,passes,defer
    try:
        passes=int(input("Enter your passed credits:"))
        checker(passes) #checker functaion has a parameter and it assign to vallue.
        fail=int(input("Enter your failed credits:"))
        checker(fail)
        defer=int(input("Enter your defer credits:"))
        checker(defer)
    except:
        print("\n~~~~~~~~~~~~~~~Invalid input,integers required~~~~~~~~~~~~~~~\n")
        inputs()
    logic()
def checker(value):#check the conditions,if pass or fail or defer not in a range and these inputs not modulus by 20,if value print range error and restart the program.
    if value>120 or value<0 or value%20!=0:
        print("\n~~~~~~~~~~~~~~~Range error~~~~~~~~~~~~~~~\n")
        inputs()
def logic():
    global fail,passes,defer
    if passes+fail+defer==120:
        if passes<=40 and fail>=80:
                    print("\n.....Your progression outcome is Excluded.....\n")
        elif passes==120:
                    print("\n.....Your progression outcome is progress.....\n")
        elif passes==100:
                    print("\n.....Your progression outcome is Do not progress Module trailer.....\n")
        elif passes<=80 and fail<=60:
                    print("\n.....Your progression outcome is Do not progress Module retriever.....\n")
    else:
        print("\n~~~~~~~~Total incorrect~~~~~~~~\n")
        restart()  

def execute():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~Your program is now executed~~~~~~~~~~~~~~")
    exit()

start() #call the function for the start the program.



