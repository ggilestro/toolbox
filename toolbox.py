#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       toolbox.py
#       
#       Copyright 2011 Giorgio Gilestro <gg@bio-ggilestr>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


colors = {   'Blue': '#0066cc',
             'Blue Marine': '#466086',
             'Bright Yellow': '#ffff00',
             'Brown': '#660000',
             'Dark Green': '#336633',
             'Dark Grey': '#333333',
             'Dark Orange': '#ff8040',
             'Dark Purple': '#663366',
             'Green': '#33cc33',
             'Grey': '#666666',
             'Light Blue': '#99ccff',
             'Light Green': '#ccff99',
             'Light Grey': '#999999',
             'Light Pink': '#ffcc99',
             'Light Yellow': '#ffff99',
             'Olive Green': '#989e67',
             'Pink': '#ff99cc',
             'Purple': '#990099',
             'Red': '#cc0033',
             'Yellow': '#ffcc00'
             }
                    


def changeFileExtension(filename, ext):
    """
    Return a filename with a new extension
    """
    if ext[0] != '.': ext = '.' + ext
    fname, old_ext = os.path.splitext(filename)
    
    return fname + ext



if __name__ == '__main__':
    pass

