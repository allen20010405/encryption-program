# 5/24/2023
""" This is a sample program and will never work in practice
note this from the creator of this program 豆贝尔维
(this is my fake name)
anyway, this program is open source,and you can change whatever you want about it
if you like this program, please consider a 13-year-old made it, and learn programing yourself to learn how this work
contribution to the people at jet brains for pycharm, and shout out to 小甲鱼"""


# import prime_generator
# mod function
# I can use the one in math, but I don't want to exclud the people who don't have python
# want to make a c++ version soon, but until then you have to compile this yourself
# this will probably have no gui, but the c++ one will
def mod(b, e, m):
    output = (b ** e) % m
    return output


# How this should work
# m^e mod N = c
# e, N and c are public
# given m, e and N, calculating c is easy,
# given e, N, and c, calculating m is hard
# m = message, e = random exponent, N = random number, c = cypher text
# easy in theory, harder in practice,
