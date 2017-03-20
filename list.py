# words = ['word','fun']
# index = 1
# words.insert(index,'is')
# print(words)

# nums = list(range(5))
# print(nums[4])

# numbers = list(range(3,8))
# print(numbers)

# print(range(20) == range(0,20))

# num = list(range(2,20,3))
# print(num)

# words = ['hello','world','spam','eggs']
# for word in words:
# 	print(word + '+');

# for i in range(10):
# 	if not i%2 ==0:
# 		print(i)

# list = [1,2,3,4]
# if len(list) %2 == 0:
# 	print(list[0])

# letters  = [ 'x','y','z']
# letters.insert(1,'w')
# print(letters[2])

# def shout(word):
# 	""" 
# 	print a word with an excalmation mark following it .
# 	"""
# 	print(word+"!")
# shout("spam")

#function as a object 
# like as function pointer in C

# def multiply(x,y):
# 		print(x*y)
# a = 4 
# b = 7 
# opera = multiply
# opera(a,b)

# def add(x,y):
# 	return x+y
# def do_2(fun,x,y):
# 	return fun(fun(x,y),fun(x,y))
# a = 2
# b = 10
# print(do_2(add,a,b))


# import random
# for i  in range(5):
# 	val = random.randint(1,6);
# 	print(val)

# try:
# 	val = 10
# 	print(10/2)
# except( Exception ):
# 	print('error')
# print("finished")

# print(1)
# raise ValueError
# print(2)

# if the file not exsist it will create it
# file = open("newfile.txt",'w') 
# writedNum = file.writedNume("new file created by zq\n")
# file.close()

# file = open("newfile.txt","r");
# print(file.read())
# file.close()


# try:
#     f = open("filename.txt","w")
#     print(f.read())
# except:
# 	print('error')
# finally:
#     f.close()

# #字典
# ages = {"zq":20,"zx":20,"zd":20}
# print(ages["zq"])
# print(ages["zx"])		

# pairs = {
# 	"orange":[2,3,4],
# 	True:False,
# 	None:"True"
# }
# print(pairs.get("orange"))
# print(pairs.get(7))
# print(pairs.get(True,"not in dictionary"))  # get(key,defaultVal""" if no find the val of key""")


#元组 不可改变的list
# words = ("hello","eggs","haha")
# print(words)


#string formatting
# nums = [4,5,6]
# msg = "NUmbers:{0}{1}{2}".format(nums[0],nums[1],nums[2])
# print (msg)
# print("{0}{1}{0}".format("a","bb"))
# print("{x}{y}".format(x=1,y=12))


#string function
# print("hello me".replace("me","world"))
# print("This is a sentence".startswith("This"))
# print("this is a sentence".endswith("e"))
# print("this is a sentence".upper())
# print("this is a Sentence".lower())
# print("spam,eggs,ham".split(","))

#Text analyer
# filename = input("enter filename:\n")
# with open(filename) as file:
# 	text = file.read()
# print(text)

#best way to open file 
# for line in open("filename.txt"):
# 	print(line)
# 	

# def make_word():
# 	word =""
# 	for ch in "spam":
# 		word+=ch
# 		yield word

# print(list(make_word()))
# 
#
#
#集合
# first = {1,2,3,4,5,6}
# second = {4,5,6,7,8,9}

# print(first|second)
# print(first&second)
# print(first-second)
# # no have + operation replace by | operation
# #print(first+second)
# print(second-first)
# print(first^second) # i have but you not have  and add it to this set


# def power(x, y):
#   if y == 0:
#     return 1
#   else:
#     return x * power(x, y-1)
# print(power(2, 3))

#2*(2*(2*(2,0)))



# import sys  
# import os.path  
# import win32clipboard as w 
# import win32con 

# def getText():#读取剪切板  
#     w.OpenClipboard()  
#     d = w.GetClipboardData(win32con.CF_TEXT)  
#     w.CloseClipboard()  
#     return d  
# def setText(aString):#写入剪切板  
#     w.OpenClipboard()  
#     w.EmptyClipboard()  
#     w.SetClipboardData(win32con.CF_TEXT, aString)  
#     w.CloseClipboard()  
# if __name__=='__main__':  
#     a="你好"  
#     setText(a)#将“你好”写入剪切板  
#     
# python 接受命令行参数
# import sys
# print("prama:{0}".format(len(sys.argv)))
# print("list:"+str(sys.argv))

# class
# class ClassName(object):
# 	i = 12345
# 	def f(self):
# 		return 'hello world'
# x  = ClassName()
# print(x.i)
# x.i = 1222
# print(x.i)
# 
#序列化
# import pickle
# import pprint

# class Account:
# 	hint =''
# 	account = ''
# 	pwd = ''
# 	pass

# account = Account()
# account.hint="aaa"
# account.account ='bb b'
# account.pwd='ccc'
# output = open("aaa",'wb')

# account1 = Account()
# account1.hint="dierge"
# account1.account ='disange'
# account1.pwd='dierge'

# pickle.dump(account,output)
# pickle.dump(account1,output)
# output.close()

# pklfile =open('aaa','rb')
# data1 = pickle.load(pklfile)
# print(data1.hint+data1.account+data1.pwd)
# data2 = pickle.load(pklfile)
# print(data2.hint+' '+data2.account+' '+data2.pwd)
# pklfile.close()
# 
# 

a = "aaaa"
b = "bbb"
print(a*5)