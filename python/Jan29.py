# list = {
#     "Moe":"A wise guy, huh?",
#     "Larry":"Ow!",
#     "Curly":"Nyuk nyuk!",
#           }
# stooge = "Curly"
# A = 'Larry'
# print(stooge,'says:',list[A])

# count = 1
# while count<=5:
#     print(count)
#     count+=1  #打1到5整数

# while True:
#     stuff = input("String to capitalize[type q to quit]:")
#     if stuff == 'q':
#         break
#     print(stuff.capitalize()) #break跳出循环

# while True:
#     value = input("Integer, please [q to quit]:")
#     if value == 'q':  #停止循环
#         break
#     number = int(value)
#     if number % 2 == 0: #判断偶数
#         continue  #用来跳到循环开始
#     print(number,'squared is', number*number)

# numbers = [1,3,5]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number %2 == 0:
#         print('Found even number',number)
#         break
#     position +=1
# else: #没有执行break
#     print('No even number found')

# word = 'cat'
# for a in word: #迭代用法
#     print(a)
#     if a =='a':
#         break

# cheeses = [1]
# for cheese in cheeses:
#     print('This shop has some lovely',cheese)
#     break
# else: #没有break表示没有找到cheese
#     print('This is not much of chesse shop,is it?')  #循环外用else PS没太懂这一块

# cheeses = []
# found_one = False
# for cheese in cheeses:
#     found_one = True
#     print('This shop has some lovely', cheese)
#     break
# if not found_one:
#     print('This is not much of a chees shop, is it?') #也是不太懂 跟上面一样

# for x in range(0,100,5):
#     print (x)

# number_list = []
# number_list.append(1)
# number_list.append(2)
# number_list.append(3)
# print (number_list)

# number_list = []
# for number in range(1,6):
#     number_list.append(number)
# print(number_list)

a_list = [number for number in range(1,6) if number % 2==1]
print(a_list)