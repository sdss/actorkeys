KeysDictionary('sos', (1, 1),
               Key("text", String(help="text for humans")),
               Key("version", String(help="EUPS/SVN version")),
               Key("b1RingMove", Float(units="deg", help="measured error in b1 ring rotation")),
               Key("b2RingMove", Float(units="deg", help="measured error in b2 ring rotation")),
               Key("b1MeanOffset", Float(units="pixels", 
                                         help="measured distance between hartmann spots")),
               Key("b2MeanOffset", Float(units="pixels", 
                                         help="measured distance between hartmann spots")),
               Key("r1PistonMove", Int(units="steps", 
                                       help="piston move required to correct r1 error")),
               Key("r2PistonMove", Int(units="steps", 
                                       help="piston move required to correct r2 error")),
               Key("sp1AverageMove", 
                   Int(units="steps", 
                       help="collimator move required to best correct r1&b1 errors")),
               Key("sp2AverageMove", 
                   Int(units="steps", 
                       help="collimator move required to best correct r2&b2 errors")),
               Key("sp1Residuals", 
                   Int(units="steps", help="r1 residual error after sp1AverageMove"),
                   Float(units="deg", help="b1 residual error after sp1AverageMove"),
                   String(help="OK, or some useful error message")),
               Key("sp2Residuals", 
                   Int(units="steps", help="r2 residual error after sp2AverageMove"),
                   Float(units="deg", help="b2 residual error after sp2AverageMove"),
                   String(help="OK, or some useful error message")),
               )
