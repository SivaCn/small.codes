#! /usr/bin/python

###############################################################################
# A Program to search almost any string in the specified Directory
# and if the directory contains sub-directories, then it searches recursively
###############################################################################

""" *** String Search Script *** 
A script for searching the strings in a specified directory and its 
sub-directories.
"""

## ------ Built-in Imports ------ ##
import os
import sys
import platform
from optparse import OptionParser
## ------ Built-in Imports ------ ##

__all__ = ['Search']

__author__ = r'Siva Cn (http://www.cnsiva.com)'

## ------ Constants or Global variables ------ ##
COMPLETE_DICT = {}
EXCLUDE_LIST = [".pyc", ".pyo"]
## ------ Constants or Global variables ------ ##


class Coloured(object):
    """."""
    def __init__(self):
        """."""
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = "\033[1m"

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def infog(self, msg):
        return self.OKGREEN + msg + self.ENDC

    def info(self, msg):
        return self.OKBLUE + msg + self.ENDC

    def warn(self, msg):
        return self.WARNING + msg + self.ENDC

    def err(self, msg):
        return self.FAIL + msg + self.ENDC


class Search(object):
    """."""
    def __init__(self, string, wildcard=".py", root=None):
        """."""
        self.string = string
        self.wildcard = wildcard
        self.root_dir = root

        self.color_obj = Coloured()

    def __search(self, file_):
        """."""

        exclude_file = False
        for ex_item in EXCLUDE_LIST:
            if ex_item in file_:
                exclude_file = True
        if exclude_file:
            return

        _dict = {}
        try:
            fp = open(file_, 'r')
            line = fp.readline()
            line_no = 1
            while line:
                if self.string.lower() in line.lower():
                    _dict[line_no] = line

                line_no += 1
                line = fp.readline()

            if _dict:
                COMPLETE_DICT[file_] = _dict

                print "----"
                print '   |', "="*80 
                print '   |', "{0}\t{1}".format(self.color_obj.warn('[FILE]'), \
                                          self.color_obj.infog(
                                               self.color_obj.info(file_.replace(os.getenv("HOME"), "~"))))

                print '   |', self.color_obj.err('-'*80)
                print '   |', " OCCURENCE: {0} Time(s)".format(self.color_obj.info(str(len(_dict.keys()))))

                print '   |', self.color_obj.err('-'*80)
                print '   |', self.color_obj.err("{0}\t{1}".format('LINE NO', '| MATCHED LINE FROM THE FILE'))
                print '   |', self.color_obj.err("{0}\t{1}".format('-------', '|{0}'.format('-'*71)))

                for line in sorted(_dict.keys()):
                    found_line = _dict[line].strip()

                    start_index = found_line.lower().find(self.string.lower())
                    end_index = start_index + len(self.string)
                    found_line = found_line[:start_index] + \
                                 self.color_obj.info(found_line[start_index:end_index]) + \
                                 found_line[end_index:]

                    print '   |', " {0}\t{1} {2}".format(self.color_obj.info(str(line)), \
                                                  self.color_obj.err('|'), \
                                                  found_line)
                print '   |', self.color_obj.err('-'*80)
                print '   |', " OCCURENCE: {0} Time(s)".format(self.color_obj.info(str(len(_dict.keys()))))
                print '   |', "="*80
                print "----"

            fp.close()

        except IOError:
            print "Error read: {0}".format(file_)

    def search(self):
        """."""
        print 
        print "<"*30, "| SEARCH STARTED |", ">"*30
        print "----"
        print "   | SEARCHING FOR THE FOLLOWING DETAILS:"
        print "   | DIR: {0}".format(self.color_obj.info((self.root_dir)))
        print "   | "
        print "   | STRING: {0}".format(self.color_obj.info(self.string))
        _file_name_str = "ALL" if not self.wildcard else self.wildcard

        print "   | FILE NAME ENDS WITH: {0}".format(self.color_obj.info(_file_name_str))
        print "----"

        for r,d,f in os.walk(self.root_dir):
            for files in f:
                if self.wildcard in files:
                     self.__search(os.path.join(r, files))

        print 
        print self.color_obj.info("RESULT: SEARCH RETURNED "), \
              "[{0}]".format(len(COMPLETE_DICT.keys())), \
              self.color_obj.info(" FILES")

        print "<"*30, "| SEARCH STOPPED |", ">"*30
        print 

def usage():
    """."""
    print """\
    Usage:
        python search_in_files.py -s <search string> [-f ".py"] [-d <dir>]
          """
    sys.exit(1)

def optparser():
    """."""
    parser = OptionParser()

    parser.add_option('-s', '--string', dest="string", \
                      help='String to be searched')

    parser.add_option('-f', '--filetype', dest='filetype', \
                      help='filetype e.g., ".py"')

    parser.add_option('-d', '--directory', dest='directory', \
                      help='root directory to start searching')

    (opts, args) = parser.parse_args()

    if not opts.string:
        print "Please specify the string to be searched"
        usage()
    if not opts.filetype:
        opts.filetype = ""
    if not opts.directory:
        opts.directory = os.getenv("HOME")

    return opts

if __name__ == "__main__":
    """."""
    parsed_args = optparser()

    obj = Search(parsed_args.string, \
                 parsed_args.filetype, \
                 parsed_args.directory)
    obj.search()
