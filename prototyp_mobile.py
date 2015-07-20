#!/usr/bin/env python
import copy

class AndroidMobile(object):

    _android_version  = None
    _mobile_name = None

    def clone(self):
        pass

    def getAndroidVersion(self):
        return self._android_version

    def getMobileName(self):
        return self._mobile_name

class mobile(AndroidMobile):

    def __init__(self, version, name):
        self._android_version = version
        self._mobile_name = name

    def clone(self):
        return copy.copy(self)

def main():
    new_mobile1 = mobile('5.0','Samsung')
    new_mobile2 = new_mobile1.clone()
    new_mobile2._android_version = '4.4'
    new_mobile2._mobile_name = 'Sony'
    new_mobile3 = new_mobile1.clone()
    new_mobile3._android_version = '4.2'
    new_mobile3._mobile_name = 'Motorola'
    print "Mobile Name : %s" %  new_mobile1.getMobileName()
    print "Android version : %s" % new_mobile1.getAndroidVersion()
    print "Mobile Name : %s" % new_mobile2.getMobileName()
    print "Android version : %s" % new_mobile2.getAndroidVersion()
    print "Mobile Name : %s" % new_mobile3.getMobileName()
    print "Android version : %s" % new_mobile3.getAndroidVersion()

if __name__ == "__main__":
    main()
