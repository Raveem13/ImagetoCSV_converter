import wx
# import time

from ocr_detector import img_csv

class Example(wx.Frame):

    def __init__(self, img_path, **kw):
        super(Example, self).__init__(img_path, **kw)
        self.img_path = img_path
        self.InitUI()
    
    def InitUI(self):
        self.count = 0 
        panel = wx.Panel(self)

        # frame.SetIcon(wx.IconFromBitmap(wx.Bitmap("images/img_con.png", wx.BITMAP_TYPE_ANY)))
        
        bmp1 = wx.Bitmap("images/upload_icon_s.png", wx.BITMAP_TYPE_ANY)
        uploadButton = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp1,
                          size=(50, 50),pos=(70, 50))
        uploadButton.Bind(wx.EVT_BUTTON, self.UploadFile)

        bmp2 = wx.Bitmap("images/download_icon_s.png", wx.BITMAP_TYPE_ANY)
        downloadButton = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp2,
                          size=(50, 50),pos=(380, 50))
        downloadButton.Bind(wx.EVT_BUTTON, self.DownloadFile)

        lblList = ['csv', 'xlsx'] 
		  
        self.rbox = wx.RadioBox(panel, label = 'Ouput Format', pos = (200,50), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS) 
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox) 

        # self.gauge = wx.Gauge(panel, range = 20, size = (200, 25), style = wx.GA_HORIZONTAL, pos=(150, 60))

        self.SetSize((500, 250))
        self.SetTitle('OCR Detector')
        self.Centre()

    # def OnStart(self, e): 
    #     while True: 
    #         time.sleep(1); 
    #         self.count = self.count + 1 
    #         self.gauge.SetValue(self.count) 
			
    #         if self.count >= 20: 
    #             print("end")
    #             return

    def UploadFile(self, e):

        # Create open file dialog
        openFileDialog = wx.FileDialog(self, "Open", "", "", 
                                      "JPG files(*.jpg)|*.jpg|PNG files(*.png)|*.png", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
        openFileDialog.ShowModal()
        # print(openFileDialog.GetPath())
        self.img_path = openFileDialog.GetPath()
        openFileDialog.Destroy()

    def onRadioBox(self,e): 
        print(self.rbox.GetStringSelection(),' is clicked from Radio Box')

    def DownloadFile(self, e):
        print("Download Button Pressed")
        # print(self.img_path)
        self.label = self.rbox.GetStringSelection()
        print(self.label)

        try:
            img_csv(self.img_path, self.label)
            print("File Converted and saved")
            wx.MessageBox('File converted and saved to local directory', 'Info', wx.OK | wx.ICON_INFORMATION)
        except:
            wx.MessageBox('Operation could not be completed', 'Error', wx.OK | wx.ICON_ERROR)

        
def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main() 