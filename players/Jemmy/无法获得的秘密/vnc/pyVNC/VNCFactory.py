import pygame
from twisted.internet import reactor
from pyVNC.RFBToGUI import RFBToGUIeightbits, RFBToGUI
from pyVNC.rfb import *
import logging
logger = logging.getLogger("pyVNC")


class VNCFactory(RFBFactory):
    """A factory for remote frame buffer connections."""

    def __init__(self, buffer, depth, fast, *args, **kwargs):
        RFBFactory.__init__(self, *args, **kwargs)
        self.buffer = buffer

        if depth == 32:
            self.protocol = RFBToGUI
        elif depth == 8:
            self.protocol = RFBToGUIeightbits
        else:
            raise ValueError("color depth not supported")

        if fast:
            self.encodings = [
                COPY_RECTANGLE_ENCODING,
                RAW_ENCODING,
            ]
        else:
            self.encodings = [
                COPY_RECTANGLE_ENCODING,
                HEXTILE_ENCODING,
                CORRE_ENCODING,
                RRE_ENCODING,
                RAW_ENCODING,
            ]

    def buildProtocol(self, addr):
        pygame.display.set_caption('pyVNC on %s:%s' % (addr.host, addr.port))
        return RFBFactory.buildProtocol(self, addr)

    def clientConnectionLost(self, connector, reason):
        logging.error("Connection lost: %r" % reason.getErrorMessage())
        logging.error("Attempting to reconnect")
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        logging.error("Could not connect to the server with reason: %r" % reason.getErrorMessage())
        reactor.stop()
