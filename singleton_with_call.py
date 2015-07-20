# This is a example file of using singleton in python using __call__  and metaclass 

class Singleton(type):
    """ Singleton class"""
    _instances = {}                         # Private variable to store class instance
    def __call__(self, *args, **kwargs):
        """
           Method called when class instance is called
           Returns if already instance is available for the class.
           Else creates one instance and appends in the dictionary.
        """
        if self.__name__ not in Singleton._instances:   
            print 'Instance for class - %s' % self
            Singleton._instances[self.__name__] = type.__call__(self, *args, **kwargs)
        return Singleton._instances[self.__name__]

class myClass(object):
    __metaclass__ = Singleton
    print 'myClass called'
    pass

class ourClass(object):
    __metaclass__ = Singleton
    print 'ourClass called'
    pass

if __name__ == '__main__':
    my_inherited_1 = myClass()
    my_inherited_2 = myClass()
    our_inherited_1 = ourClass()
    our_inherited_2 = ourClass()