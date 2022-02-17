from  cryptography.fernet import  Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key",'rb') #> rb> write in byte mode
    key = file.read()
    file.close()
    return  key


master_pwd = input("Whats your master password? \n")
key  = load_key() + master_pwd.encode() # storing it in byte
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        count = 1
        for line in f:
            print(f"{count}.")
            data = line.rstrip()
            user,passw = data.split("|")
            print("user name : ",user, "> password : ", fer.decrypt(passw.encode()).decode())
            count +=1

def add():
    name = input('Account name: ')
    pwd  = input('Password: ')
    '''
    open > creates file named inside the parameter in ide. 
    with > open the file and close the file automatically when the work is done
    a > appending mode
    w > if you already have, it will clear it and starts writing
    r > read mode
    '''
    with open('password.txt', 'a') as f:
        f.write(name+ "|" + fer.encrypt(pwd.encode()).decode() +"\n") # created a

while True:
    mode = input("Would you like to add a new password or view existing one(view) or add or q(quit) \n").lower()

    if mode == 'q':
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("invalid mode")
        continue
