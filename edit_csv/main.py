'''
Created on 8 janv. 2017

@author: bruno
'''
import csv

FILE_NAME = 'test.csv'
DELIMITER = ';'

'''
 Read the file filename as a csv document using the delimiter delimiter
 returns an array of its rows
'''
def readCsvFile(filename, delimiter):
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        rows = []
        for row in reader:
            rows.append(row)
        return rows
'''
 Write content of the array rows to the CSV file filename (creates it if needed)
 using the delimiter delimiter
'''
def writeCsvFile(filename, delimiter, rows):
    with open(filename, 'w+', newline='') as csvfile:
        if(len(rows)>0):
            writer = csv.writer(csvfile, delimiter=delimiter)
            for i in range(len(rows)):
                writer.writerow(rows[i])

if __name__ == '__main__':
    rows = readCsvFile(FILE_NAME, DELIMITER)
    print(rows)
    