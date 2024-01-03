#password gen by kenny zhang

import random, string, time

def main():
    password = []
    length = 16
    
    for x in range(random.randint(5,6)):
        temp = random.choice(string.digits.replace('0''1', ''))
        password.append(temp)
    for x in range(random.randint(5,6)):
        temp = random.choice("@&$!#?%")
        password.append(temp)
    temp = length - len(password)
    for x in range(temp):
        temp = random.choice(string.ascii_letters.replace('I''l''o''O',''))
        password.append(temp)

    random.shuffle(password)
    password = "".join(password)
    print(password)
    time.sleep(10)
    
if __name__ == "__main__":   
    main()




