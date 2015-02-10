import wx
import core


WINDOW_SIZE = (380, 123)


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"炉石传说-对手牌号记录器", size=WINDOW_SIZE)
        panel = wx.Panel(self)

        closeBtn = wx.Button(panel, label="Close")
        closeBtn.Bind(wx.EVT_BUTTON, self.on_close)

    def on_close(self, event):
        self.Close()
        core.main()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()