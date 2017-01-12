'''
Created on 8 janv. 2017

@author: Bruno
'''
import unittest
import edit_csv

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"


class Test(unittest.TestCase):

    # test if we can read a simple CSV file
    def testReadCsvFileHelloWorld(self):
        filename = 'tmpHelloWorld.csv'
        with open(filename, 'w+', newline='') as tmpfile:
            tmpfile.write("1rst word;2nd word;3rd word\nHello;World;!\n")
        rows = main.readCsvFile('tmpHelloWorld.csv', ';')
        assert(rows[0][0] == '1rst word')
        assert(rows[0][1] == '2nd word')
        assert(rows[1][0] == 'Hello')
        assert(rows[1][1] == 'World')
        pass
    
        # we can erase the tmp file
        os.remove(filename)
    
    #test if we can write a simple CSV file
    def testWriteCsvFileHelloWorld(self):
        filename = 'tmpHelloWorld.csv'
        rows = [['1rst word', '2nd word'],['Hello', 'World']]
        # tested function
        main.writeCsvFile(filename, ';', rows)
        
        # test
        with open('tmpHelloWorld.csv', 'rt') as readBackFile:
            content = readBackFile.readline()
            assert(content == "1rst word;2nd word\n")
            content = readBackFile.readline()
            assert(content == "Hello;World\n")
            
        # we can erase the tmp file
        os.remove(filename)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()