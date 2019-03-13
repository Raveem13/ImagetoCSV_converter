import wx
 
def onButton(event):
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "", 
                                      "JPG files(*.jpg)|*.jpg|PNG files(*.png)|*.png", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
    openFileDialog.ShowModal()
    print(openFileDialog.GetPath())
    openFileDialog.Destroy()
    return openFileDialog.GetFilename()
 
app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,200)
panel = wx.Panel(frame, wx.ID_ANY)
 
bmp = wx.Bitmap("images/upload_icon.png", wx.BITMAP_TYPE_ANY)
button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp,
                          size=(50, 50))
 
button.Bind(wx.EVT_BUTTON, onButton)
button.SetPosition((10,10))
 
frame.Show()
frame.Centre()
app.MainLoop()