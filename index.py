# #set1 = {1,2,3,4,5}
# #set2 = {5,6,7,8,9,10,}
# #set3 = set1 + set2
# #print(set3)
# x = 11
# print("pass, good work") if x == 10 else print
# # map and filter
# def s(n):
#     if n%2 == 0:
#         return "even"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = list(filter(s, numbers))
# f = open("example.txt","w")
# f.write("Hello, world! 1")
# f.write("\nHello, world!\n")
# f.write("Hello, world! 2")
# f = open("example.txt","r")
# print(f.read())
# g =open("example2.txt","w")
# g.write("Example2\nExample2 123")
# # g.close()
# h = open("example2.txt","r")
# print(h.read())
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

P =Person("john Doe")    


print(P.name)