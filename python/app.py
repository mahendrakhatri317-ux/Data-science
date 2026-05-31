# print("hello hiii kese ho 😂😂")

#>>>>>>>>>>>>>>>>>>>>>>>>>>> variables 😎


# variable :- Variable ek container ki tarah hota hai jo value ko store karta hai.


# name = "Mahendra"
# _name = "montu"
# print(_name)       # output => montu

# last5515151name = ""     ### 👉 aise variablr declare nhi kar sakte 😥
# 5 = 10 



# age = 10                  ### 👉 upper case lower case ka farak padta hai 😉
# Age = 20 
# AGE = 30 
# print(age)  #output => 10
# print(Age)  #output => 20
# print(AGE)  #output => 30



# @ = 10                  ### 👉aise bhi variable declare nhi kar sakte 😒
# $ = 10 
# % = 20 
# ^ = 10 
# & = 0 

########## 

 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Data Types


#  Data Types :- Data type batata hai ki variable me kis type ka data store hai.


# Category	           Examples
# Numeric Type	       int, float, complex
# Sequence Type	       list, tuple, range, str
# Mapping Type	       dict
# Set Type	           set, frozenset
# Boolean Type	       bool


# a = 10
# print(a)  # output => 10


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 👏string datatype in python

# string :- In Python, String ek data type hoti hai jo text ya characters ko store karti hai.
#Simple language me: Letters, words, sentences ya symbols ko string kehte hain.

name = "upflairs"
print("This is my first string :- ",name)    #output => This is my first string :-  upflairs
print("type of my first string :- ",type(name))  # output => This is my first string :-  <class 'str'>
  ## type function data type btata hai 


# num ="2345"
# print(num)
# print("type of my first string :- ",type(num))




name = "Mahendra"
print("len of my first string👉👉",len(name)) ### find the length of the string 

# # #✌ indexing & slicing 

print(name[0])
print(name[2])
print(name[4])
print(name[5])
print(name[1])

print("Slicing :- ",name[0:4])     ### kaha se kaha tak string ko print karvnana hai uske lia slicing ka use hota hai
 

# print(name[-1])                     ### string ko piche se print karne ke lia negative use karte hai 

###### task 1 💋
# print(name[: : -1])      #“[::-1] is used to reverse a string using slicing in Python.”

# name = "Ritik"
# print(len(name))                     ### find the length of string 


# ------>>>>>>>lower case convert into upper case 👉👉👉
# comapny_name= "upflairs pvt ldt"
# upper_case =comapny_name.upper()      ### '.upper' ka use string ko upper case me karne ke lia hota hai
# print("upper case 🔫🔫🔫🔫",upper_case)

#------->>>>>>>> upper case convert into lower case

# comapny_name="UPFLAIRS PVT LDT"     ### '.upper' ka use string ko lower case me karne ke lia hota hai      
# lower_Case =comapny_name.lower()

# print("lower case 👉",lower_Case)
 

# ##### task2 💖
# lower_case =comapny_name.casefold()   ## casefold() string ke sabhi uppercase letters ko lowercase me badal deta hai.
# print(lower_case)                     ## Ye lower() jaisa hi hota hai, lekin aur zyada powerful hota hai Unicode text ke liye.

###  NOTE 👉👉 difference between lower_case and casefold :: =>
# 1. lower() :: Sirf normal uppercase letters ko lowercase me convert karta hai. 
# 2. casefold() :: Ye bhi lowercase karta hai, lekin special Unicode characters ko bhi properly handle karta hai.


# company_name = "upflairs pvt ldt"    ### .title() ka use string ke har word ka first letter capital karne ke liye hota hai.
# first_latter=company_name.title()    
# print(first_latter)

# first_latter=company_name.capitalize()   ### .capitalize() ka use string ke sirf first character ko capital karne ke liye hota hai.
# print("👉👉👉👉",first_latter)

# name="mahendra"
# c =name.count('a')  ### .count() ka use kisi string me kisi character ya word kitni baar aaya hai ye count karne ke liye hota hai
# print(c)


# print(name.index('a'))   ## .index() ka use string me kisi character ya word ki position (index number) find karne ke liye hota hai.



# name = "ritrrik"          ## do string ko add karne ke lia dono string ke bick ' + ' ka use karte hai ( withoout space)
# last_name = "Kumar"
# print(name + last_name)


# print("🥹🥹🥹",name,last_name)   ### do string ko add karne ke lia dono string ke bick ' , ' ka use karte hai ( with space) 


# print("😂😂😂",name +" "+ last_name )    ## ek tarika ye bhi hai do string ko add karne ke lia ( with space)



# name = "Diya "      ### string ko no. se multiply kar sakte hai
# print(name*10)




# intro = """Hello everyone,    
# My name is Ritik Kumawat, and I am a developer and Data Science Engineer from Jaipur, Rajasthan. I specialize in Python, Machine Learning, Deep Learning, FastAPI, Flask, and Generative AI. I also work with cloud technologies like AWS and databases such as MySQL and MongoDB.

# Currently, I work as a trainer and developer where I help students learn modern technologies and build real-world projects. I am passionate about teaching, coding, and creating innovative AI applications.

# I believe in continuous learning, practical knowledge, and maintaining good communication while working on projects. Thank you.
# """
# print(intro)                              ## paragraph me multiple line ko print karvane ke lia ( """   .   """) ka use karte hai



# name = "Govind"      ### add string   
# address = "jaipur rajasthan "
# print(f"my name is {name} and i am from {address} ")



# path = r"C:\Program Files (x86)\Microsoft Office\Office16"    
# print(path)            ### path ko print karne ke lia ' r' ka usr karte hai



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..list ✔

# list :- Python me List ek data type hai jo ek saath multiple values store karti hai.
#Simple language me: “List ek collection hoti hai jisme bahut sari values ek variable me store hoti hain.”

# heterogeneous :- Python me agar ek list me alag-alag data types hain, to usse heterogeneous collection bolte hain.


# lst = [1,2,5,2,5,1, "hello", 3.4 , "😍😍😍😍"]

# print("This is my first list :- ",lst)
# print("Type of my list :-  ",type(lst))   ## list ka type batane ke lia ' type ' ka use hota hai
# print("len of my list :- ",len(lst))      ## find the length of list


#---------------->>>>>>>>>>>>>>>>>indexing and Slicing


# list = [1,2,2,5,5]
# print(list)

# lst = [1,2,5,2,5,1, "hello", 3.4 , "😍😍😍😍"]   ##find indexing in list
# print(lst[0])
# print(lst[2])
# print(lst[5])
# print(lst[3])



# print(lst[0:3])       ## find slicing in list
# print(lst[2:4])
# print(lst[5:8])
# print(lst[1:3])


# name ="Ritik"       
# print("f" in name)


# lst = [1,2,5,2,5,1, "hello", 3.4 , "😍😍😍😍"]
# lst.append("upflairs")         ## append() function list ke end me ek new item add karta hai.
# lst.insert(1, "upflairs")    ## insert() function list me kisi bhi specific position par value add karta hai
# print(lst)       




# lst.remove(3.4)                  ## remove() list me se kisi specific value ko delete karta hai.
# lst.pop(2)                       ## pop() list se element ko remove karta hai aur us removed value ko return bhi karta hai.
# lst.extend([1,0])                ## extend() ek list me dusri list ke multiple elements add karta hai.
# lst.count(5)                     ## count() list me kisi value kitni baar aayi hai usko count karta hai.
# lst.clear()                      ## clear() list ke saare elements ko remove kar deta hai
# lst.copy()                       ## copy() list ki duplicate copy banata hai.

# print(lst)


# lst1 = [1,2,2,54]               ## arithmetic operations in iist 
# lst2 = [8,2,5,5]
# print(lst1+lst2)
# print(lst1*lst2)
# print(lst1/lst2)
# print(lst1//lst2)

# lst = ["hello", 2,4,54,5]
# max()      # largest value
# min()      # smallest value
# sum()      # total addition
# len()      # length/count


# lst = [1,2,2,4,2,2]
# lst.sort()                  ## sort() list ke elements ko ascending ya descending order me arrange karta hai.
# # lst.reverse()             ## reverse() list ke elements ka order ulta kar deta hai.
# print(lst)
# lst[0]="hello"              ## 1 ki jagah hello aa jayega
# print(4 in lst)
# print(lst)




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.Tuple 👉

# tuple ✨ : “A tuple is an ordered and immutable collection of elements in Python.”

tpl =(1,2,3,45,"hello", 2.2, 1,2)
# print("This is my first tuple :- ",tpl)     #output = this is my first tuple :-  (1, 2, 3, 45, 'hello', 2.2, 1, 2)
# print("len of my tuple  :-",len(tpl))       #output = len of my tuple  :- 8



# #--------->>>>>>>>>>>>> indexing and slicing
#>>>>>>>>>> indexing
# print(tpl[0]) #output = 1
# print(tpl[4]) #output = hello 
# print(tpl[2]) #output = 3
# print(tpl[7]) #output= 2

#>>>>>>>>> slicing 
# print(tpl[0:4])
# print(tpl[2:5])
# print(tpl[1:7])
# print(tpl[::-1])
# print(tpl[4:-1])

#========================>>>>>>>>> type casting 
# a = 1,23,5,4,5, "hello"
# print(a)                                    #output = (1, 23, 5, 4, 5, 'hello')
# print(type(a))                              #output = <class 'tuple'>
# print(len(a))                               #output = 6


# tpl = (1,2,3,"hii",5,4)
# print("ye mera tpl :-",tpl)                   #output = ye mera tpl :- (1, 2, 3, 'hii', 5, 4)
# print("Type of my tuple :- ",type(tpl))       #output = Type of my tuple :-  <class 'tuple'>

#### ======================>>>>>>>tuple unpacking 

# uple unpacking  = Tuple unpacking ka matlab hai tuple ki values ko alag-alag variables me store karna.

# a, b,c =(1,2,3)
# print(a)                                    #output = 1
# print(b)                                    #output = 2
# print(c)                                    #output = 3



# a,b,c =(1,2,3)
# print(a)                                    #output = 1               
# print(b)                                    #output = 2

# =============================>>>>>>>>>>>>> index and count 

# tpl = (1,2,3,"hello",5.5,5)
# print(tpl)                                    #output = (1,2,3,"hello", 5.5, 5)
# print(tpl.count(1))                           #output = 1
# print(tpl.index(2))                           #output = 1


#==============================>>>>>>>> tuple convert into list 🎉


# print("tpl convert into list")
# lst =list(tpl)
# print(">>>>",lst)                              #output = tpl convert into list  >>>> [1, 2, 3, 'hii', 5, 4]

# print(">>>>",type(lst))                        #output = >>>> <class 'list'>
# lst.append(100)
# print(lst)                                       #output = tpl convert into list  >>>>>   [1, 2, 3, 'hii', 5, 4, 100]
# tpl=tuple(lst) 
# print( "list convert into tuple " ,tpl)           #output = list convert into tuple  (1, 2, 3, 'hii', 5, 4)




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. dict 🤦‍♂️
# dict :- “A dictionary is a mutable collection that stores data in key-value pairs.”

# student = {"name":"Ritik",
#            "class":"Second year",
#            "Roll_number":21,
#            "branch": "CSE",
#            "Address":"jaipur"}

# name , class , Roll_number , branch , address >>>>>>>>> keys 
# Ritik second year 21 cse jaipur >>>>>> values 
# key + value = "Item "


# print(student)

# print("dict keys ",student.keys())            # only print keys
# print("dict values ",student.values())        # only print values
# print("dict items ",student.items())         # print complete items


# print(student['name'])                       # only print name   output = ritik
# print(student['class'])                      # only print class  output = second year
# print(student['branch'])                     # only print branch  output = CSE




#===========================>>>>>>>>>>>>>>>>>>> add item in python dict

# student['subject']='python'

# print(student)



#### task 1  update function , fromkeys 

# student = {
#     'name': 'Mahendra',
#     'class': 'BTech',
#     'branch': 'CSE'
# }

# print(student['name'])
# print(student['class'])
# print(student['branch'])

######## update function 

# student.update({'class': '3rd Year'})
# student.update({'college': 'BTU'})

# print(">>>>" ,student)

######### from keys

# keys = ['name', 'class', 'branch']

# new_student = dict.fromkeys(keys, 'new')
# print(">>>>>>>>>",new_student)



# print(student.get('name'))
# student.clear()
# student.copy("class")
# student.pop()
# student.popitem()


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("color", "white")

# print(x)

##### iteration & update value

# car = {
#   "brand": ["Ford","Honda", "hero"],
#   "model": "Mustang",
#   "year": 1964
# }
# print(car)
# for x in car.items():
#     print(x)
    
# print(car)
# car['year']=200
# print(car)


# Deep copy task 2 

# car = {
#   "brand": ["Ford","Honda", "hero"],
#   "model": "Mustang",
#   "year": 1964
# }







   


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Set 

#set = “A set is an unordered collection of unique elements in Python.”

# sat = {1,2,3,5}
# print("This is my first set:- ",sat)
# print("Type of my  set:- ",type(sat))
# print("len of my  set:- ",len(sat))

# sat = {1,2, "hello",3,5,1,2}
# print(set)   ## set me duplicate value ko store nhi kar sakte hai
# sat.remove("hello")
# sat.discard("1")
# print(sat)



# # >>>>>>>>>>> operatore 
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y) 






































































































































































