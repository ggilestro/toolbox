#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VideoCapture.py
#
#  A Linux alternative to the WIN32 VideoCapture
#  http://gilest.ro/tools/videocapture-for-linux/
#  
#  Copyright 2010 Giorgio Gilestro <giorgio@gilest.ro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


import time, opencv
from PIL import ImageFont, ImageChops
from ImageDraw import Draw
from opencv import highgui

class Device(object):
    def __init__(self, devnum=0, showVideoWindow=0):
        self.camera = highgui.cvCreateCameraCapture(devnum)
        
        #self.normalfont = ImageFont.load_default()
        #self.boldfont = ImageFont.load_default()
        #This is going to be linux specific! We might have a problem here
        self.normalfont = ImageFont.truetype('/usr/share/fonts/truetype/custom/tahoma.ttf', 12)
        self.normalfont = ImageFont.truetype('/usr/share/fonts/truetype/custom/tahomabd.ttf', 12)

        self.font = None


    def setResolution(self, x,y):
        x = float(x)
        y = float(y)
        self.resolution = (x, y)
        highgui.cvSetCaptureProperty(self.camera, highgui.CV_CAP_PROP_FRAME_WIDTH, x)
        highgui.cvSetCaptureProperty(self.camera, highgui.CV_CAP_PROP_FRAME_HEIGHT, y)
        #x,y = highgui.cvGetCaptureProperty(self.camera, highgui.CV_CAP_PROP_FRAME_WIDTH), highgui.cvGetCaptureProperty(self.camera, highgui.CV_CAP_PROP_FRAME_HEIGHT)
        #print x,y

    def getImage(self, timestamp=0, boldfont=0, textpos='bl'):
        """Returns a PIL Image instance.

        timestamp:  0 ... no timestamp (the default)
                    1 ... simple timestamp
                    2 ... timestamp with shadow
                    3 ... timestamp with outline

        boldfont:   0 ... normal font (the default)
                    1 ... bold font

        textpos:    The position of the timestamp can be specified by a string
                    containing a combination of two characters.  One character
                    must be either t or b, the other one either l, c or r.

                    t ... top
                    b ... bottom

                    l ... left
                    c ... center
                    r ... right

                    The default value is 'bl'

        """

        im = highgui.cvQueryFrame(self.camera)

        #onlyRed = False
        #if onlyRed:
        #    r,g,b = opencv.adaptors.Ipl2PIL(im).split()
        #    im = ImageChops.difference(r, g) 
        #    im = im.convert("RGB")

        #else:
        im = opencv.adaptors.Ipl2PIL(im)

        if timestamp:
            width, height = self.resolution
            textcolor = 0xffffff
            shadowcolor = 0x000000            

            text = time.asctime(time.localtime(time.time()))

            if boldfont:
                self.font = self.boldfont
            else:
                self.font = self.normalfont
            tw, th = self.font.getsize(text)
            tw -= 2
            th -= 2
            if 't' in textpos:
                y = -1
            elif 'b' in textpos:
                y = height - th - 2
            else:
                raise ValueError, "textpos must contain exactly one out of 't', 'b'"
            if 'l' in textpos:
                x = 2
            elif 'c' in textpos:
                x = (width - tw) / 2
            elif 'r' in textpos:
                x = (width - tw) - 2
            else:
                raise ValueError, "textpos must contain exactly one out of 'l', 'c', 'r'"
            draw = Draw(im)
            if timestamp == 2: # shadow
                draw.text((x+1, y), text, font=self.font, fill=shadowcolor)
                draw.text((x, y+1), text, font=self.font, fill=shadowcolor)
                draw.text((x+1, y+1), text, font=self.font, fill=shadowcolor)
            else:
                if timestamp >= 3: # thin border
                    draw.text((x-1, y), text, font=self.font, fill=shadowcolor)
                    draw.text((x+1, y), text, font=self.font, fill=shadowcolor)
                    draw.text((x, y-1), text, font=self.font, fill=shadowcolor)
                    draw.text((x, y+1), text, font=self.font, fill=shadowcolor)
                if timestamp == 4: # thick border
                    draw.text((x-1, y-1), text, font=self.font, fill=shadowcolor)
                    draw.text((x+1, y-1), text, font=self.font, fill=shadowcolor)
                    draw.text((x-1, y+1), text, font=self.font, fill=shadowcolor)
                    draw.text((x+1, y+1), text, font=self.font, fill=shadowcolor)
            draw.text((x, y), text, font=self.font, fill=textcolor)
        
        return im

    def saveSnapshot(self, filename, quality=90, **args):
        img = self.getImage(**args)
        img.save(filename, quality=quality)
