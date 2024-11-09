import pygame
from pygame.locals import *
from pyVNC import rfb


POINTER = tuple([(8, 8), (4, 4)] + list(pygame.cursors.compile((
    # 01234567
    "        ",  # 0
    "        ",  # 1
    "        ",  # 2
    "   .X.  ",  # 3
    "   X.X  ",  # 4
    "   .X.  ",  # 5
    "        ",  # 6
    "        ",  # 7
), 'X', '.')))

# keyboard mappings pygame -> vnc
KEYMAPPINGS = {
    K_BACKSPACE: rfb.KEY_BackSpace,
    K_TAB: rfb.KEY_Tab,
    K_RETURN: rfb.KEY_Return,
    K_ESCAPE: rfb.KEY_Escape,
    K_KP0: rfb.KEY_KP_0,
    K_KP1: rfb.KEY_KP_1,
    K_KP2: rfb.KEY_KP_2,
    K_KP3: rfb.KEY_KP_3,
    K_KP4: rfb.KEY_KP_4,
    K_KP5: rfb.KEY_KP_5,
    K_KP6: rfb.KEY_KP_6,
    K_KP7: rfb.KEY_KP_7,
    K_KP8: rfb.KEY_KP_8,
    K_KP9: rfb.KEY_KP_9,
    K_KP_ENTER: rfb.KEY_KP_Enter,
    K_UP: rfb.KEY_Up,
    K_DOWN: rfb.KEY_Down,
    K_RIGHT: rfb.KEY_Right,
    K_LEFT: rfb.KEY_Left,
    K_INSERT: rfb.KEY_Insert,
    K_DELETE: rfb.KEY_Delete,
    K_HOME: rfb.KEY_Home,
    K_END: rfb.KEY_End,
    K_PAGEUP: rfb.KEY_PageUp,
    K_PAGEDOWN: rfb.KEY_PageDown,
    K_F1: rfb.KEY_F1,
    K_F2: rfb.KEY_F2,
    K_F3: rfb.KEY_F3,
    K_F4: rfb.KEY_F4,
    K_F5: rfb.KEY_F5,
    K_F6: rfb.KEY_F6,
    K_F7: rfb.KEY_F7,
    K_F8: rfb.KEY_F8,
    K_F9: rfb.KEY_F9,
    K_F10: rfb.KEY_F10,
    K_F11: rfb.KEY_F11,
    K_F12: rfb.KEY_F12,
    K_F13: rfb.KEY_F13,
    K_F14: rfb.KEY_F14,
    K_F15: rfb.KEY_F15,
}

MODIFIERS = {
    K_NUMLOCK: rfb.KEY_Num_Lock,
    K_CAPSLOCK: rfb.KEY_Caps_Lock,
    K_SCROLLOCK: rfb.KEY_Scroll_Lock,
    K_RSHIFT: rfb.KEY_ShiftRight,
    K_LSHIFT: rfb.KEY_ShiftLeft,
    K_RCTRL: rfb.KEY_ControlRight,
    K_LCTRL: rfb.KEY_ControlLeft,
    K_RALT: rfb.KEY_AltRight,
    K_LALT: rfb.KEY_AltLeft,
    K_RMETA: rfb.KEY_MetaRight,
    K_LMETA: rfb.KEY_MetaLeft,
    K_LSUPER: rfb.KEY_Super_L,
    K_RSUPER: rfb.KEY_Super_R,
    K_MODE: rfb.KEY_Hyper_R,  # ???
    # ~ K_HELP:             rfb.
    # ~ K_PRINT:            rfb.
    K_SYSREQ: rfb.KEY_Sys_Req,
    K_BREAK: rfb.KEY_Pause,  # ???
    K_MENU: rfb.KEY_Hyper_L,  # ???
    # ~ K_POWER:            rfb.
    # ~ K_EURO:             rfb.
}