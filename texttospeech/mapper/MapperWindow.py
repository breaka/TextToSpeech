import wx

class MapperWindow(wx.Frame):
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent, title=title, size=(300,200))
        self.Show(True)

app = wx.App(False)
frame = MapperWindow("TextToSpeech Mapper")
app.MainLoop()