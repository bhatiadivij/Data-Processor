import os
import re
import time
## Assuming that all the P*.txt files and sample*.txt files are in the same directory as this data_processor.py file

class DataProcessor:
    def __init__(self):
        self.index = {} ## hash table which stores the srings of all the P* files with keys (filename,string) and value 1
        self.filenames=[] ## list of all P* file names
        cwd=os.getcwd() ## detecting the current working directory
        dir = os.listdir(cwd) ## reading the cwd
        pattern = re.compile("\AP") ## regex for matching P* file names
        for file in dir:
            if pattern.match(file):
                self.filenames.append(file)
                with open(file, encoding="utf8") as f:
                    for content in f:
                        self.index[(file, content.strip())] = 1 ## building the hashtable as a member of the class
                
    def find_property(self, strings):
        property = []
        for filename in self.filenames:
            score = 0
            for string in strings: 
                score += self.index.get((filename, string), 0)
            property.append((filename, score)) ## building the property list 
        property.sort(key=lambda x: x[1], reverse=True) ## sorting the property list in decreasing order of score
        return property

    def process_input(self):
        cwd=os.getcwd()
        dir = os.listdir(cwd)
        pattern = re.compile("\Asample") ## regex to matching the sample* files
        property=[] ## this list will store the list of tuples for every sample* file
        for file in dir:
            t=time.time()
            if pattern.match(file):
                with open(file, encoding="utf8") as f:
                    strings = [x.strip() for x in f] ## reading sample* files
                    property.append(self.find_property(strings))  ## evaluate the property for every sample file
                print(file," : ",time.time()-t)
        ## return or print property list based on the usecase

if __name__ == "__main__":    
    data_processor = DataProcessor()
    data_processor.process_input()
