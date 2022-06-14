
# A simple program without GUI to create, read, update and delete mechanical spares @ a MSME company

import os
import datetime
os.getcwd()

class CRUD: 
    " this class contain 4 modules"
    " Add Spare, Display Spare, Issue Spare, Return Spare,"

    def __init__(self, listOfBooks,LibraryName):
        self.listOfspares="listOfSpares.txt"
        self.LibraryName = LibraryName
        self.sparesDict= {}
        Id = 1001

        with open(self.listOfspares) as spare:
            content = spare.readlines()
        for lines in content:
            self.sparesDict.update({str(Id):{"SparesTitle":lines.replace("\n",""), 
            "lenderName":"", "issueDate": "", "status": "available"}})
            Id = Id+1
    
    def displaySpare(self):
                print()
                print("-----------------------LIST OF SPARES--------------------------")
                #print()
                print("Spares Id", "\t", "Title", "\t\t\t\t\t", "Status")
                print("--------------------------------------------------------------")
                for key, value in self.sparesDict.items():
                    print(key, "\t\t", value.get("SparesTitle"), "\t\t\t\t", "[",value.get("status"), "]")

                                                    
c = CRUD("listOfspares.txt", "python's Library")
print(c.displaySpare())


