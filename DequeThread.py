from collections import deque
import logging
import threading
import time

class DequeThread(threading.Thread):
    '''
    This thread consists of a double-ended queue (deque) and runs the items
    in the deque when there are items to run.

    TODO: check python deque's add and get - see if there is any possibility of error - handle appropriately if there is
    '''

    def __init__(self):
        threading.Thread.__init__(self)

        self.q = deque()
        self.qNotEmpty = threading.Event()
        self.eventLock = threading.Lock()
        



class GatewayReaderDequeThread(DequeThread):
    '''
    The items here are UrlReaders (see FetchMetric.py).

    This class differs from the DequeThread in that, when an item fails,

    '''

    def __init__(self):
        DequeThread.__init__(self)

        self.errorThread = ErrorContainerThread(self)
        self.errorThread.start()

    def runItem(self, item):
        logging.debug('running')
        if not item.run():
            self.errorThread.addItem(item)
