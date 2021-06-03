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
student_tuple = ()
print("student_tuple = ('Amanda', [98,85,87])")
student_tuple = ('Amanda',[98,85,87])
print("The first item of student_tuple is: ",student_tuple[0])

first_name, grades = student_tuple
print("first name is ", first_name)
print("grades are ", grades)
"""Displaying a Bar Chart"""
numbers = [19,3,15,7,11]

print('\nCreating a bar charg from numbers:')
print(f'Index{"Value":>8}    Bar')

for index,value in enumerate(numbers):
    print(f'{index:>5}{value:>8}    {"*" * value}')

print("numbers = list(range(1,16))")
numbers = list(range(1,16))
print("numbers = ", numbers)

print("numbers[1:len(numbers):2]")
numbers[1:len(numbers):2]
print("numbers after slice: ",numbers)

print("numbers[5:10] = [0] * len (numbers[5:10])")
numbers[5:10] = [0] *len(numbers[5:10])
print("numbers",numbers)

print("numbers[5:] = []")
numbers[5:] = []
print("numbers =",numbers)

print("numbers[:] = []")
numbers[:] = []
print("numbers = ",numbers)

print("numbers = list(range(0,10))")
numbers=list(range(0,10))

print("numbers = ",numbers)

print("del numbers[-1]")
del numbers[-1]

print("numbers = ",numbers)

print("del numbers[0:2]")
del numbers[0:2]
print("numbers = ", numbers)

print("passing a list to a function")
def modify_elements(items):
    for i in range(len(items)):
        items[i] *=2
numbers = [10,3,7,1,9]
print("numbers before modify_elements", numbers)
modify_elements(numbers)
print("Numbers after modify_elements", numbers)

numbers = [10,3,7,1,9,4,2,8,5,6]
print("numbers unsorted: ",numbers)
numbers.sort()
print("numbers sorted:",numbers)
numbers.sort(reverse=True)
print("numbers reverse sorted: ",numbers)
numbers = [10,3,7,1,9,4,2,8,5,6]
print("numbers back to original: ",numbers)
print("numbers using sorted()", sorted(numbers))
print("numbers after sorted",numbers)

print("foods = ['Cookies', 'pizza', 'Grapes', 'apples','steak','Bacon']")
foods = ['Cookies','pizza','Grapes','apples','steak','Bacon']

print("foods.sort()")
foods.sort()
print("foods sorted: ",foods)

print('numbers = [3,7,1,9,4,2,8,5,6]')
numbers = [3,7,1,9,4,2,8,5,6]
print("numbers = ",numbers)
print('numbers index of 5 is ',numbers.index(5))

print("1000  in numbers?",1000 in numbers)
print("5 in numbers? ",5 in numbers )
print("All the values in this list is positve any(numbers)<0: ", any(numbers)>0)
print("There are no negative values in the list all(numbers),0: ",all(numbers)>0)

print("list2 = [item for item in range(1,600)]")
list2 = [item for item in range(1,600)]
print("list2 =", list2)









