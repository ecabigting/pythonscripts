root_pwd = input("root?:")

def view():
    pass #keyword literal do nothing

def add():
    label = input("Give this credentials a label: ")
    uname = input("Set Username: ")
    pword = input("Set Password: ")

    # set the open mode to "a" append
    # declare it as "f" to automatically handle open and closing of
    # file instead of declaring it as a file that manually opens and needs closing
    with open("plist.txt","a") as f:
        

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
