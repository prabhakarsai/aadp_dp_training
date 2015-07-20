#!/usr/bin/env python
 
class Director(object):
 
    __builder = None
 
    def setBuilder(self, builder):
        self.__builder = builder
 
    # Assembling a laptop
    def getLaptop(self):
        """
        """
        laptop = Laptop()
 
        # get the processor
        processor = self.__builder.getProcessor()
        laptop.setProcessor(processor)
 
        # get the RAM memory
        ram_memory = self.__builder.getRAMMemory()
        laptop.setRAMMemory(ram_memory)
 
        # get the Disk Memory
        disk_memory = self.__builder.getDiskMemory()
        laptop.setDiskMemory(disk_memory)

        # get the screen
        screen_size = self.__builder.getScreenSize()
        laptop.setScreenSize(screen_size)
 
        return laptop
 
# Laptop as a product
class Laptop(object):
    
    def __init__(self):
        self.__processor      = None
        self.__ram_memory     = None
        self.__disk_memory    = None
        self.__screen_size    = None
 
    def setProcessor(self, processor):
        self.__processor = processor
 
    def setRAMMemory(self, ram_memory):
        self.__ram_memory = ram_memory
 
    def setDiskMemory(self, disk_memory):
        self.__disk_memory = disk_memory
 
    def setScreenSize(self, screen_size):
        self.__screen_size = screen_size

    def specification(self):
        print "Processor   : %s" % self.__processor.speed
        print "RAM Memory  : %s" % self.__ram_memory.memory
        print "Disk Memory : %s" % self.__disk_memory.memory
        print "Screen size : %s" % self.__screen_size.size
 
 
class Builder(object):
 
    def getProcessor(self): 
        pass

    def getRAMMemory(self): 
        pass

    def getDiskMemory(self): 
        pass

    def getScreenSize(self): 
        pass
 
class toshibhaBuilder(Builder):
  
    def getProcessor(self): 
        processor = Processor()
        processor.speed = '2 GHZ' 
        return processor

    def getRAMMemory(self): 
        ram_memory = RAMMemory()
        ram_memory.memory = '4 GB'
        return ram_memory

    def getDiskMemory(self): 
        disk_memory = DiskMemory()
        disk_memory.memory = '1 TB'
        return disk_memory

    def getScreenSize(self): 
        screen_size = ScreenSize()
        screen_size.size = "14 inch"
        return screen_size
 

class Processor(object):
    speed = None
 
class RAMMemory(object):
    memory = None
 
class DiskMemory(object):
    memory = None
 
class ScreenSize(object):
    size = None

def main():
    laptopBuilder = toshibhaBuilder()
    
    director = Director()
 
    print "Toshiba"
    director.setBuilder(laptopBuilder)
    toshiba = director.getLaptop()
    toshiba.specification()
 
  
if __name__ == "__main__":
    main()