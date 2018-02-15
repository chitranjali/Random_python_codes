''' searching folders!'''
from collections import namedtuple
import os
import glob
import sys


def main():
    # All_matches = []
    folder, search_string = get_user_input()
    all_matches = search(folder, search_string)
    print_matches(all_matches)


def get_user_input():
    folder = input('What directory you want to search?:')
    search_string = input("'What string you're looking for?:")

    # Check folder is not empty and valid folder
    if not folder or not folder.strip() or not os.path.isdir(folder):
        # folder = None
        print('Sorry, Invalid Directory name!')
        sys.exit(1)
    else:
        # os.path.abspath() ~ os.path.join()
        folder = os.path.abspath(folder)
        return folder, search_string


def search(folder, search_string):
    all_matches = []
    # items = os.listdir(folder)
    ''' Get folder contents'''
    # To skip hidden files such as .ds_store on OSX (OSX specific)
    items = glob.glob(os.path.join(folder, '*'))
    #  Use recursion to check sub folders. [all_matches?]
    for item in items:
        if os.path.isdir(item):
            # search(item, search_string, All_matches)
            matches = search(item, search_string)
            all_matches.extend(matches)
        else:                                   # Base case..
            file_path = os.path.abspath(item)
            matches = search_file(file_path, search_string)
            all_matches.extend(matches)  # Add a list to ano list

    return all_matches


def search_file(file, search_string):
    matches = []
    SearchResult = namedtuple('SearchResult', 'file, line, text')

    with open(file, 'r', encoding='utf-8') as fin:  # encoding?
        line_num = 0
        # reads one line at a time. When the next line is read,
        # the previous one will be garbage collected unless you have stored
        # a reference to it somewhere else
        for line in fin:
            line_num += 1
            # If find is successful, returns >0, else a -1
            if line.find(search_string) >= 0:
                m = SearchResult(file=file, line=line_num, text=line.strip())
                matches.append(m)

    return matches


def print_matches(all_matches):
    # Check new print stat in 3.6
    for item in all_matches:
        # loop over each tuple in list => {item}
        print('{}, line {}  >> {} '.format(os.path.basename(item.file),
                                           item.line, item.text))


main()
