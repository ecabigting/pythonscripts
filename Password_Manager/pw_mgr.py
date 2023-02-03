from cryptography.fernet import Fernet
import os.path

#region function definitions

def write_key():
    key = Fernet.generate_key()
    # "wb" write byte mode
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    keyFile = open("key.key","r")
    key = keyFile.read()
    keyFile.close()
    return key

def view():
    with open("plist.txt","r") as f:
        for line in f.readlines(): # read all the lines in the file
            data = line.rstrip() # rstrip remove the breakline in the end of the file
            dLabel, dUname, dPword = data.split("|")
            print(" >> Label: " + dLabel)
            print(" >> Username: " + dUname)
            print(" >> Access: " + dPword)
            print("....")

def add():
    label = input("Give this credentials a label: ")
    uname = input("Set Username: ")
    pword = input("Set Password: ")

    '''
    set the open mode to "a" append, add the
    declare it as "f" to automatically handle open and closing of
    file instead of declaring it as a file that manually opens and needs closing
    additional parameters instead of "a"
    "w" for write, override if file exist
    "r" only open as read-only, throws an error if file does not exist
    "a" append mode, add to the end of file, or create the file if it does not exist
    '''
    with open("plist.txt","a") as f:
        f.write(label + "|" + uname + "|" + fer.encrypt(pword.encode()) + "\n")

#endregion

if(os.path.exists("key.key")):
    key = load_key()
else:
    write_key()
    key = load_key()

root_pwd = input("root:")   

key = load_key() + root_pwd.bytes
fer = Fernet(key)

while True:
    mode = input("New Password(cmd:add) View Existing(cmd: view) Quit(cmd: q) ").lower()
    if mode == "q":
        break

    if mode == "view" : 
        view()
    elif mode == "add":
        add()
    else:
        print("-- Invalid Input --")
        continue


##DLn3jOsNRVE?t=5339