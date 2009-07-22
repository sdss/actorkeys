"""
SDSS-3 Actor keyword dictionaries

Refer to https://trac.sdss3.org/wiki/Ops/KeysDictionary for details.
"""
import os
import glob

def _getStdDictionaryNames():
    currPath = os.path.dirname(__file__)
    nonStdDicts = ("__init__.py", "testing.py")
    allModules = glob.glob(os.path.join(currPath, "*.py"))
    retList = []
    for modPath in allModules:
        modName = os.path.basename(modPath)
        if "_" in modName:
            continue
        if " " in modName:
            continue
        if modName.startswith("test"):
            continue
        retList.append(modName[0:-3])
    return retList

keyDictionaries = _getStdDictionaryNames()