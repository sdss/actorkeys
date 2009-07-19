#
# Definitions of PLC bit fields
#
SDSS_CSV = $(PLC_DIR)/etc/sdss.csv $(PLC_DIR)/etc/extra.csv

all : mcp.py

mcp.py : mcp.py.skl $(SDSS_CSV)
	read-csv -D -s mcp.py.skl $(SDSS_CSV) > mcp.py
