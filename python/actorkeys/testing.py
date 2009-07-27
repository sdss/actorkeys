#from opscore.protocols.keys import *
#from opscore.protocols.types import *

KeysDictionary('testing',(1,7),
	Key('note',String(name='text',invalid='??')),
	Key('unsigned',UInt(name='value',invalid='??')),
	Key('no_name',Int(invalid='??')),
	Key('two',Float(name='value',invalid='??')*2),
	Key('two_to_four',Int(name='value',invalid='??')*(2,4)),
	Key('one_or_more',Int(name='value',invalid='??')*(1,)),
    Key('count',UInt(name='val')),
    Key('time',Double(name='time'),String(name='tai')),
    Key('helpful',
        Int(name='theInteger',help="""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation
            ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit
            esse cillum dolore eu fugiat nulla pariatur. Excepteur
            sint occaecat cupidatat non proident, sunt in culpa qui
            officia deserunt mollit anim id est laborum.
            """
        ),
        ByName('tai'),
        #ByName('theInteger'),
        #ByName('unknown'),
        Float(name='theFloats',help="""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation
            ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit
            esse cillum dolore eu fugiat nulla pariatur. Excepteur
            sint occaecat cupidatat non proident, sunt in culpa qui
            officia deserunt mollit anim id est laborum.
            """
        )*(1,),
        help = """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
        do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat. Duis aute
        irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt
        mollit anim id est laborum.
        """
    ),
    Key('axis',
        PVT(help="""
            Lorem ipsum dolor sit amet, consectetur adipisicing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation
            ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit
            esse cillum dolore eu fugiat nulla pariatur. Excepteur
            sint occaecat cupidatat non proident, sunt in culpa qui
            officia deserunt mollit anim id est laborum.
            """
        ),
        help="This demonstrates a keyword with a PVT value"
    ),
    Key('message2',
        UInt(name='source',help='Message source'),
        CompoundValueType(
            Enum('INFO','WARN','ERROR','FAIL',name='code',help='Status code'),
            String(name='text',help='Message body'),
            name = 'message',
            help = 'A tagged message'
        )
    )
)
