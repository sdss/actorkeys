# Based on what the TCC knows about the perms widget
KeysDictionary('hub',(1,1),
    Key('actors', String()*(1,), help="Current actors"),
    Key('commanders', String()*(1,), help="Current commanders"),
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
    Key('users', String()*(1,), help="current human (non-hub) commanders"),
    Key('httpRoot', String()*2, help="common http info for image retrieval: host, root dir"),
)