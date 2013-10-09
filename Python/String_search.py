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

class Search(object):
    """."""
    def __init__(self, string, wildcard=".py", root=None):
        """."""
        self.string = string
        self.wildcard = wildcard
        self.root_dir = root

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
                print "[FILE]\t{0}\n".format(file_.replace(os.getenv("HOME"), "~"))
                print "[SEARCH STRING]\t{0} --> [Case insensitive Search...]\n".format(self.string)
                ##print '''Found "{0}"'''.format(self.string)
                for line in sorted(_dict.keys()):
                    print "[LINE] {0}\t{1}".format(line, _dict[line].strip())
                print "-"*80

            fp.close()

        except IOError:
            print "Error read: {0}".format(file_)

    def search(self):
        """."""
        print 
        print "="*80
        print "SEARCHING FOR THE FOLLOWING DETAILS:"
        print "DIR: {0}".format(self.root_dir)
        print
        print "STRING: {0}".format(self.string)
        _file_name_str = "ALL" if not self.wildcard else self.wildcard

        print "FILE NAME ENDS WITH: {0}".format(_file_name_str)
        print "="*80

        for r,d,f in os.walk(self.root_dir):
            for files in f:
                if self.wildcard in files:
                     self.__search(os.path.join(r, files))

        print 
        print "RESULT: SEARCH RETURNED [{0}] FILES".format(len(COMPLETE_DICT.keys()))
        print "="*80
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

    parser.add_option('-s', '--string', dest="string",  help='String to be searched')

    parser.add_option('-f', '--filetype', dest='filetype', help='filetype e.g., ".py"')

    parser.add_option('-d', '--directory', dest='directory', help='root directory to start searching')

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

    obj = Search(parsed_args.string, parsed_args.filetype, parsed_args.directory)
    obj.search()
