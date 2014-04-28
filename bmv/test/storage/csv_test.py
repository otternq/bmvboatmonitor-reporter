import unittest
import os

from bmv.bmv_local_csv import BMVLocalCSV

class BMVLocalCSVTest(unittest.TestCase):

    @staticmethod
    def getData():
        return [
            "./tests_results/test.csv",
            {"FW": "211", "ALARM": "OFF", "SOC": 78.0, "H10": 41, "BMV": "600S", "TTG": 5103, "I": -3.314, "H11": 29, "H12": 0, "CE": -116.175, "AR": "0", "V": 24.095, "H8": 29801, "H9": 2.18881944367398, "RELAY": "OFF", "H2": -116.175, "H3": 0.0, "H1": -259.107, "H6": -8832.716, "H7": 18.677, "H4": 1, "H5": 0.0}
        ]

    @staticmethod
    def countFileLines(file):
        """Auxilary to cound the number of lines in a file

        Keyword arguments:

        file -- The file to cound

        Returns:

        The number of lines in the file
        """
        return len(open(file).readlines(  ))

    @staticmethod
    def addData(fileName, bmv_data):
        """Auxilary to perform actions to be tested

        Keyword arguments:

        fileName -- Where to store data
        bmv_data -- The data to store

        Returns:

        The number of lines in the file
        """

        BMVLocalCSV.store(
            fileName,
            bmv_data
        )

        return BMVLocalCSVTest.countFileLines(fileName)


    def testStore(self):

        (fileName, bmv_data) = BMVLocalCSVTest.getData()

        count = BMVLocalCSVTest.addData(fileName, bmv_data)

        #make sure both the headers and data are added
        self.assertEqual(count, 2)

        count = BMVLocalCSVTest.addData(fileName, bmv_data)

        #make sure just the data is added
        self.assertEqual(count, 3)

        #remote the file
        os.remove(fileName)

        
