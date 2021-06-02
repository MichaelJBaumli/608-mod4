#Program Name: 608-mod4.py
#Assignment Module 4
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210601

c = [1,3,45,6,3,78,4,7,4]
print("This is a list named 'c'")
print(c)
print("This is the fifth element of c, numbered c[4]: ")
print(c[4])
print("The length of list c is : ", len(c))
print("The value of c[-1] is:" ,c[-1])
print("This is what happens when I ask for a value longer the list: ")
print("IndexError: list indiex is out of range")
print("These are the first three elements added: ", c[0]+c[2]+c[1])
c+=[1]
print("This code appending items c+=[1]:", c)
a = [1,2,3]
b = [4,5,6]
d = a + b
print("List a = [1,2,3] and list b = [4,5,6]: ", d)
print("The following is a list iterated:")
for i in range(len(c)):
    print (f'This is item {i+1} of the list c: {c[i]}')
print("a <= c:", a<=c)
print("a <= b:", a<=b)
print("b <= c:", b<=c)
print("creating a tuple: student_tuple = () ")
student_tuple = ()
print("Addint to the tuple: student_tuple = ('John', 'Green', 3.3)")
student_tuple = ("John", "Green", 3.3)
print("student_tuple = ", student_tuple)
print('tuple1 = (10,20) and tuple2 = (30,40)')
tuple1 =(10,20)
tuple2 =(30,40)
tuple1+=tuple2
print("Appending a tuple to another, tuple1+=tuple2)",tuple1)
print("The first item of student_tuple is: ",student_tuple[0])




