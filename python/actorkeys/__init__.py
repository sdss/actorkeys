"""
SDSS-3 Actor keyword dictionaries

Refer to https://trac.sdss3.org/wiki/Ops/KeysDictionary for details.
"""
import os
import glob

def _getStdDictionaryNames():
    currPath = os.path.dirname(__file__)
    allModPaths = glob.glob(os.path.join(currPath, "*.py"))
    allModNames = sorted(os.path.basename(path[0:-3]) for path in allModPaths)
    retList = []
    for modName in allModNames:
        if modName.startswith("_"):
            continue
        if " " in modName:
            continue
        if modName.startswith("test"):
            continue
        retList.append(modName)
    return retList

keyDictionaries = _getStdDictionaryNames()