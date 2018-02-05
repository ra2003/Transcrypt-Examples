#!/usr/bin/env python
# -*- coding: utf-8 -*-

window = document

class TestSystem:
    
    def __init__ (self):
        self.text = 'Hello, DOM!'
        self.size = 12
        self.mult = 1
    
    def insert(self):
        document.querySelector('output').innerText = self.text

    def pressed(self):
        self.size = self.size + 2 * self.mult
        document.getElementById('textblock').style.fontSize=str(self.size)+'px'
        if self.size == 36:
            self.mult = -1
        elif self.size == 10:
            self.mult = 1
        debugstring = "self.size "+str(self.size)+" self.mult "+str(self.mult)
        console.log(debugstring)

testSystem = TestSystem()
