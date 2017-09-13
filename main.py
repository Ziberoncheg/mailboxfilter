
def func():                                                         # Python version 3.*

    dict = {}                                                       # Dictionary of sender data and quantity
    trigger = False                                                 # New message detector
    f = open('mbox.txt', 'r')                                       # Open file
    for line in f:                                                  # Loop for line in file
        if line.find("From") != -1:                                 # Find substr "From" in line
            if trigger == False:                                    # Check of one use data parse
                endpoint = line.find(" ", 5)                        # Separating the string
                fromstr = line[4:endpoint]                          # Get sender from string
                datestr = line[endpoint + 1:]                       # Get date from string
                try:                                                # We try to add the number of letters to the sender
                    dict[fromstr] += 1                              # if it is in the dictionary or create a new key
                except:                                             # for it and assign a value of 1
                    dict[fromstr] = 1                               #
                trigger = True                                      # Set trigger True
        if line.find('Subject') != -1:                              # If find "Subject" in string:
            subj = line[7:]                                         # get Subject from string
        if line.find("----------------------") != -1:               # Detect of new letter
            trigger = False                                         # Set trigger default value
            print("%s (%s) %s \n" % (fromstr, datestr, subj))       # Print task data

    for key, value in dict.items():                                 # Lop for dictionary of sender data and quantity
        print("%s: %s \n" % (key, value))                           # Print sender data and quantity
    f.close()                                                       # Close file

