#Opens the txt file for python to read
log_file = open("um-server-01.txt")

#Creating a function that takes in the txt file as a param
def sales_reports(log_file):
    #Starts a loop that will go through each line of of the txt file
    for line in log_file:
        #Removes any white-space after the string is finished
        line = line.rstrip()
        #Declaring the variable day to equal the first three character on each line
        day = line[0:3]
        #Saying 'if' those three characters match this string then perform the next action
        if day == "Mon":
            #If the coniditions are met, it will print or 'console log' that line
            print(line)

#Calling the function to run with the txt file passed in as the param
sales_reports(log_file)
