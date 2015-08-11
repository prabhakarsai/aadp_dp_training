# This is a example file of using singleton in python using __new__ constructor

class Singleton(object):
    """ Singleton class"""
    _instances = {}                         # Private variable to store instance
    def __new__(cls, *args, **kwargs):
        """
           Constructor method called when class instance is created
           Returns if already instance is available.
           Else creates one instance and assigns to the variable.
        """
        if cls not in cls._instances:   
            print 'Instance for cls - %s' % cls
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class myClass(Singleton):
    print 'myClass called'
    pass

class ourClass(Singleton):
    print 'ourClass called'
    pass

if __name__ == '__main__':
    singleton_1 = Singleton()
    singleton_2 = Singleton()
    my_inherited_1 = myClass()
    my_inherited_2 = myClass()
    our_inherited_1 = ourClass()
    our_inherited_2 = ourClass()