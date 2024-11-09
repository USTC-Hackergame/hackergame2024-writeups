import pygame
import numpy as np
from pyVNC.constants import *
from twisted.internet import reactor
from pyVNC.Screen import Screen


class Buffer:

    def __init__(self):
        self.canvas = None
        self._canvas = None
        self.protocol = None
        self.size = (None, None)
        self.area = (None, None, None, None)

    def set_protocol(self, protocol):
        self.protocol = protocol

    def set_rfb_size(self, width, height, depth=32):
        self.size = (width, height)
        self.area = (0, 0, width, height)

        self.canvas = pygame.Surface(self.size, 0, 32)

    def update_complete(self):
        pass

    def loop(self):
        pass


class ArrayBuffer(Buffer):

    def __init__(self):
        super().__init__()
        self._canvas = np.ndarray(shape=(10, 10, 3), dtype=np.uint8)
        self._screen = Screen()

    def update_complete(self):
        self._canvas = pygame.surfarray.array3d(self.canvas).swapaxes(0, 1)
        self._screen.update(self._canvas)

    def get_array(self):
        return self._canvas


class DisplayBuffer(Buffer):

    def __init__(self, include_array):
        super().__init__()
        self.include_array = include_array
        self.window = None
        self.background = None
        self.window_style = 0  # Fullscreen

    def set_rfb_size(self, width, height, depth=32):
        super().set_rfb_size(width, height, depth)

        if depth not in [32, 8]:
            raise ValueError("color depth not supported")

        pygame.mouse.set_cursor(*POINTER)
        pygame.key.set_repeat(500, 30)
        self.window = pygame.display.set_mode(self.size, self.window_style, depth)
        self.background = pygame.Surface(self.size, depth)
        self.background.fill(0)  # black

    def update_complete(self):
        if self.include_array:
            self._canvas = pygame.surfarray.array3d(self.canvas).swapaxes(0, 1)

        self.window.blit(self.canvas, (0, 0))
        pygame.display.update()

    def get_array(self):
        return self._canvas

    def loop(self, dum=None):
        no_work = self.check_events()
        reactor.callLater(no_work and 0.0050, self.loop)

    def check_events(self):
        seen_events = 0

        if self.protocol is None:
            return seen_events

        for e in pygame.event.get():
            seen_events = 1

            if e.type == QUIT:
                reactor.stop()

            if e.type == KEYDOWN:
                if e.key in MODIFIERS:
                    self.protocol.key_event(MODIFIERS[e.key], down=1)
                elif e.key in KEYMAPPINGS:
                    self.protocol.key_event(KEYMAPPINGS[e.key], down=1)
                elif e.unicode:
                    print(ord(e.unicode))
                    self.protocol.key_event(ord(e.unicode))
                else:
                    print("warning: unknown key %r" % (e))

            if e.type == KEYUP:
                if e.key in MODIFIERS:
                    self.protocol.key_event(MODIFIERS[e.key], down=0)
                if e.key in KEYMAPPINGS:
                    self.protocol.key_event(KEYMAPPINGS[e.key], down=0)

            if e.type == MOUSEMOTION:
                self.buttons = e.buttons[0] and 1
                self.buttons |= e.buttons[1] and 2
                self.buttons |= e.buttons[2] and 4
                self.protocol.pointer_event(e.pos[0], e.pos[1], self.buttons)

            if e.type == MOUSEBUTTONUP:
                if e.button == 1: self.buttons &= ~1
                if e.button == 2: self.buttons &= ~2
                if e.button == 3: self.buttons &= ~4
                if e.button == 4: self.buttons &= ~8
                if e.button == 5: self.buttons &= ~16
                self.protocol.pointer_event(e.pos[0], e.pos[1], self.buttons)

            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1: self.buttons |= 1
                if e.button == 2: self.buttons |= 2
                if e.button == 3: self.buttons |= 4
                if e.button == 4: self.buttons |= 8
                if e.button == 5: self.buttons |= 16
                self.protocol.pointer_event(e.pos[0], e.pos[1], self.buttons)

            return not seen_events
        return not seen_events

