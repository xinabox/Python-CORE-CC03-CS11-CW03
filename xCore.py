import time
import board
import busio

class xCore:
    def __init__(self,freq=100000, sda=board.SDA, scl=board.SCL):  
        self.i2c = busio.I2C(scl, sda, frequency=freq) 

    def write_read(self, addr, reg, length):
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(addr, bytearray([reg]))
            raw = bytearray(length)
            self.i2c.readfrom_into(addr, raw, start=0, end=length)
        finally:
            self.i2c.unlock()
        return raw

    def write_bytes(self, addr, *args):
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(addr, bytes(args))
        finally:
            self.i2c.unlock()

    def write(self, addr, buf):
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(addr, buf)
        finally:
            self.i2c.unlock()

    def read(self, addr, length):
        while not self.i2c.try_lock():
            pass
        try:
            raw = bytearray(length)
            self.i2c.readfrom_into(addr, raw, start=0, end=length)
        finally:
            self.i2c.unlock()
        return raw
    
    def sleep(sleeptime):
        time.sleep(sleeptime/1000.000)
        
