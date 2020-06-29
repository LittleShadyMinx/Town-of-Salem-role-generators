#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jun 29, 2020 04:21:24 PM CEST  platform: Windows NT

import sys
from functools import partial
from init import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import TOSGUI_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    TOSGUI_support.set_Tk_var()
    top = Toplevel1(root)
    TOSGUI_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    TOSGUI_support.set_Tk_var()
    top = Toplevel1(w)
    TOSGUI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("769x742+492+79")
        top.minsize(120, 1)
        top.maxsize(3204, 1061)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.001, relwidth=1.007)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.labelPlayername = tk.Label(self.Frame1)
        self.labelPlayername.place(relx=0.0, rely=0.0, height=31, width=118)
        self.labelPlayername.configure(activebackground="#f9f9f9")
        self.labelPlayername.configure(activeforeground="black")
        self.labelPlayername.configure(background="#d9d9d9")
        self.labelPlayername.configure(disabledforeground="#a3a3a3")
        self.labelPlayername.configure(
            font="-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.labelPlayername.configure(foreground="#0000ff")
        self.labelPlayername.configure(highlightbackground="#d9d9d9")
        self.labelPlayername.configure(highlightcolor="black")
        self.labelPlayername.configure(text='''Player:''')

        self.labelRole = tk.Label(self.Frame1)
        self.labelRole.place(relx=-0.013, rely=0.057, height=31, width=99)
        self.labelRole.configure(activebackground="#f9f9f9")
        self.labelRole.configure(activeforeground="black")
        self.labelRole.configure(background="#d9d9d9")
        self.labelRole.configure(disabledforeground="#a3a3a3")
        self.labelRole.configure(font="-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.labelRole.configure(foreground="#0000ff")
        self.labelRole.configure(highlightbackground="#d9d9d9")
        self.labelRole.configure(highlightcolor="black")
        self.labelRole.configure(text='''Role:''')

        self.btnRoleSelect = tk.Button(self.Frame1)
        self.btnRoleSelect.place(relx=0.103, rely=0.057, height=34, width=217)
        self.btnRoleSelect.configure(activebackground="#ececec")
        self.btnRoleSelect.configure(activeforeground="#000000")
        self.btnRoleSelect.configure(background="#d9d9d9")
        self.btnRoleSelect.configure(disabledforeground="#a3a3a3")
        self.btnRoleSelect.configure(font="-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnRoleSelect.configure(foreground="#0000ff")
        self.btnRoleSelect.configure(highlightbackground="#d9d9d9")
        self.btnRoleSelect.configure(highlightcolor="black")
        self.btnRoleSelect.configure(pady="0")
        self.btnRoleSelect.configure(takefocus="0")
        self.currentrole = StringVar()
        self.btnRoleSelect.configure(textvariable=self.currentrole)
        self.btnRoleSelect.configure(command=self.openRoleSelect)

        self.btnPrevPlayer = tk.Button(self.Frame1)
        self.btnPrevPlayer.place(relx=0.0, rely=0.937, height=44, width=217)
        self.btnPrevPlayer.configure(activebackground="#ececec")
        self.btnPrevPlayer.configure(activeforeground="#000000")
        self.btnPrevPlayer.configure(background="#d9d9d9")
        self.btnPrevPlayer.configure(disabledforeground="#a3a3a3")
        self.btnPrevPlayer.configure(font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnPrevPlayer.configure(foreground="#0080ff")
        self.btnPrevPlayer.configure(command=self.prev_player)
        self.btnPrevPlayer.configure(highlightbackground="#d9d9d9")
        self.btnPrevPlayer.configure(highlightcolor="black")
        self.btnPrevPlayer.configure(pady="0")
        self.btnPrevPlayer.configure(takefocus="0")
        self.btnPrevPlayer.configure(text='''Previous Player''')

        self.btnNextPlayer = tk.Button(self.Frame1)
        self.btnNextPlayer.place(relx=0.752, rely=0.937, height=44, width=187)
        self.btnNextPlayer.configure(activebackground="#ececec")
        self.btnNextPlayer.configure(activeforeground="#000000")
        self.btnNextPlayer.configure(background="#d9d9d9")
        self.btnNextPlayer.configure(command=self.next_player)
        self.btnNextPlayer.configure(disabledforeground="#a3a3a3")
        self.btnNextPlayer.configure(font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnNextPlayer.configure(foreground="#0080ff")
        self.btnNextPlayer.configure(highlightbackground="#d9d9d9")
        self.btnNextPlayer.configure(highlightcolor="black")
        self.btnNextPlayer.configure(pady="0")
        self.btnNextPlayer.configure(takefocus="0")
        self.btnNextPlayer.configure(text='''Next Player''')

        self.playername_gui = tk.Entry(self.Frame1)
        self.playername_gui.place(relx=0.189, rely=0.0, height=40
                                  , relwidth=0.432)
        self.playername_gui.configure(background="#d9d9d9")
        self.playername_gui.configure(borderwidth="2")
        self.playername_gui.configure(cursor="arrow")
        self.playername_gui.configure(disabledforeground="#a3a3a3")
        self.playername_gui.configure(
            font="-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.playername_gui.configure(foreground="#0000ff")
        self.playername_gui.configure(highlightbackground="#d9d9d9")
        self.playername_gui.configure(highlightcolor="black")
        self.playername_gui.configure(insertbackground="black")
        self.playername_gui.configure(selectbackground="#c4c4c4")
        self.playername_gui.configure(selectforeground="black")
        self.playername_gui.configure(takefocus="0")
        self.currname = StringVar()
        self.currname.set(currentplayer.name)
        self.playername_gui.configure(textvariable=self.currname)

        self.labelPlayerNumber = tk.Label(self.Frame1)
        self.labelPlayerNumber.place(relx=0.142, rely=0.0, height=32, width=36)
        self.labelPlayerNumber.configure(activebackground="#f9f9f9")
        self.labelPlayerNumber.configure(activeforeground="black")
        self.labelPlayerNumber.configure(background="#d9d9d9")
        self.labelPlayerNumber.configure(disabledforeground="#a3a3a3")
        self.labelPlayerNumber.configure(
            font="-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.labelPlayerNumber.configure(foreground="#0000ff")
        self.labelPlayerNumber.configure(highlightbackground="#d9d9d9")
        self.labelPlayerNumber.configure(highlightcolor="black")
        self.currentid = StringVar()
        self.currentid.set(currentplayer.pid)
        self.labelPlayerNumber.configure(textvariable=self.currentid)

        self.playerSelect = tk.Frame(self.Frame1)
        self.playerSelect.place(relx=0.724, rely=0.256, relheight=0.669
                                , relwidth=0.267)
        self.playerSelect.configure(relief="groove")
        self.playerSelect.configure(background="#d9d9d9")
        self.playerSelect.configure(cursor="fleur")
        self.playerSelect.configure(highlightbackground="#d9d9d9")
        self.playerSelect.configure(highlightcolor="black")

        self.mafiaSelect = tk.Frame(self.Frame1)
        self.mafiaSelect.place(relx=0.0, rely=0.108, relheight=0.817
                               , relwidth=0.991)
        self.mafiaSelect.configure(relief="groove")
        self.mafiaSelect.configure(background="#d9d9d9")
        self.mafiaSelect.configure(cursor="fleur")
        self.mafiaSelect.configure(highlightbackground="#d9d9d9")
        self.mafiaSelect.configure(highlightcolor="black")

        self.townSelect = tk.Frame(self.Frame1)
        self.townSelect.place(relx=0.0, rely=0.108, relheight=0.818
                              , relwidth=0.991)
        self.townSelect.configure(relief="groove")
        self.townSelect.configure(background="#d9d9d9")
        self.townSelect.configure(highlightbackground="#d9d9d9")
        self.townSelect.configure(highlightcolor="black")

        self.neutralSelect = tk.Frame(self.Frame1)
        self.neutralSelect.place(relx=0.0, rely=0.108, relheight=0.817
                                 , relwidth=0.991)
        self.neutralSelect.configure(relief="groove")
        self.neutralSelect.configure(background="#d9d9d9")
        self.neutralSelect.configure(highlightbackground="#d9d9d9")
        self.neutralSelect.configure(highlightcolor="black")

        self.actionSelect = tk.Frame(self.Frame1)
        self.actionSelect.place(relx=0.0, rely=0.135, relheight=0.791
                                , relwidth=0.745)
        self.actionSelect.configure(relief="groove")
        self.actionSelect.configure(background="#d9d9d9")
        self.actionSelect.configure(highlightbackground="#d9d9d9")
        self.actionSelect.configure(highlightcolor="#00ff40")

        self.roleSelect = tk.Frame(self.Frame1)
        self.roleSelect.place(relx=0.0, rely=0.108, relheight=0.817
                              , relwidth=0.991)
        self.roleSelect.configure(relief="groove")
        self.roleSelect.configure(background="#d9d9d9")
        self.roleSelect.configure(highlightbackground="#d9d9d9")
        self.roleSelect.configure(highlightcolor="black")
        self.roleSelect.configure(takefocus="5")

        self.btnTownSelect = tk.Button(self.roleSelect)
        self.btnTownSelect.place(relx=0.065, rely=0.132, height=124, width=267)
        self.btnTownSelect.configure(activebackground="#ececec")
        self.btnTownSelect.configure(activeforeground="#000000")
        self.btnTownSelect.configure(background="#d9d9d9")
        self.btnTownSelect.configure(disabledforeground="#a3a3a3")
        self.btnTownSelect.configure(font="-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnTownSelect.configure(foreground="#0000ff")
        self.btnTownSelect.configure(highlightbackground="#d9d9d9")
        self.btnTownSelect.configure(highlightcolor="black")
        self.btnTownSelect.configure(pady="0")
        self.btnTownSelect.configure(takefocus="0")
        self.btnTownSelect.configure(text='''Town''')
        self.btnTownSelect.configure(command=self.openTownSelect)

        self.btnMafiaSelect = tk.Button(self.roleSelect)
        self.btnMafiaSelect.place(relx=0.469, rely=0.132, height=124, width=267)
        self.btnMafiaSelect.configure(activebackground="#ececec")
        self.btnMafiaSelect.configure(activeforeground="#000000")
        self.btnMafiaSelect.configure(background="#d9d9d9")
        self.btnMafiaSelect.configure(disabledforeground="#a3a3a3")
        self.btnMafiaSelect.configure(
            font="-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnMafiaSelect.configure(foreground="#0000ff")
        self.btnMafiaSelect.configure(highlightbackground="#d9d9d9")
        self.btnMafiaSelect.configure(highlightcolor="black")
        self.btnMafiaSelect.configure(pady="0")
        self.btnMafiaSelect.configure(takefocus="0")
        self.btnMafiaSelect.configure(text='''Mafia''')

        self.btnNeutralSelect = tk.Button(self.roleSelect)
        self.btnNeutralSelect.place(relx=0.065, rely=0.412, height=124
                                    , width=267)
        self.btnNeutralSelect.configure(activebackground="#ececec")
        self.btnNeutralSelect.configure(activeforeground="#000000")
        self.btnNeutralSelect.configure(background="#d9d9d9")
        self.btnNeutralSelect.configure(disabledforeground="#a3a3a3")
        self.btnNeutralSelect.configure(
            font="-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnNeutralSelect.configure(foreground="#0000ff")
        self.btnNeutralSelect.configure(highlightbackground="#d9d9d9")
        self.btnNeutralSelect.configure(highlightcolor="black")
        self.btnNeutralSelect.configure(pady="0")
        self.btnNeutralSelect.configure(takefocus="0")
        self.btnNeutralSelect.configure(text='''Neutral''')

        self.btnCovenSelect = tk.Button(self.roleSelect)
        self.btnCovenSelect.place(relx=0.469, rely=0.412, height=124, width=267)
        self.btnCovenSelect.configure(activebackground="#ececec")
        self.btnCovenSelect.configure(activeforeground="#000000")
        self.btnCovenSelect.configure(background="#d9d9d9")
        self.btnCovenSelect.configure(cursor="fleur")
        self.btnCovenSelect.configure(disabledforeground="#a3a3a3")
        self.btnCovenSelect.configure(
            font="-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnCovenSelect.configure(foreground="#0000ff")
        self.btnCovenSelect.configure(highlightbackground="#d9d9d9")
        self.btnCovenSelect.configure(highlightcolor="black")
        self.btnCovenSelect.configure(pady="0")
        self.btnCovenSelect.configure(takefocus="0")
        self.btnCovenSelect.configure(text='''Coven-WIP''')

        self.btnPlayersActions = tk.Button(self.Frame1)
        self.btnPlayersActions.place(relx=0.336, rely=0.937, height=44
                                     , width=267)
        self.btnPlayersActions.configure(activebackground="#ececec")
        self.btnPlayersActions.configure(activeforeground="#000000")
        self.btnPlayersActions.configure(background="#d9d9d9")
        self.btnPlayersActions.configure(disabledforeground="#a3a3a3")
        self.btnPlayersActions.configure(
            font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnPlayersActions.configure(foreground="#0080ff")
        self.btnPlayersActions.configure(highlightbackground="#d9d9d9")
        self.btnPlayersActions.configure(highlightcolor="black")
        self.btnPlayersActions.configure(pady="0")
        self.btnPlayersActions.configure(takefocus="0")
        self.btnPlayersActions.configure(text='''Players and Actions''')
        self.btnPlayersActions.configure(command=self.openPlayerActions)
        row = 1
        col = 0
        self.labelInvestigative = tk.Label(self.townSelect)
        self.labelInvestigative.configure(
            font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0", foreground="#0080ff",
            background="#d9d9d9", text="Investigative")
        self.labelInvestigative.grid(row=0, column=0)
        for button in make_buttons(self.townSelect, ["Sheriff", "Investigator", "Spy", "Lookout"], self):
            button.grid(row=row)
            button.configure(width=11, command=lambda role=button["text"]: self.set_role(role))
            row += 1

    def openPlayerActions(self):
        self.actionSelect.lift()
        self.playerSelect.lift()
        self.roleSelect.lower()

    def openRoleSelect(self):
        self.roleSelect.lift()

    def openTownSelect(self):
        self.townSelect.lift()

    def next_player(self):
        global currentplayer
        index = currentplayer.pid
        currentplayer.name = self.currname.get()
        if index >= 15:
            index = 0
        currentplayer = players[index]
        self.currentid.set(currentplayer.pid)
        self.currname.set(currentplayer.name)

    def prev_player(self):
        global currentplayer
        currentplayer.name = self.currname.get()
        index = currentplayer.pid
        currentplayer = players[index - 2]
        self.currentid.set(currentplayer.pid)
        self.currname.set(currentplayer.name)

    def set_role(self, role):
        global currentplayer
        currentplayer.role = Role(role)
        self.currentrole.set(currentplayer.role.name)


if __name__ == '__main__':
    vp_start_gui()
