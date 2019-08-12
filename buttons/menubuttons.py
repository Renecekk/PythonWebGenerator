def newproject(self, event):
    frame = EditorFrame()
    frame.Show()
    print('New Window Opened')
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