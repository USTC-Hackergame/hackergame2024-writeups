from threading import Thread
from twisted.internet import reactor, task
import pygame
import time
from pyVNC import constants
from pyVNC.Buffer import DisplayBuffer, ArrayBuffer
from pyVNC.VNCFactory import VNCFactory
import logging
logger = logging.getLogger("pyVNC")

class Client(Thread):
    def __init__(self, host="127.0.0.1", password=None, port=5902, depth=32, fast=False, shared=True, gui=False, array=False, callbacks=[]):
        Thread.__init__(self)
        pygame.init()
        self.has_gui = gui
        self.screen = DisplayBuffer(array) if gui else ArrayBuffer()
        self.host = host
        self.password = password
        self.port = port
        self.depth = depth
        self.fast = fast
        self.shared = shared
        self.callbacks = callbacks
    
    def send_line(self, line):
        for c in line:
            self.send_key(c if c != '\n' else constants.K_RETURN)
        self.send_key(constants.K_RETURN)

    def send_key(self, key, duration=0.001):
        if key in constants.MODIFIERS:
            self.screen.protocol.key_event(constants.MODIFIERS[key], down=1)
        elif key in constants.KEYMAPPINGS:
            self.screen.protocol.key_event(constants.KEYMAPPINGS[key], down=1)
        elif type(key) == str:
            self.screen.protocol.key_event(ord(key), down=1)

        time.sleep(duration)

        if key in constants.MODIFIERS:
            self.screen.protocol.key_event(constants.MODIFIERS[key], down=0)
        elif key in constants.KEYMAPPINGS:
            self.screen.protocol.key_event(constants.KEYMAPPINGS[key], down=0)
        elif type(key) == str:
            self.screen.protocol.key_event(ord(key), down=0)

    def send_press(self, key):
        if key in constants.MODIFIERS:
            self.screen.protocol.key_event(constants.MODIFIERS[key], down=1)
        elif key in constants.KEYMAPPINGS:
            self.screen.protocol.key_event(constants.KEYMAPPINGS[key], down=1)
        elif type(key) == str:
            self.screen.protocol.key_event(ord(key), down=1)

    def send_release(self, key):
        if key in constants.MODIFIERS:
            self.screen.protocol.key_event(constants.MODIFIERS[key], down=0)
        elif key in constants.KEYMAPPINGS:
            self.screen.protocol.key_event(constants.KEYMAPPINGS[key], down=0)
        elif type(key) == str:
            self.screen.protocol.key_event(ord(key), down=0)

    def send_mouse(self, event="Left", position=(0, 0)):
        # Left 1, Middle 2, Right 3,
        button_id = None
        if event is "Left":
            button_id = 1
        elif event is "Middle":
            button_id = 2
        elif event is "Right":
            button_id = 4

        self.screen.protocol.pointer_event(position[0], position[1], 0)
        self.screen.protocol.pointer_event(position[0], position[1], button_id)

    def add_callback(self, interval, cb):
        l = task.LoopingCall(cb)
        l.start(interval)


    def run_block(self):
        reactor.connectTCP(
            self.host,  # remote hostname
            self.port,  # TCP port number
            VNCFactory(
                self.screen,  # the application/display
                self.depth,  # color depth
                self.fast,  # if a fast connection is used
                self.password,  # password or none
                int(self.shared),  # shared session flag
            )
        )

        # Create callbacks
        for cb_pair in self.callbacks:
            try:
                fps, cb = cb_pair
                interval = fps / 1000
                self.add_callback(interval, cb)

            except:
                logger.error("Callbacks must be formed as (fps, callback_fn)")


        # run the application
        reactor.callLater(0.1, self.screen.loop)
        reactor.run(installSignalHandlers=False)

    def run(self):
        self.run_block()
