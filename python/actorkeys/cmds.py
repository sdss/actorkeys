KeysDictionary('cmds',(1,1),
    Key('CmdDone',UInt(),help='Hub internal command sequence number'),
    Key('NewCmd',UInt(),help='Hub internal command sequence number'),
    Key('CmdTime',Double(),units='s',help='MJD UTC timestamp'),
    Key('Cmdr',String(),help='Commander name'),
    Key('CmdrMID',UInt(),help='Hub internal'),
    Key('CmdrCID',String(),help='Deprecated hub internal'),
    Key('CmdActor',String(),help="Name of actor handling command"),
    Key('CmdText',String(),help="The command text")

    Key('CmdQueued',
        UInt(name='hubID', help='Internal command sequence number. Unique within a run of the hub'),
        Double(name='cmdTime',units='s',help='MJD TAI timestamp'),
        String(name='cmdr',help='Commander name'),
        UInt(name='cmdrMID',help='The sequence number from the commander'),
        String(name='actor',help='Actor name'),
        UInt(name='actorMID',help='The sequence number assigned to the command sent to the actor'),
        String(name='cmdText',help='The command text'),
        doCache=False,
        help='Generated right before a new command is sent to an actor.')
)
