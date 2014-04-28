import unittest
import os

from bmv.bmv_local_factory import BMVLocalFactory, Formats
from csv import BMVLocalCSVTest

class BMVLocalFactoryTest(unittest.TestCase):

    def testCSV(self):

        (fileName, bmv_data) = BMVLocalCSVTest.getData()

        BMVLocalFactory.factory(
            Formats.CSV,
            fileName, 
            bmv_data
        )

        count = BMVLocalCSVTest.countFileLines(fileName)

        #make sure both the headers and data are added
        self.assertEqual(count, 2)

        BMVLocalFactory.factory(
            Formats.CSV,
            fileName, 
            bmv_data
        )

        count = BMVLocalCSVTest.countFileLines(fileName)

        #make sure just the data is added
        self.assertEqual(count, 3)

        #remote the file
        os.remove(fileName)

