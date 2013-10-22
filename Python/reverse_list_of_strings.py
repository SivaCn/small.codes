#! /usr/bin/python

##############################################################################
##
## A program to perform the following
##
## inp = ['abcd', 'efgh', 'ijkl']
##
## out = ['lkji', 'hgfe', 'ccba']
##
##############################################################################


inp = ['abcd', 'efgh', 'ijkl']
print inp


def reverse_list(inp):
    for i in xrange(len(inp) / 2):
        _temp = inp[i]
        inp[i] = inp[- (i + 1)]
        inp[- (i + 1)] = _temp
    return inp

print [''.join(reverse_list(list(ele))) for ele in reverse_list(inp)]
