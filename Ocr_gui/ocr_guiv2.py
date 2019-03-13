import wx
import time

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

        self.gauge = wx.Gauge(panel, range = 20, size = (200, 25), style = wx.GA_HORIZONTAL, pos=(150, 60))

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

    def DownloadFile(self, e):
        print("Download Button Pressed")
        # print(self.img_path)
        
        try:
            img_csv(self.img_path)
            print("File Converted and saved")
            wx.MessageBox('File Converted and saved local Directory', 'Info', wx.OK | wx.ICON_INFORMATION)
        except:
            wx.MessageBox('Operation could not be completed', 'Error', wx.OK | wx.ICON_ERROR)

        
def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main() 