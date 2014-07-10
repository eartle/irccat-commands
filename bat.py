#!/usr/bin/env python
import sys

batfile = '/usr/share/irccat/.bat.txt'
batqueue = []

sender = sys.argv[1]

def writeFile():
    with open(batfile, 'wb') as f:
        for user in batqueue:
            print>>f, user

# read the queue in from file
with open(batfile, 'rb') as f:
    for line in f:
        user = line.rstrip()
        if len(user) is not 0:
            batqueue.append(user)

if len(sys.argv) == 6:
    # they've given a command
    command = sys.argv[5]

    if command == 'request':
        if sender not in batqueue:
            batqueue.append(sender)
            writeFile()

            if len(batqueue) == 1:
                print sender + ': the cricket bat is yours!'
            else:
                print sender + ': you\'ve been added to the end of the queue in position ' + str(batqueue.index(sender) + 1) + '.'

        else:
            if batqueue.index(sender) == 0:
                print sender + ": you already have the bat!"
            else:
                print sender + ': you\'re already ' + str(batqueue.index(sender) + 1) + ' of ' + str(len(batqueue)) + ' in the queue.'


    elif command == 'done':
        if sender in batqueue:
            index = batqueue.index(sender)
            batqueue.remove(sender);
            writeFile()
            
            if index == 0 and len(batqueue) > 0:
                print sender + ": you've been removed from the queue."
                print batqueue[0] + ': you now have the cricket bat so get testing!'
            else:
                print sender + ": you've been removed from the queue, which is now empty."
        else:
            print sender + ": you're not in the queue."
    else:
        print sender + ": sorry, I only understand 'request' and 'done'."

elif len(sys.argv) == 5:
    # the user has not issued a command
    if sender in batqueue:
        index = batqueue.index(sender)

        if index == 0:
            print sender + ': you have the cricket bat.'
        else:
            print sender + ": " + batqueue[0] + " has the cricket bat and you're " + str(batqueue.index(sender) + 1) + ' of ' + str(len(batqueue)) + ' in the queue.'
    
    elif len(batqueue) > 0:
        print sender + ": " + batqueue[0] + ' has the cricket bat and you\'re not even in the queue.'
    else:
        print sender + ": there's no one in the queue."
else:
    # I didn't understand that
    print sender + ": sorry, I only understand 'request' and 'done'."
