# -*- coding: utf-8 -*-
import wx  # wx.version() == '3.0.2.0'


CARD_POOL_SIZE = 30
MAX_CARD_SIZE = 10


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.Colour(207, 230, 255))
        button_sizer = wx.GridSizer(rows=2, cols=MAX_CARD_SIZE)

        self.hand_cards = 3
        self.card_pool_size = CARD_POOL_SIZE - self.hand_cards
        self.next_card_number = self.hand_cards + 1

        # self.button_panel = wx.Panel(self, -1, size=(1000, 10000))
        self.button_list = []
        for i in range(1, MAX_CARD_SIZE + 1):
            button = wx.Button(self, -1, str(i))
            button.Bind(wx.EVT_BUTTON, self.use_card)
            if i > self.hand_cards:
                button.Hide()
            button_sizer.Add(button, 0, wx.EXPAND | wx.ALL, 3)
            self.button_list.append(button)

        button_labels = (
            (u"重置", self.reset),
            (u"抽牌", self.draw_card),
            # (u"加随从", self.OnPause),
            # (u"加法术", self.OnPause),
            # (u"窃", self.OnStepForward),
            # (u"加零件", self.OnPause),
            # (u"加香蕉", self.OnPause),
            # (u"牌库+1", self.OnStepForward),
            # (u"牌库-1", self.OnStepForward),
        )
        for label, handle in button_labels:
            button = wx.Button(self, -1, label)
            button.Bind(wx.EVT_BUTTON, handle)
            button_sizer.Add(button, 0, wx.EXPAND | wx.ALL, 3)

        self.SetSizer(button_sizer)

    def use_card(self, event):
        self.hand_cards -= 1
        use_button = event.GetEventObject()
        for i, button in enumerate(self.button_list):
            if use_button.GetLabelText() == button.GetLabelText():
                for j in range(i, self.hand_cards):
                    self.button_list[j].SetLabelText(self.button_list[j + 1].GetLabelText())
                self.button_list[self.hand_cards].Hide()
                break

    def reset(self, event):
        pass

    def draw_card(self, event):
        self.card_pool_size -= 1
        self.next_card_number += 1
        # print self.card_pool
        if self.hand_cards == 10:
            return
        self.button_list[self.hand_cards].SetLabelText(str(self.next_card_number - 1))
        self.button_list[self.hand_cards].Show()
        self.hand_cards += 1
        if self.card_pool_size == 0:
            event.GetEventObject().Disable()


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=u"炉石传说-对手牌号记录器", size=(380, 123))
        main_panel = MainPanel(self)
        box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        box_sizer.Add(main_panel, 1, wx.EXPAND)
        self.SetSizer(box_sizer)


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()