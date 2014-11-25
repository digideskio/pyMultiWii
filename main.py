#!/usr/bin/env python

"""main.py: Main module to control a multicopter."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"


import serial, struct, time
import cfg, MSP



if __name__ == "__main__":

    MSP.startMulticopter()

    try:
        while True:
            start=time.time()
            MSP.getData(MSP.RC)
            elapsed = time.time()-start
            #print rc
            print MSP.rcChannels
            print str(round(elapsed,3))+" "
            
          
    except Exception,error:
        print "Error: "+str(error)
        MSP.ser.close()