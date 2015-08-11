# This is a example file of using singleton in python using __new__ constructor

class Singleton(object):
    """ Singleton class"""
    _instances = {}                         # Private variable to store instance
    def __new__(cls, key='mainclass', *args, **kwargs):
        """
           Constructor method called when class instance is created
           Returns if already instance is available.
           Else creates one instance and assigns to the variable.
        """
        if key not in cls._instances:   
            print 'Instance for key - %s' % key
            cls._instances[key] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[key]

class myClass(Singleton):
    print 'myClass called'
    pass

class ourClass(Singleton):
    print 'ourClass called'
    pass

if __name__ == '__main__':
    singleton_1 = Singleton()
    singleton_2 = Singleton()
    my_inherited_1 = myClass(key='myclass')
    my_inherited_2 = myClass(key='myclass')
    our_inherited_1 = ourClass(key='ourclass')
    our_inherited_2 = ourClass(key='ourclass')
    my_inherited_3 = myClass(key='newclass')
    our_inherited_3 = ourClass(key='newclass')