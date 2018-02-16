import string
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar)
for x in range(rand(int(min_char, max_char))))
print ("This is your password : ",password)
