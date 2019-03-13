import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (600, 500))

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Our First Window")
        self.frame.Show()

        return True

app = MyApp()
app.MainLoop()
