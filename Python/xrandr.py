#!/usr/bin/python

# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
import re

from copy import deepcopy
from subprocess import check_output

from pprint import pprint as pp
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]

class Xrandr(object):
    '''A Class for .'''

    def __init__(self):
        '''Initialization Block.
        '''
        self._disp = list()
        self.primary_display = None

    def __call__(self):
        '''Making instance callable.
        '''
        self.collect_displays()

        for display in self._disp:

            print display['modes']

            if display['is_primary']:
                continue

            if display['status'] == 'connected':
                cmd = "xrandr --output {} --mode {}".format(
                    display['display'],
                    display['modes'][0] if display['modes'] else ''
                )

                check_output(cmd.split())

                print cmd

                cmd = "xrandr --output {} --right-of {}".format(
                    display['display'],
                    self.primary_display
                )

                check_output(cmd.split())

                print cmd

    def __str__(self):
        '''Overridden str method implementation.
        '''
        return '''{}'''.format()

    def __repr__(self):
        '''Overridden repr method implementation.
        '''
        return '''<ClassName({})>'''.format()

    def collect_displays(self):
        '''.'''

        def sort_modes(modes_list):
            '''.'''
            modes_list = [
                (x, y)
                for x, y in
                [x_and_y.split('x') for x_and_y in modes_list]
            ]

            import pdb; pdb.set_trace() ## XXX: Remove This
            modes_list = sorted(modes_list, key=lambda tup: tup[0])

            return [
                'x'.join(x_and_y)
                for x_and_y in modes_list
            ]

        scan_modes = False

        _xrandr = check_output(['xrandr'])

        _mode_list = list()

        for line in _xrandr.splitlines()[::-1]:

            if scan_modes:
                _mode = re.findall('[0-9]+x[0-9]+', line)
                if _mode:
                    _mode_list.extend(_mode)

            if 'connected' in line:

                template = {
                    'modes': list(),
                    'display': None,
                    'status': None,
                    'is_primary': False,
                }

                if not _mode_list:
                    scan_modes = True
                else :
                    template.update(
                        {'modes': sort_modes(deepcopy(_mode_list)) if _mode_list else list()}
                    )

                    _mode_list = list()

                    scan_modes = False

                key, value = line.split()[:2]

                template.update(
                    {'display': key,
                     'status': value,
                     'is_primary': True if 'primary' in line else False,
                    }
                )

                self._disp.append(template)

        for display in self._disp:
            if display['is_primary']:
                self.primary_display = display['display']


if __name__ == '__main__':
    """This Bolck is used for Unit Test.
    """
    xrandr = Xrandr()

    xrandr()
