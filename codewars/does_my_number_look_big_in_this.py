# does my number look big in this? by kenny zhang
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

print(narcissistic(153))
print(narcissistic(1652))