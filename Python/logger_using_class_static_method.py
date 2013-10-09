#
#
# This Program was Copied from internet.
#
#


class Logger :
    ''' Handles logging of debugging and error messages. '''

    DEBUG = 5
    INFO  = 4
    WARN  = 3
    ERROR = 2
    FATAL = 1
    _level = DEBUG

    def __init__( self ) :
        Logger._level = Logger.DEBUG

    @classmethod
    def isLevel( cls, level ) :
        return cls._level >= level

    @classmethod
    def debug( cls, message ) :
        if cls.isLevel( Logger.DEBUG ) :
            print "DEBUG:  " + message

    @classmethod
    def info( cls, message ) :
        if cls.isLevel( Logger.INFO ) :
            print "INFO :  " + message

    @classmethod
    def warn( cls, message ) :
        if cls.isLevel( Logger.WARN ) :
            print "WARN :  " + message

    @classmethod
    def error( cls, message ) :
        if cls.isLevel( Logger.ERROR ) :
            print "ERROR:  " + message

    @classmethod
    def fatal( cls, message ) :
        if cls.isLevel( Logger.FATAL ) :
            print "FATAL:  " + message

def logAll() :
    Logger.debug( "This is a Debug message." )
    Logger.info ( "This is a Info  message." )
    Logger.warn ( "This is a Warn  message." )
    Logger.error( "This is a Error message." )
    Logger.fatal( "This is a Fatal message." )

if __name__ == '__main__' :

    print "Should see all DEBUG and higher"
    Logger._level = Logger.DEBUG
    logAll()

    print "Should see all ERROR and higher"
    Logger._level = Logger.ERROR
    logAll()

    print '---'
    
    Logger._level = Logger.WARN
    logAll()
