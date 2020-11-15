#-*-coding:utf-8-*-

import sys
import os
import wx
import json

##################
# 每个标签的panel #
#                #
##################


class ContentPanel():

    def __init__(self, parent = None):


        cdr = '{"name":"aspiring", "age": 17, "hobby": ["money","power", "read"],"parames":{"a":1,"b":2}}'
        cdr = json.loads(cdr)
        self.panel = wx.Panel(parent, pos = (0, 30), size = (1200,600))
        Button = wx.Button(self.panel, label = 'test', size = (100,200))
        txt = wx.TextCtrl(self.panel,-1,str(self.panel.GetId()), style = wx.TE_READONLY | wx.BORDER_SIMPLE | wx.TE_MULTILINE | wx.HSCROLL
        ,  pos = (500, 0), size = (800,600))
        txt.SetValue(json.dumps(cdr, indent=4))
        
        boxSizer = wx.BoxSizer(wx.VERTICAL)
        boxSizer.Add(txt, flag=wx.ALL,border=15)
        self.panel.SetSizer(boxSizer)

    def SetFocus(self):
        if self.panel is not None:
            self.panel.SetFocus()


        