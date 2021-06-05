# Question 1
print("I love Programin!")

#Questtion 2
print("I can't wait to make my first game!")

#Chapter 2

city = "Barueri"
year = 2021

print(city + " " + str(year))

#Chapter 3

brands =  ["GM", "FORD", "VW", "FIAT", "NISSAN", "HONDA"] #4
print(brands[1]) #5
brands.append("bicycle") #6
print(brands) #7
brands[0] = "Bruno" #8
print(brands) #9
brandtwo = brands[0] + ' ' + brands[1] #10
print(brandtwo) #11
brandlast = brands[6].upper() #12
print(brandlast) #13 
brands.insert(2,"Barueri") #14
print(brands) #15
brands.pop(1) #16
print(brands) #17
brandpoplast = brands.pop() #18
print(brandpoplast) #19
brandpopfirst = brands.pop(0) #20
print(brandpopfirst) #21
fruits = ["melon", "banana", "apple"] #22
print(fruits) #23
print(fruits[-3]) #31
fruitcopy = sorted(fruits) #28
print(f'{fruitcopy}\n{fruits}') #29
print(sorted(fruits)) #24 and 25
fruits.sort(reverse=True) #26
print(fruits) #27 
print(len(fruits)) #30



