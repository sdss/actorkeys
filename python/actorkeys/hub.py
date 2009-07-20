# Based on what the TCC knows about the perms widget
KeysDictionary('hub',(1,4),
    Key('actors', String()*(0,), help="Current actors"),
    Key('commanders', String()*(0,), help="Current commanders"),
    # do NOT refresh user:
    Key('user', String()*(5,6), help=
        """Information about a user:
        - cmdrID (program.name)
        - client name (e.g. "TUI")
        - client version (sortable)
        - system info (e.g. platform.platform())
        - IP address (numeric)
        ? fully qualified domain name (if supplied)
        """,
    ),
    Key('text', String(), help="Craig's random musings"),
    Key('users', String()*(0,), help="current human (non-hub) commanders"),
    Key('version', String(), help="Craig's random choice of version string"),
)
