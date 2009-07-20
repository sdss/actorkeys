# Based on what the TCC knows about the perms widget
KeysDictionary('hub',(1,5),
    Key('actors', String()*(0,), help="Current actors"),
    Key('commanders', String()*(0,), help="Current commanders"),
    Key('user', String()*(5,6), help=
        """Information about a user:
        - cmdrID (program.name)
        - client name (e.g. "TUI")
        - client version (sortable)
        - system info (e.g. platform.platform())
        - IP address (numeric)
        ? fully qualified domain name (if supplied)
        """,
        doCache=False,
    ),
    Key('text', String(), help="Craig's random musings", doCache=False),
    Key('users', String()*(0,), help="current human (non-hub) commanders"),
    Key('version', String(), help="Craig's random choice of version string"),
)
