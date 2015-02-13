# -*- coding: utf-8 -*-
import wx  # wx.version() == '3.0.2.0'
import choose_order


WINDOW_POS = (50, 50)
WINDOW_SIZE = (380, 123)

CARD_POOL_SIZE = 30
MAX_CARD_SIZE = 10


class MainPanel(wx.Panel):
    def __init__(self, parent, opp_first):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.SetBackgroundColour(wx.Colour(207, 230, 255))
        button_sizer = wx.GridSizer(rows=2, cols=MAX_CARD_SIZE)

        self.hand_card_amount = 3 if opp_first else 4
        self.card_pool_size = CARD_POOL_SIZE - self.hand_card_amount
        self.next_card_number = self.hand_card_amount + 1

        # self.button_panel = wx.Panel(self, -1, size=(1000, 10000))
        self.button_list = []
        for i in range(1, MAX_CARD_SIZE + 1):
            button = wx.Button(self, -1, str(i))
            button.Bind(wx.EVT_BUTTON, self.use_card)
            if i > self.hand_card_amount:
                button.Hide()
            button_sizer.Add(button, 0, wx.EXPAND | wx.ALL, 3)
            self.button_list.append(button)

        if not opp_first:
            self.add_card(u"硬币")

        self.draw_button = wx.Button(self, -1, u"抽牌")
        self.draw_button.Bind(wx.EVT_BUTTON, self.draw_card)
        button_sizer.Add(self.draw_button, 0, wx.EXPAND | wx.ALL, 3)

        button_labels = (
            (u"随从", self.add_monster),
            (u"法术", self.add_magic),
            (u"窃取", self.add_steal),
            (u"衍生", self.add_derivation),
            (u"硬币", self.add_coin),
            (u"+库", self.add_card_pool),
        )
        for label, handle in button_labels:
            button = wx.Button(self, -1, label)
            button.Bind(wx.EVT_BUTTON, handle)
            button_sizer.Add(button, 0, wx.EXPAND | wx.ALL, 3)

        self.reduce_card_pool_button = wx.Button(self, -1, u"-库")
        self.reduce_card_pool_button.Bind(wx.EVT_BUTTON, self.reduce_card_pool)
        button_sizer.Add(self.reduce_card_pool_button, 0, wx.EXPAND | wx.ALL, 3)

        self.left = wx.Button(self, -1, str(self.card_pool_size))
        self.left.Bind(wx.EVT_BUTTON, None)
        self.left.Disable()
        button_sizer.Add(self.left, 0, wx.EXPAND | wx.ALL, 3)

        self.reset_button = wx.Button(self, -1, u"重置")
        self.reset_button.Bind(wx.EVT_BUTTON, self.reset)
        button_sizer.Add(self.reset_button, 0, wx.EXPAND | wx.ALL, 3)

        self.SetSizer(button_sizer)

    def use_card(self, event):
        self.hand_card_amount -= 1
        use_button = event.GetEventObject()
        for i, button in enumerate(self.button_list):
            if use_button.GetLabelText() == button.GetLabelText():
                for j in range(i, self.hand_card_amount):
                    self.button_list[j].SetLabelText(self.button_list[j + 1].GetLabelText())
                self.button_list[self.hand_card_amount].Hide()
                break

    def change_card_pool_size(self, add):
        self.card_pool_size += add
        self.left.SetLabelText(str(self.card_pool_size))
        if self.card_pool_size == 0:
            self.draw_button.Disable()
            self.reduce_card_pool_button.Disable()
        else:
            self.draw_button.Enable()
            self.reduce_card_pool_button.Enable()

    def add_card(self, card_name):
        if self.hand_card_amount == 10:
            return
        self.button_list[self.hand_card_amount].SetLabelText(card_name)
        self.button_list[self.hand_card_amount].Show()
        self.hand_card_amount += 1

    def draw_card(self, event):
        self.change_card_pool_size(-1)
        self.add_card(str(self.next_card_number))
        self.next_card_number += 1

    def add_monster(self, event):
        self.add_card(u"随从")

    def add_magic(self, event):
        self.add_card(u"法术")

    def add_steal(self, event):
        self.add_card(u"窃取")

    def add_derivation(self, event):
        self.add_card(u"衍生")

    def add_coin(self, event):
        self.add_card(u"硬币")

    def add_card_pool(self, event):
        self.change_card_pool_size(1)

    def reduce_card_pool(self, event):
        self.change_card_pool_size(-1)

    def reset(self, event):
        self.parent.Close()
        choose_order.main()


class MainFrame(wx.Frame):
    def __init__(self, opp_first):
        wx.Frame.__init__(self, None, title=u"炉石传说-对手牌号记录器", pos=WINDOW_POS, size=WINDOW_SIZE)
        main_panel = MainPanel(self, opp_first)
        box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        box_sizer.Add(main_panel, 1, wx.EXPAND)
        self.SetSizer(box_sizer)


def main(opp_first):
    app = wx.App()
    frame = MainFrame(opp_first)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()