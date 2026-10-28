ls=["\nHello, World!", "\nThis is a new line added to the file."]
with open('exp.txt','a') as file:
    file,writelines(ls)