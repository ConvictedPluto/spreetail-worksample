#Spreetail Work Sample: Multi-Value String Dictionary (MVD)
#Author: Lj Leuchovius

#Global Variables
mvd = {}
q = False

#This main function prompts the user to enter commands until they QUIT the app. 
def main(): 
    print("""Welcome to Multi-Value String Dictionary!
    Enter a command, or type HELP for a list of commands!""")
    while q == False:
        raw_command = input("")
        command = parse(raw_command)
        if valid(command[0]):
            redirect(command)
        elif command[0] == "":
            print("Please enter a command. Enter HELP for a list of commands.")
        else:
            print("ERROR, " + command[0] + " is not a valid command.")

#This function reformats the user's input into a three-item command list.
#The first item will be the command itself (e.g. "ADD").
#The second is the relevant key. This is empty if a key is not given.
#The third is the relevant member. This is empty if a member is not given.
def parse(raw_command):
    raw_command = raw_command.strip()
    command = raw_command.split(" ")
    command[0] = command[0].upper()
    if len(command) < 2:
        command.append("") 
    if len(command) < 3:
        command.append("")
    if len(command) > 3:
        command[2] = concat(command[2:])
    return command[:3]

#This function concatonates a list of strings into a string separated by spaces.
#This allows the MVD to store member strings containing spaces (e.g. "Rock & Roll").
def concat(member_list):
    member = member_list[0]
    for word in member_list[1:]:
        member += " "
        member += word
    return member

#This function returns whether the given command is valid.
#(Right now, it's small, but it's abstracted in case other criteria are added later.)
def valid(command):
    return command in command_functions

#This function redirects the user to a function corresponding to their command.
#To simplify redirection, even functions not requiring parameters have them.
#Functions not requiring a key and/or value are passed empty string(s) instead.
#This also allows scalability if new requirements for parameters are added later.
def redirect(command):
    command_functions[command[0]](command[1], command[2]) 
    
#This function corresponds to the ADD command as documented in the requirements.
def add(key, member):
    if key == "":
        print("ERROR, the empty string is not a valid key.")
    elif member == "":
        print("ERROR, the empty string is not a valid member.")
    else: 
        if key not in mvd:
            mvd[key] = set()
        if member in mvd[key]:
            print("ERROR, member already exists for key.")
        else: 
            mvd[key].add(member)
            print("Added") 

#This function corresponds to the KEYS command as documented in the requirements.
#Since KEYS does not require parameters, it ignores any parameters the user gives.
def keys(key, member):
    for key in mvd:
        print(key)

#This function corresponds to the MEMBERS command as documented in the requirements.
#Since MEMBERS only requires one parameter, it ignores any extras the user gives.
def members(key, member):
    if key in mvd:
        for member in mvd[key]:
                print(member)
    else:
        print("ERROR, key does not exist.")
            
#This function corresponds to the REMOVE command as documented in the requirements.
def remove(key, member):
    if key in mvd:
        if member in mvd[key]:
            mvd[key].remove(member)
            print("Removed")
            if len(mvd[key]) == 0:
                mvd.pop(key)
        else:
            print("ERROR, member does not exist.")
    else:
        print("ERROR, key does not exist.")
                
#This function corresponds to the REMOVEALL command as documented in the requirements.
#Since REMOVEALL only requires one parameter, it ignores any extras the user gives.
def removeall(key, member):
    if key in mvd:
        mvd.pop(key)
        print("Removed")
    else:
        print("ERROR, key does not exist.")

#This function corresponds to the CLEAR command as documented in the requirements.
#Since CLEAR does not require parameters, it ignores any given parameters.
def clear(key, member):
    mvd.clear()
    print("Cleared")

#This function corresponds to the KEYEXISTS command as documented in the requirements.
#Since KEYEXISTS only requires one parameter, it ignores any extras the user gives.
def keyexists(key, member):
    print(key in mvd)

#This function corresponds to the MEMBEREXISTS command as documented in the requirements.
def memberexists(key, member):
    if key in mvd: 
        print(member in mvd[key])
    else:
        print(False)

#This function corresponds to the ALLMEMBERS command as documented in the requirements.
#Since ALLMEMBERS does not require parameters, it ignores any given parameters.
def allmembers(key, member):
    for key in mvd:
        for member in mvd[key]:
            print(member)

#This function corresponds to the ITEMS command as documented in the requirements.
#Since ITEMS does not require parameters, it ignores any given parameters.
def items(key, member):
    for key in mvd:
        for member in mvd[key]:
            print(key + ": " + member)

#This function corresponds to an additional HELP command.
#It lists the valid commands in no particular order for usability.
def helpme(key, member):
    print("These are the valid commands, in no particular order:")
    for command in command_functions:
        print(command)

#This function corresponds to a QUIT command that exits the app w/o closing window.
def quitapp(key, member):
    global q
    q = True

#This global is a dictionary associationg valid commands to their functions.
#It is necessary to the redirect function and must be updated to add new commands.
#Python requires this global to be defined after the associated functions. 
command_functions = {"ADD": add, "KEYS": keys, "MEMBERS": members, "REMOVE":
                     remove, "REMOVEALL": removeall, "CLEAR": clear,
                     "KEYEXISTS": keyexists, "MEMBEREXISTS": memberexists,
                     "ALLMEMBERS": allmembers, "ITEMS": items, "HELP": helpme,
                     "QUIT": quitapp}
