# playing with digits by kenny zhang
# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    temp = str(n)
    total = 0
    for x in temp:
        total += int(x)**p
        p += 1
    if total % n == 0:
        return total // n
    else:
        return -1
    
print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))