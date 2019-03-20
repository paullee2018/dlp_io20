import argparse
import logging
import serial
import time
import sys
import threading
from commands import cmd_functions
from commands import CMD
from queue import Queue
from queue import Empty


class CommandDispatcher:
    cmdDict = {}
    def __init__(self, comms, queue):
        self.comms = comms
        self.queue = queue
    def register_handler(self, key, params):
        # add the new entry to the dictionary
        self.cmdDict[key]= params
    def remove_handler(self, key, params):
        if key in self.cmdDict and self.cmdDict[key]== params:
            del self.cmdDict[key]
    def execute(self, key):
        if key in self.cmdDict:
            # call the Command Handler
            self.comms.write(self.cmdDict[key])
            self.comms.flushInput()
            # place data into the queue
            serialString = serialPort.read(10)
            self.queue.put(serialString)
        else:
            # no Command Handler registered for this command
            pass


class CommsManager(threading.Thread):
    def __init__(self, queue, dispatcher):
        self.logger = logging.getLogger(__name__)
        self.dispatcher = dispatcher
        for i in range(0, CMD.MAX_CMD-1):
            self.dispatcher.register_handler(i, cmd_functions[i])
        self.queue = queue
        self.stop_event = threading.Event()
        threading.Thread.__init__ (self)

    # main thread loop
    def run(self):
        while not self.stop_event.is_set():
            try:
                if not self.queue.empty():
                    txdata = self.queue.get()
                    dispatcher.execute(txdata)
            except Empty:
                pass

    def close(self):
        self.stop_event.set()




if __name__ == "__main__" :
    # parser = argparse.ArgumentParser(description='A class to manage reading and writing from and to a serial port.')
    # parser.add_argument('--baud', '-t', type=int, default=9600, help='Baudrate of serial port [default: 9600].')
    # parser.add_argument('--src', '-s', type=int, default=0xDE, help='Source address in CommLon [default: 0xAA].')
    # parser.add_argument('--dest', '-d', type=int, default=0x91, help='Source address in CommLon [default: 0x91].')
    # parser.add_argument('--polltime', '-p', type=int, default=5, help='Poll time for transmitting [default: 5].')
    # parser.add_argument('device', help='The serial port to use (COM4, /dev/ttyUSB1 or similar).')

    # args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(__name__)

    logger.info("Test application started\n")

    serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    serialString = ""                           # Used to hold data coming over UART

    event_queue = Queue()
    tx_queue = Queue()
    dispatcher = CommandDispatcher(serialPort, event_queue)

    comms = CommsManager(tx_queue, dispatcher)
    comms.start()

    tx_queue.put(0)

    try:
        while(1):

            if not event_queue.empty():
                rxdata = event_queue.get()
                logger.debug("Received {}".format(rxdata))
                tx_queue.put(0)
            
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        logger.debug("program exiting...")
        sys.exit()
    finally:
        logger.debug("Closing comms")
        comms.close();  


