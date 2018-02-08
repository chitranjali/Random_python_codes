from Journal import *
import sys
"""
Create journal entries(text file) and display
"""

def main():
    print_header()
    run_event_loop()

def print_header():
    print('------------------------')
    print('        JOURNAL')
    print('------------------------')

#Get events from user and run until user exits..
def run_event_loop():
    user_cmd = ' '

    # Load journal
    journal_name = 'default'
    journal_data,size = load(journal_name)  # list

    while user_cmd != 'x':  # and user_cmd:?
        user_cmd = input("What you want to do? [L]ist entries, [A]dd an entry, E[x]it: ")
        user_cmd = user_cmd.lower().strip()

        if user_cmd == 'l':
            list_entries(journal_data)
        elif user_cmd == 'a':
            add_entries(journal_data)
        elif user_cmd != 'x':
            print("Sorry, we don't understand {} .".format(user_cmd))

    print("Done, Good bye!")
    save(journal_name,journal_data,size)
    sys.exit(0)

def add_entries(journal_data):
    jou_entry = input("Enter your journal entry:")
    add_entry(jou_entry,journal_data)

def list_entries(journal_data):
    print('Your journal entries: ')
    entries = reversed(journal_data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))

if __name__ == '__main__':
    main()





