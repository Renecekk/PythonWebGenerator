import wx
import os

from numpy.distutils.system_info import wx_info

global xMax, yMax
frame = None
btncolor='#353535'


class App(wx.App):

    def OnInit(self):
        frame = Menu()
        frame.Show()
        self.SetTopWindow(frame)
        return True


class Menu(wx.Frame):
    def __init__(self):
        global xMax, yMax, yHalf, xHalf
        xMax, yMax = wx.GetDisplaySize()
        if xMax is 0:
            xMax = 1920

        if yMax is 0:
            yMax = 1080

        xHalf = xMax / 2
        yHalf = yMax / 2

        if xMax > 1920:
            xHalf = 1920 / 2

        if yMax > 1080:
            yHalf = 1080 / 2

        if xHalf < 600:
            xHalf = xMax
            yHalf = yMax

        if yHalf < 400:
            yHalf = yMax
            xHalf = xMax

        super().__init__(parent=None, title="Main Menu", size=(xHalf, yHalf), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER  |  wx.MAXIMIZE_BOX)
        self.SetBackgroundColour('#252525')
        panel = wx.Panel(self)

        font = wx.Font(30, wx.DEFAULT, wx.ITALIC, wx.BOLD, underline=False, faceName="Candara")

        self.newproj = wx.Button(panel, label="Create New Project", pos=(50, yHalf/7*2+20), size=(xHalf - 100, yHalf/8))
        self.newproj.SetBackgroundColour(btncolor)
        self.newproj.Bind(wx.EVT_BUTTON, self.newproject)
        self.newproj.SetFont(font)
        self.newproj.SetForegroundColour('#d024fb')
        self.newproj.SetWindowStyleFlag(wx.NO_BORDER)
        self.newproj.Bind(wx.EVT_ENTER_WINDOW, self.newprojHover)
        self.newproj.Bind(wx.EVT_LEAVE_WINDOW, self.newprojUnhover)

        self.loadproj = wx.Button(panel, label="Load Project", pos=(50, yHalf/7*3+20), size=(xHalf-100, yHalf/8))
        self.loadproj.SetBackgroundColour(btncolor)
        self.loadproj.Bind(wx.EVT_BUTTON, self.loadproject)
        self.loadproj.SetFont(font)
        self.loadproj.SetForegroundColour('#d024fb')
        self.loadproj.SetWindowStyleFlag(wx.NO_BORDER)
        self.loadproj.Bind(wx.EVT_ENTER_WINDOW, self.loadprojHover)
        self.loadproj.Bind(wx.EVT_LEAVE_WINDOW, self.loadprojUnhover)

        self.settings = wx.Button(panel, label="Settings", pos=(50, yHalf/7*4+20), size=(xHalf - 100, yHalf/8))
        self.settings.SetBackgroundColour(btncolor)
        self.settings.Bind(wx.EVT_BUTTON, self.opensettings)
        self.settings.SetFont(font)
        self.settings.SetForegroundColour('#d024fb')
        self.settings.SetWindowStyleFlag(wx.NO_BORDER)
        self.settings.Bind(wx.EVT_ENTER_WINDOW, self.settingsHover)
        self.settings.Bind(wx.EVT_LEAVE_WINDOW, self.settingsUnhover)

        self.exitbtn = wx.Button(panel, label="Quit to Desktop", pos=(50, yHalf / 7 * 5 + 20),  size=(xHalf - 100, yHalf / 8))
        self.exitbtn.SetBackgroundColour(btncolor)
        self.exitbtn.Bind(wx.EVT_BUTTON, self.closeapp)
        self.exitbtn.SetFont(font)
        self.exitbtn.SetForegroundColour('#d024fb')
        self.exitbtn.SetWindowStyleFlag(wx.NO_BORDER)
        self.exitbtn.Bind(wx.EVT_ENTER_WINDOW, self.exitbtnHover)
        self.exitbtn.Bind(wx.EVT_LEAVE_WINDOW, self.exitbtnUnhover)

        self.Center()
        self.Show()


    def newproject(self, event):
        frame = EditorFrame()
        frame.Show()
        self.Destroy()


    def loadproject(self, event):
        print("laodproject")

    def opensettings(self, event):
        print("opensettings")

    def closeapp(self, event):
        dlg = wx.MessageDialog(self, 'Do you want to close App? ', 'Confirm Exit', wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()


    def settingsHover(self, event):
        self.settings.SetBackgroundColour('#454545')
        event.Skip()

    def settingsUnhover(self, event):
        self.settings.SetBackgroundColour('#353535')
        event.Skip()

    def exitbtnHover(self, event):
        self.exitbtn.SetBackgroundColour('#454545')
        event.Skip()

    def exitbtnUnhover(self, event):
        self.exitbtn.SetBackgroundColour('#353535')
        event.Skip()

    def newprojHover(self, event):
        self.newproj.SetBackgroundColour('#454545')
        event.Skip()

    def newprojUnhover(self, event):
        self.newproj.SetBackgroundColour('#353535')
        event.Skip()

    def loadprojHover(self, event):
        self.loadproj.SetBackgroundColour('#454545')
        event.Skip()

    def loadprojUnhover(self, event):
        self.loadproj.SetBackgroundColour('#353535')
        event.Skip()


class EditorFrame(wx.Frame):

    def __init__(self):
        global xMax, yMax, yHalf, xHalf
        super().__init__(parent=None, title="Main Menu", size=(xHalf, yHalf), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER  |  wx.MAXIMIZE_BOX)
        self.SetBackgroundColour('#252525')


        self.Center()
        self.Show()


if __name__ == "__main__":
    app = App()
    app.MainLoop()
