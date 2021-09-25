# Your name: Luis Fernando Solano
# Your student id: 06415334
# Your email: solanol@umich.edu
# List who you have worked with on this homework:


# import the random module for use in this program
import random

# Create the class Crystal_Ball
class Crystal_Ball:

    # create the constructor (__init__) method
    # it takes as input: a list of possible predictions
    # it takes as input: a list of possible names
    # it sets this object's prediction_list (instance variable) to the passed list of possible predictions
    # it sets this object's name_list (instance variable) to the passed list of possible names
    # it sets this object's prediction_history_list (instance variable) to an empty list
    # it sets this object's name_history_list (instance variable) to an empty list 

    def __init__(self, prediction_list, name_list):          
        prediction_list = prediction_list
        name_list = name_list           # how to pass this list correctly 
        self.prediction_history_list = []
        self.name_history_list = []
    
    # create the __str__ method
    # It should return a string with all the predictions
    # in prediction_list separated by commas
    
    def __str__(self, prediction_list):
        seperated_by_commas = ','.join(prediction_list)      
        str(seperated_by_commas)
        print(seperated_by_commas)

    # create the predict method that takes a name
    # it randomly picks an index from 0 to the number of items in the prediction_list minus one
    # it adds that index to the end of the prediction_history_list
    # it randomly picks an index from 0 to the number of items in the name_list minus one
    # it adds that index to the end of the name_history_list
    # It adds the passed name to the end of the name_list
    # it returns a string with the prediction at the picked index followed by the name at the name index

    def predict(self, name): 
        prediction_random_index = random.prediction_list(0, -1)  # do i need to put -1 or is it a given "minus 1"
        self.prediction_history_list.append(self.prediction_list[prediction_random_index])
        name_random_index = random.name_list(0, -1)              # do i need to put -1 or is it a given "minus 1"
        self.name_history_list.append(self.name_list[name_random_index])
        self.name_list.append(name)
        self.selected_prediction_and_name = self.prediction_list[prediction_random_index] + self.name_list[name_random_index]
        print(self.selected_prediction_and_name)

    # create the check_name method that takes a name
    # it checks if the name is in the name_list and if so returns
    #         "I already have that name!”
    # Otherwise it returns the prediction from predict

    def check_name(self, name):
        possible_repeat = self.name_list.count(name)        # does this work for strings or just ints?
        if possible_repeat  > 0:
            print("I already have that name!")
        else:
            print(self.selected_prediction_and_name)  # how to communicate to previous method

    # create the print_history method
    # prints "[prediction index] prediction - [name index] name" for each of the indices in the prediction_history_list
    # from the first to the last with each on a single line.  If there are not items in the
    # prediction_history_list it prints "None yet"
    # it does not return anything!

    def print_history(self):                                   # what parameters are used
        for x in range(len(self.prediction_history_list)):    # how to communicate to previous 
            for x in range(len(self.name_history_list)):
                print(self.prediction_history_list[x] + " prediction at index - " + self.name_history_list[x] + " name at index")
        if not self.prediction_history_list:
            print("None yet")


    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random response n times by calling predict.
    # It prints the counts for each prediction index, and
    # prints the most frequently occurring prediction index and prediction

def main():

    # Replace the prediction_list with your desired predictions!
    prediction_list = ["Is going to take a class with ",
                        "Will fall in love with ",
                        "Will spill on ",
                        "Must go on a walk with ",
                        "Is going to have a snowball fight with "]
    # Replace the name_list with your desired names!
    name_list = ['Yasmeen', 'Xinghui', 'Elaina', 'Anna', 'Ewelina', 'Nik']
    bot = Crystal_Ball(prediction_list, name_list)

    # get the first name or quit
    name = input("Give first name or type quit")
    # loop while name is not "quit"
    while name != "Quit" or "quit":
        # get the result from check_name
        bot.check_name(name)                 # bot. added correctly or?
       
        name_check = bot.check_name
        # print name - result from check_name
        print(name + " - " + name_check)
        # get the next name or quit
        name = input("Give first name or type quit")
 


def test():

    prediction_list = ["Is going to take a class with ",
                        "Will fall in love with ",
                        "Will spill on ",
                        "Must go on a walk with ",
                        "Is going to have a snowball fight with "]

    name_list = ['Yasmeen', 'Elaina', 'Anna', 'Ewelina', 'Nik']

    print()
    print("Testing Crystal Ball:")
    bot2 = Crystal_Ball(prediction_list,name_list)

    print("Testing the __str__ method")
    print(bot2)
    print()
'''
    print("Printing the history when no predictions have been generated yet")
    bot2.print_history()
    print()

    print("Giving the name: Muna")
    print(bot2.check_name("Muna"))
    print()

    print("Giving the name: Muna again")
    print(bot2.check_name("Muna"))
    print()

    print("Giving the name: Mike")
    print(bot2.name_list("Mike"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()

    print("Printing name_list")
    print(bot2.name_list())      # changed bot2.check_name_list() to bot2.name_list()
    print()
'''
    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    # print("Testing most_frequent method")
    # print(bot2.most_frequent(1000))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    #main()                                         #commented main out temporarily 
    test()
