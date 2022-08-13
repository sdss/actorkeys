import os


observatory = os.getenv("OBSERVATORY", "APO")

# The filename is usually the same as the dictname, but in some cases
# actorkeys overrides it, for example tcc (APO) and lcotcc (LCO) have
# different filenames (tcc.py, lcotcc.py) but apply to the same actor tcc.

if observatory == "APO":
    FILENAME_OVERRIDES = {}
else:
    FILENAME_OVERRIDES = {"tcc": "lcotcc"}
