#
# Definitions of PLC bit fields
#


SDSS_CSV = $(PLC_DIR)/etc/sdss.csv $(PLC_DIR)/etc/extra.csv

all:

ifdef PLC_DIR
	@make mcp.py
else
	$(info No PLC_DIR set. Are we at LCO? $(PLC_DIR))
	@exit
endif

mcp.py : mcp.py.skl $(SDSS_CSV)
	read-csv -D -s mcp.py.skl $(SDSS_CSV) > mcp.py


