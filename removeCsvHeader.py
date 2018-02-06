import os
import csv

os.makedirs('headerRemoved', exist_ok=True)
dir_loc =  ''

# Take Directory of CSV files to be changed
while not os.path.isdir(dir_loc):
    dir_loc = input('Enter Location of direcory')
# Dir_loc = '/Users/chitranjali/Downloads/automate_online-materials/cs/NAICS_data_1048.csv'

for folderName, subfolders, filenames in os.walk(dir_loc): #Takes Dir path
    for filename in filenames:
        if filename.endswith(".csv"):
            print('Removing header from ' + filename + '...')

            # Open and read CSV file for which header needs to be removed
            try:
                ReadFileObject = open(os.path.join(folderName, filename))
                readerObj = csv.reader(ReadFileObject)

                # Open and create writer object for new CSV file
                WriteFileObj = open(os.path.join('headerRemoved', filename), 'w', newline='')
                WriterObj = csv.writer(WriteFileObj)

                # Write to new file skipping first line
                for row in readerObj:
                    if readerObj.line_num == 1:
                        continue
                    WriterObj.writerow(row)
            except (IOError, OSError, Failure) as e:
                pass
            finally:
            # Close Reader and writer objects(Files)
                ReadFileObject.close()
                WriteFileObj.close()

print(" Files are created")
