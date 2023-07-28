#Day2 ControlFlow in Python 
#We are gonna look at (if-elif-else) in this Section

"""
age = 90

if age >= 18:
    print("You are qualified to vote")
elif age >=18 and age <= 65:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
"""

################################################################
    #for Loop
    
   
"""items = [1,2,3,4,5,6,7,8,9,10,11]
for item in items:
   print(item)
"""

################################################################
    #while Loop
    

# omo = 0
# while omo < 6:
#     print("My Name is OGKI MOSES ODERA")
#     omo = omo + 1



################################################################
#Break and continue statements

#Break Statement

# for num in range(1,10):
#     if num == 5:
#         break
#     print(num)

#Continue Statement
# for num in range(1,10):
#     if num == 55:
#         continue
#     print(num)


################################################################

# try:
#     item = [1,2,3]
#     print(item[6])
    

# except IndexError:
#     print("Index Error")
# except TypeError:
#     print("String")
# finally:
#     print("Finally")

# try:
    
#     x = 10 / 0
# except ValueError:
   
#     print("ValueError occurred")
# except ZeroDivisionError:
    
#     print("ZeroDivisionError occurred")
# except Exception as e:
    
#     print("An exception occurred:", str(e))
# finally:
#     print("Always returning")

#1_EXERCISE

health = {
    1: "Am very Healthy",
    2: "Am very Sick",
    3: "Am very tired",
    4: "Am feeling hurtful",
    5: "Am feelind deazy",
    6: "Am fairly healthy",
    7: "Am finding it hard to breath",
    8: "Am weak",
    9: "Am soon getting healthy",
    10: "Am very sick bro"
    
}

options = input("Enter how your feeling in a Scale of 1 to 10 ").lower()

if int(options) in health:
    print(health[int(options)])

else:
    print("I dont know how i feel")
