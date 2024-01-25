#Assigning 'import_file' to the file.
import_file = "allowed_ip.txt"

#Defining function to update imported file..
#parameter 1 accepts allowed IP addresses file(import file).
#parameter 2 accepts remove/(not allowed) list of IP addresses.
def update_list(import_file, remove_list):

    #opening the allow list file to read contents
    with open(import_file, "r") as file:
        allowed_ip = file.read()

    #Converting the file containing strings into list using .split() method
        allowed_ip = allowed_ip.split()

    # Looping through the allowed_ip.
    # variable = "element"
    for element in allowed_ip:

        #applying condition 'if' the element matches with any element in remove list.
        #then removing it from the allowed_ip.
        if element in remove_list:
            allowed_ip.remove(element)

    #Applying .join() method to allowed_ip to convert it back to list.
            allowed_ip = " ".join(allowed_ip)

    #Opening the original allowed ip file.
    #Rewrite the contents with the updated contents.
    with open(import_file, "w") as file:
        file.write(allowed_ip)

    #opening the updated allow list file for reading purpose.
    with open(import_file, "r") as file:
        text = file.read()

    #Displaying file contents on screen.
    print(text)
    

