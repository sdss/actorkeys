"""
SDSS-3 Actor keyword dictionaries

Refer to https://trac.sdss3.org/wiki/Ops/KeysDictionary for details.
"""
import glob

def _getStdDictionaryNames():
    nonStdDicts = ("__init__.py", "testing.py")
    allModules = glob.glob("*.py")
    retList = []
    for modName in allModules:
        if "_" in modName:
            continue
        if " " in modName:
            continue
        if modName.startswith("test"):
            continue
        retList.append(modName[0:-3])
    return retList

keyDictionaries = _getStdDictionaryNames()