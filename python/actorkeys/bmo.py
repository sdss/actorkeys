
KeysDictionary('bmo', (0, 1), *(
    Key('bmoCamera',
        Bool('False', 'True', name='connected', help='Is the camera connected?') * (2, 2),
        String(name='deviceId', invalid='?', help='The device ID.') * (2, 2),
        help='Information about the cameras, including whether they are connected and their device IDs.',
        ),
    Key('bmoVimbaState',
        Enum('Real', 'Fake', 'None', help='The state of the Vimba controller.'),
        help='The state of the Vimba controller, declaring whether it is the real thing or the fake controller for testing.',
        ),
    Key('bmoExposureTime',
        Float(name='onAxisExpTime', units='sec', help='The exposure time for the on-axis camra'),
        Float(name='offAxisExpTime', units='sec', help='The exposure time for the off-axis camra'),
        help='The exposure time for each camera.'
        ),
    Key('bmoExposeState',
        Enum('idle', 'exposing', help='Is the camera exposing?') * (2, 2),
        help='The exposing state of each camera.',
        ),
    Key('version',
        String(help='EUPS/SVN version'))
))
