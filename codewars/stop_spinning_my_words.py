# stop spinning my words! by kenny zhang
# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    temp = sentence.split()
    output = []
    for x in temp:
        if len(temp[x]) >= 5:
            output.append(temp[x][::-1])
        else:
            output.append(temp[x])
    return " ".join(output)

print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))

