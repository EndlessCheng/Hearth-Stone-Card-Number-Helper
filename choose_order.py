# -*- coding: utf-8 -*-
import wx  # wx.version() == '3.0.2.0'
import core


WINDOW_POS = (50, 50)
WINDOW_SIZE = (450, 123)


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"炉石传说-对手牌号记录器 制作: Σndless", pos=WINDOW_POS, size=WINDOW_SIZE)
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(207, 230, 255))

        button_sizer = wx.GridSizer(rows=1, cols=2)

        i_first_button = wx.Button(panel, -1, u"我先手")
        i_first_button.Bind(wx.EVT_BUTTON, self.first)
        button_sizer.Add(i_first_button, 0, wx.EXPAND | wx.ALL, 3)

        i_second_button = wx.Button(panel, -1, u"我后手")
        i_second_button.Bind(wx.EVT_BUTTON, self.second)
        button_sizer.Add(i_second_button, 0, wx.EXPAND | wx.ALL, 3)

        panel.SetSizer(button_sizer)

    def first(self, event):
        self.Close()
        core.main(False)

    def second(self, event):
        self.Close()
        core.main(True)


def main():
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()