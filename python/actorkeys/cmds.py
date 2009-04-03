KeysDictionary('cmds',(1,0),
    Key('CmdDone',UInt(),help='Hub internal command sequence number'),
    Key('NewCmd',UInt(),help='Hub internal command sequence number'),
    Key('CmdTime',Double(),units='s',help='MJD UTC timestamp'),
    Key('Cmdr',String(),help='Commander name'),
    Key('CmdrMID',UInt(),help='Hub internal'),
    Key('CmdrCID',String(),help='Deprecated hub internal'),
    Key('CmdActor',String(),help="Name of actor handling command"),
    Key('CmdText',String(),help="The command text")
)
