"""
Controlador
"""

import glfw
import sys

from model import Tpose


class Controller(object):
    tposemodel: 'Tpose'

    def __init__(self):
        self.tposemodel = None

    def set_tpose(self, tp:'Tpose'):
        self.tposemodel = tp

    def on_key(self, window, key, scancode, action, mods):
        if action != glfw.PRESS:
            return

        if key == glfw.KEY_ESCAPE:
            sys.exit()

        elif key == glfw.KEY_F:
            self.tposemodel.toggle()

        else:
            print('Unknown key')
