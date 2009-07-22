KeysDictionary("alerts", (0,2),
    Key("alert",
        String(name="alertID", help="alert ID: actor.keyword"),
        Enum('info', 'warn', 'serious', 'critical', name="severity",
            help="The severity level of an alert."),
        String(name="value", help="value of keyword"),
        Bool("False", "True", name="enabled", help="Is this alert at this level enabled?"),
        doCache=False,
    ),
    Key("acknowledge",
        String(name="alertID", help="alert ID: actor.keyword"),
        Enum('info', 'warn', 'serious', 'critical', name="severity",
            help="The severity level of an alert."),
    ),
    doCache=False,
    Key("alertEnabled",
        String(name="alertID", help="alert ID: actor.keyword"),
        Enum('info', 'warn', 'serious', 'critical', name="severity",
            help="The severity level of an alert."),
        Bool("False", "True", name="enabled"),
        help="Indicates that this alert at this severity or below has been enabled or disabled.",
    ),
    doCache=False,
)
