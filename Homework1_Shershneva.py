#Задание 1.

import random

#############################################################################################
def check_1(lst_obj):
    
    #Сложность: O(n).

    lst_to_set = set(lst_obj)  # O(n)
    return lst_to_set  # O(1)


#############################################################################################
def check_2(lst_obj):
    
    #Сложность: O(n`2).

    for j in range(len(lst_obj)):          # O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # O(n)
            return False                   # O(1)
    return True                            # O(1)


#############################################################################################
def check_3(lst_obj):
   
    #Сложность: O(n log n)

    lst_copy = list(lst_obj)                 # O(n)
    lst_copy.sort()                          # O(n log n)
    for i in range(len(lst_obj) - 1):        # O(n)
        if lst_copy[i] == lst_copy[i+1]:     # O(n)
            return False                     # O(1)
    return True                              # O(1)

#############################################################################################


for j in (50, 500, 1000, 5000, 10000):
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))

#Задание 2. 
#O(n)
def min_num_list(num_list):
    min_num = num_list[0]
    for i in range(len(num_list)):
        if i == len(num_list)-1:
            break

        if min_num > num_list[i+1]:
            min_num = int(num_list[i+1])
            print("min num has been changed to " + str(min_num))
        
    return min_num

num_list1 = [19,18,17,16,16,182,123,12,3,4,2412,212,238,1]
print("min number is " + str(min_num_list(num_list1)))

#O(n`2)
def as_prep(num_list):
    for i in num_list:
        is_min = True
        for j in num_list:
            if i > j:
                is_min = False
        if is_min:
            return i


num_list1 = [19,18,17,16,1,16,182,123,12,3,4,2412,212,238,2]
print(as_prep(num_list1))



#Задача 3
#вариант 1
def get_key(val):
    for key, value in dict1.items():   #O(1)
        if val == value:
            return key


dict1 = {"Makarena":25400, "Azbuka":15700, "Selebrity":36750, "Fata":17456}
val = []

for value in dict1.values(): #O(1)
    val.append(value)        #O(1)

val.sort(reverse=True)       #O(n log n)

for i in range(3):           #O(n)
    print(get_key(val[i]))

#вариант 2
dict1 = {"Makarena":25400, "Azbuka":15700, "Selebrity":36750, "Fata":17456}

val = []

def bubblesort(mass):
    for i in range(len(mass)):            #O(n)
        for j in range(0, len(mass)-i-1):  #O(n)
            if mass[j] < mass[i]:
                temp = mass[j]
                mass[j] = mass[j+1]
                mass[j+1] = temp


def get_key(val):
    for key, value in dict1.items():      #O(1)
        if val == value:
            return key

for value in dict1.values():          #O(n)
    val.append(value)                 #O(n)

bubblesort(val)
print(val)

for i in range(3):                 #o(n)
    print(get_key(val[i]))

#Считаю первый вариант более эффективным, тк с точки зрения О-большого будет работать быстрее.


#Задача 5


class Stack:
    def __init__(self):
        self.stack = []
        self.max = None
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed
    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item
    def get_max(self):
        return self.max

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.max
print(s.max)

#вариант 2

def dish_stack(size_of_stack, number_of_dishes):
    tmp_lst = []
    final_lst = []
    iter = 0
    for i in range(1, number_of_dishes+1):
        if iter != size_of_stack:
            tmp_lst.append(i)
            print(iter)
        else:
            iter = 0
            tmp = list(tmp_lst)
            final_lst.append(tmp)
            tmp_lst[:] = []
            tmp_lst.append(i)
        iter = iter + 1
    final_lst.append(tmp_lst)
    print("Тарелочный стек")
    print(final_lst)


max_size = int(input("Введите размер стека "))
num_dish = int(input("Введите кол-во тарелок "))


dish_stack(max_size,num_dish)










