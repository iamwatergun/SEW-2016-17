import threading
import string
import random

#ut all Letters and numbers into a string with ascii
ascii = string.ascii_letters + string.digits
random_ascii = ''.join(random.sample(ascii, len(ascii)))

my_dict = dict(zip(ascii, random_ascii))
#inputs
text = ""
number = 0

crypt = []

def check_inputs(text, number):
    # Checks if the inuts are the right type
    check = False

    # checks number for int
    try:
        val = int(number)
        check = True
    except ValueError:
        print("You didn't put in a number!")

    # if number is int checks text for string
    if text.isalpha() and check == True:
        return check

    return False

def divide_input(text,number):
    #divides the text into the threadcount and puts the pieces in a list
    # divides the input to the ammount of threads and rounds down
    #then adds the rest of the input to the last thread making it bigger than the others
    #then returns the list with the pieces
    __length = len(text)

    #make number to int
    number = int(number)

    #divide string length by thread count
    __div = int(__length / number)

    #gets the rest of the division
    __rest = __length % number

    #list
    __list=[]

    #fills list
    i = 0
    for i in range(0, number):
        __list.append(text[int(i*__div):int(i*__div+__div)])

    #append the rest which isnt divideable by the 'number'
    if __rest != 0:
        __list[number-1]= __list[number-1]+(text[len(text)-__rest:len(text)])
    #print the list to see if the split worked
    print('The threads look like this: ')
    print(__list)

    #returns the list
    return __list

class Au02(threading.Thread):
    #Constructor
    def __init__(self,inputtext):
        threading.Thread.__init__(self)
        self.inputtext = inputtext
    #overrides the run() method
    def run(self):
        #for loop which loops through the ammount of textpieces
        for i in range(len(self.inputtext)):
            if self.inputtext[i] == " ":
                crypt.append(" ")
            else:
                #adds the crypted letters from my_dict to the crypt list
                crypt.append(my_dict[self.inputtext[i]])

def main():
    #Main method

    #sets inputs
    text = input("Which message do you want to encrypt?")
    number = input("How many Threads should encrypt the message?")

    #calls the divided_text method with the inputs
    divided_text = divide_input(text, number)

    #creates a list for the threads
    thread_list = []

    #for loop which puts the threads into the list
    for i in range(0, int(number)):
        #creates a new thread with the piece of the input
        t = Au02(divided_text[i])
        #starts the new thread
        t.start()
        #waits for the end of the run(9 function with join()
        t.join()
        #appends the thread to the list
        thread_list.append(t)

    #prints an empty line for beauty reasons
    print()
    print('The encryted results look like this: ')
    # prints the crypted list
    print(crypt)

    for i in crypt:
        #print my_dict.keys()[my_dict.values().index(i)]
        print(list(my_dict.keys())[list(my_dict.values()).index(i])

#starts the main() method
main()