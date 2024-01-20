# credit card mask by kenny zhang
# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    temp = list(cc)
    if len(temp) > 4:
        for i in range(len(temp)-4):
            temp[i] = '#'
        return ''.join(temp)
    else:
        return cc

print(maskify('4556364607935616'))
print(maskify('64607935616'))
print(maskify('1'))
print(maskify(''))
print(maskify('Skippy'))
print(maskify('Nananananananananananananananana Batman!'))