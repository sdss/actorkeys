# Based on what the TCC knows about the perms widget
KeysDictionary('perms',(1,1),
    Key('actors', String()*(1,), help="Actors controlled by perms"),
    # do not refresh authList
    Key('authList', String()*(1,), help="Program and 0 or more authorized actors"),
    Key('lockedActors', String()*(1,), help="Actors locked out by APO"),
    Key('programs', String()*(1,), help="Programs registered with perms"),
)
