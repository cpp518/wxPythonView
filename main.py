#-*-coding:utf-8-*-

import sys
import os
import wx
import context
import label





class Frame(wx.Frame):
    def __init__(self, parent = None, id = 1):
        self.contentPanelList = []
        wx.Frame.__init__(self, parent, id, title = "wxPython Frame", pos = wx.DefaultPosition, size=(1200, 600))
        
        #创建菜单栏
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        #创建菜单栏选项
        fileMenu.Append(wx.MenuItem(fileMenu, wx.ID_OPEN, "Open"))
        fileMenu.Append(wx.MenuItem(fileMenu, wx.ID_EXIT, "Exit"))

        #将菜单栏选项添加到菜单栏
        menuBar.Append(fileMenu, "File")

        #设置菜单栏
        self.SetMenuBar(menuBar)

        #绑定消息处理函数
        self.Bind(wx.EVT_MENU, self.MenuEvent)

        #文件标签
        label.LabelPanel(self)
        pass

    def AddPanel(self):
        context.ContentPanel(self)
        self.contentPanelList.append(context.ContentPanel(self))
        

    #菜单消息处理函数
    def MenuEvent(self, event):
        id = event.GetId()
        
        if id == wx.ID_OPEN:
            #wx.MessageBox("Open a File")
            Frame.AddPanel(self)

        if id == wx.ID_EXIT:
            wx.Exit()
        pass


class HandleEvent():
    pass
    

class myWx(wx.App):

    #创建App，并设置框架
    def OnInit(self):
        mainFrame = Frame()
        self.frame = mainFrame
        self.frame.Show(True)
        return True







def main():
    app = myWx()
    app.MainLoop()

if __name__ == '__main__':
    print(123)
    main()
