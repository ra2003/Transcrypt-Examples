#!/usr/bin/env python
# -*- coding: utf-8 -*-

def show_date_time():
    text = "It is "
    date_time = Date()
    elements = date_time.split(" ")
    time = elements[4].split(":")
    hour = int(time[0])
    text += elements[4] + "<br>"
    if (6<hour<11):
        text += "I would say: Good morning"
    elif (11<=hour<14):
        text += "Enjoy your lunch"
    elif (14<=hour<17):
        text += "Good afternoon"
    elif (17<=hour<22):
        text += "Good evening"
    else:
        text += "Good night"
    document.getElementById('greet').innerHTML = text