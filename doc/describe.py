#!/usr/bin/env python
"""
Describe keywords using their dictionary metadata.

Refer to https://trac.sdss3.org/wiki/Ops/KeysDictionary for details.
"""

if __name__ == '__main__':
    
    import sys
    from optparse import OptionParser
    
    theParser = OptionParser()
    theParser.add_option(
        '--actor',action='store',help='actor name to describe'
    )
    theParser.add_option(
        '--keyword',action='store',help='keyword name to describe'
    )
    theParser.add_option(
        '--totext',action='store',help='describe as plain text to FILE',metavar='FILE'
    )
    theParser.add_option(
        '--tohtml',action='store',help='describe in HTML format to FILE',metavar='FILE'
    )
    theParser.add_option(
        '--css',action='store',help='cascading style sheet to use for HTML output'
    )
    theParser.add_option(
        '--js',action='store',help='javascript library to use for HTML output'
    )
    theParser.set_defaults(css='describe.css')
    (options, args) = theParser.parse_args()
    # decode target options
    import opscore.protocols.keys as protoKeys
    if not options.actor:
        sys.stderr.write('Must specify an actor to describe\n')
        sys.exit(-1)
    try:
        kdict = protoKeys.KeysDictionary.load(options.actor)
    except protoKeys.KeysDictionaryError:
        sys.stderr.write('No such actor: %s\n' % options.actor)
        sys.exit(-1)
    if options.keyword:
        if options.keyword in kdict:
            target = kdict[options.keyword]
            title = '%s.%s' % (options.actor,target.name)
        else:
            sys.stderr.write('No such keyword: %s.%s\n' % (options.actor,options.keyword))
            sys.exit(-1)
    else:
        title = options.actor
        target = kdict
    # decode output file options
    if(options.tohtml and options.totext):
        sys.stderr.write('Only one of --tohtml and --totext can be specified\n')
        sys.exit(-1)
    if(options.tohtml):
        format = 'html'
        outfile = open(options.tohtml,'w')
    else:
        format = 'text'
        if options.totext:
            outfile = open(options.totext,'w')
        else:
            outfile = sys.stdout
    # describe the target
    if format == 'text':
        outfile.write(target.describe())
    else:
        import opscore.utility.html as html
        content = html.HTMLDocument(
            html.Head(title=title,css=options.css,js=options.js),
            target.describeAsHTML()
        )
        outfile.write(str(content))
    # close the output file
    if outfile is not sys.stdout:
        outfile.close()
