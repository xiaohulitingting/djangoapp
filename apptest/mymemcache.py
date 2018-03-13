from pymemcache.client.base import Client
class MemcachedClient():
    def __init__(self):
        #self.__mc = memcache.Client(hostList)
        self.__mc = Client(('localhost', 11211))
    def set(self, key, value):
        result = self.__mc.set(key, value)
        return result
    def set_timeout(self, key, value,timeout):
        result = self.__mc.set(key, value,timeout)
        return result
    def get(self, key):
        name = self.__mc.get(key)
        return name
    def delete(self, key):
        result = self.__mc.delete(key)
        return result

