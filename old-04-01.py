from hashlib import sha1

f = open("list.csv", 'w')

for i in range(10000000, 100000000):
    password = str(i) + "salt_for_you"

    for j in range(0, 500):
        password = sha1(password.encode('utf-8')).hexdigest()

    print(str(i) + ", " + password)
    f.write(str(i) + ", " + password + "\n")

f.close()
