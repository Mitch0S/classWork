import random
import hashlib

a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_"
newpwd = ""
uppercase = 0
amt = 0
pwd = ""

for i in a:
    amt = amt + 1

pwdLen = int(input("How long do you want this password to be?\n> "))

for i in range(pwdLen):
    pwd = pwd + a[random.randint(0, amt-1)]
#print(pwd)

for digit in pwd:
    if digit.isupper():
        uppercase = uppercase+1
    if uppercase > 3:
        newpwd = newpwd+digit.lower()
    else:
        newpwd = newpwd+digit
hashnewpwd = newpwd.encode("utf-8")
hashnewpwd = hashlib.sha512(hashnewpwd).hexdigest()
print(("The originally generated password was {}, the sha512 hashed password is on the following line\n{}").format(newpwd, hashnewpwd))
