root_pwd = input("root?:")

def view():
    pass #keyword literal do nothing

def add():
    label = input("Give this credentials a label: ")
    uname = input("Set Username: ")
    pword = input("Set Password: ")

    # set the open mode to "a" append, add the
    # declare it as "f" to automatically handle open and closing of
    # file instead of declaring it as a file that manually opens and needs closing
    # additional parameters instead of "a"
    # "w" for write, override if file exist
    # "r" only open as read-only, throws an error if file does not exist
    # "a" append mode, add to the end of file, or create the file if it does not exist
    with open("plist.txt","a") as f:
        f.write(label + "|" + uname + "|" + "|" + pword)
        

while True:
    mode = input("New Password(cmd:add)? View Existing(cmd: view)?").lower()
    if mode == "q":
        break

    if mode == "view" : 
        view()
    elif mode == "add":
        add()
    else:
        print("-- Invalid Input --")
        continue
