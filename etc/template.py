# type: ignore

KeysDictionary(
    "XXX",
    (0, 1),
    Key("version", String(help="Actor version")),
    Key("text", String(help="Text for humans")),
    Key("schema", String(help="Schema definition")),
    Key("help", String(help="Help string")),
    Key("error", String(help="Error message")),
    Key("yourUserID", Int(help="User ID")),
    Key("UserInfo", Int(name="userID"), String(name="IP")),
    Key("num_users", Int(help="Number of users connected")),
)
