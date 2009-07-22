KeysDictionary("alerts", (0,4),
    Key("alert",
        String(name="alertID", help="alert ID: actor.keyword"),
        Enum('ok', 'info', 'warn', 'serious', 'critical', name="severity",
            help="The severity level of an alert; ok means the alert is over."),
        String(name="value", help="value of keyword"),
        Bool(False, True, name="enabled"),
        Bool(False, True, name="acknowledged"),
        doCache=False,
    ),
    Key("alertEnabled",
        String(name="alertID", help="alert ID: actor.keyword"),
        Enum('ok', 'info', 'warn', 'serious', 'critical', name="severity",
            help="The severity level of an alert; ok means the alert is over."),
        Bool(False, True, name="enabled"),
        help="This alert at this severity or below has been enabled or disabled.",
        doCache=False,
    ),
)