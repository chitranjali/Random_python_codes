"""
This is the journal module.
"""
import os

def load(name):
    """
    This method creates and loads a new journal.
    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    size = 0
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
                # size = size + 1#sum(1 for entry in fin)

    return data,size

def save(name, journal_data,size):
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
                fout.write(entry + '\n')


def get_full_pathname(name):
    # Get OS independant path
    directory = 'journals'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return  os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))

def add_entry(text, journal_data):
    journal_data.append(text)
