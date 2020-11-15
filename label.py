#-*- coding:utf-8 -*-

## 标签的panel
##
##
##
##
import wx




class LabelButton(wx.Button):


    def __init__(self, parent, name):
        #self.id = id
        self.name = name
        wx.Button(parent, label = 'test', pos = (0, 0), size = (100,200))
        
        pass


class LabelPanel():

    def __init__(self, parent = None):
        panel = wx.Panel(parent, -1, pos = (0, 0), size = (1200,30))
        panel.SetBackgroundColour('#FFCC66')
        


    def Add(self, newone):
        Button = 
