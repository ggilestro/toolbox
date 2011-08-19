#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       toolbox.py
#       
#       Copyright 2011 Giorgio Gilestro <giorgio@gilest.ro>
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

import os
import ConfigParser

#Some nice colors for matplotlib plotting
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


class myconfig():
    """
    Handles program configuration
    Uses ConfigParser to store and retrieve
    From gg's toolbox
    """
    def __init__(self, filename=None, temporary=False, defaultOptions=None):
        """
        filename    the name of the configuration file
        temporary   whether we are reading and storing values temporarily
        defaultOptions  a dict containing the defaultOptions
        """
        
        filename = filename or 'config.cfg'
        pDir = os.getcwd()
        if not os.access(pDir, os.W_OK): pDir = os.environ['HOME']

        self.filename = os.path.join (pDir, filename)
        self.filename_temp = '%s~' % self.filename
        
        self.config = None
        
        if defaultOptions != None: 
            self.defaultOptions = defaultOptions
        else:
            self.defaultOptions = { "option" : [0, "desc"],
                                    }
        
        self.Read(temporary)

    def New(self, filename):
        """
        """
        self.filename = filename
        self.Read()  

    def Read(self, temporary=False):
        """
        read the configuration file. Initiate one if does not exist
        
        temporary       True                Read the temporary file instead
                        False  (Default)     Read the actual file
        """

        if temporary: filename = self.filename_temp
        else: filename = self.filename        
        
        if os.path.exists(filename):
            self.config = ConfigParser.RawConfigParser()
            self.config.read(filename)   
            
        else:
            self.Save(temporary, newfile=True)

                               
    def Save(self, temporary=False, newfile=False):
        """
        """
        if temporary: filename = self.filename_temp
        else: filename = self.filename
            
        if newfile:
            self.config = ConfigParser.RawConfigParser()
            self.config.add_section('Options')
            
            for key in self.defaultOptions:
                self.config.set('Options', key, self.defaultOptions[key][0])

        with open(filename, 'wb') as configfile:
            self.config.write(configfile)
    
        if not temporary: self.Save(temporary=True)


    def SetValue(self, section, key, value):
        """
        """
        
        if not self.config.has_section(section):
            self.config.add_section(section)
        
        self.config.set(section, key, value)
        
    def GetValue(self, section, key):
        """
        get value from config file
        Does some sanity checking to return tuple, integer and strings 
        as required.
        """
        r = self.config.get(section, key)
        
        if type(r) == type(0) or type(r) == type(1.0): #native int and float
            return r
        elif type(r) == type(True): #native boolean
            return r
        elif type(r) == type(''):
            r = r.split(',')
        
        if len(r) == 2: #tuple
            r = tuple([int(i) for i in r]) # tuple
        
        elif len(r) < 2: #string or integer
            try:
                r = int(r[0]) #int as text
            except:
                r = r[0] #string
        
        if r == 'False' or r == 'True':
            r = (r == 'True') #bool
        
        return r
                

    def GetOption(self, key):
        """
        """
        return self.GetValue('Options', key)
        
class partial:
    """
    AKA curry
    This function allows calling another function upon event trigger and pass arguments to it
    
    buttonA.Bind (wx.EVT_BUTTON, partial(self.Print, 'Hello World!'))
    
    """

    def __init__(self, fun, *args, **kwargs):
        self.fun = fun
        self.pending = args[:]
        self.kwargs = kwargs.copy()

    def __call__(self, *args, **kwargs):
        if kwargs and self.kwargs:
            kw = self.kwargs.copy()
            kw.update(kwargs)
        else:
            kw = kwargs or self.kwargs

        return self.fun(*(self.pending + args), **kw)                    

def changeFileExtension(filename, ext):
    """
    Return a filename with a new extension
    
    filename        a valid filename or full path
    ext             the new extension 
    
    """
    
    if not ext.startswith('.'): ext = '.' + ext
    f,_ = os.path.splitext(filename)
    
    return f + ext


if __name__ == '__main__':
    pass

