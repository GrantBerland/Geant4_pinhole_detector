#!/usr/bin/python3.5


import pandas as pd
import numpy as np
import sys

class RunFileParser:
    def __init__(self, fileName=None):

        '''
        User can either enter filename on RFP construction,
        auto parse the hit file for filename, or
        enter filename from CLI
        '''

        self._filePath = '../macros/'
        self._fileName = fileName

        fileName = self.parseHitFileForFilename()

        if fileName is None:
            self._fileName = self.callForFilename()

        self.energy = self.getAttributeFromFile("/gps/energy")
        self.numberOfParticles = self.getAttributeFromFile("/run/beamOn")

    def parseHitFileForFilename(self):
        with open('./data/hits.csv', 'r') as f:
            str = f.readline()
        if str == "NFN":
            return None
        else:
            return str

    def callForFilename(self):
        # TODO: check behavior if input() is empty
        try:
            fileName = sys.argv[1]
        except IndexError:
            print("Enter filename to parse: ")
            fileName = input()
            pass
        return fileName

    def getAttributeFromFile(self, attr):
        with open(self._filePath+self._fileName, 'r') as file:
            file_contents = file.read()
            index = file_contents.find(attr)
            str = file_contents[index+12:index+20]
            str = str.replace('\n','')
            return str

    def getEnergy(self):
        return self.energy
    def getNumParticles(self):
        return self.numberOfParticles
