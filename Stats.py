from collections import Counter


class Dict(object):
    """Contains a dictionary"""

    def __init__(self, obj=None):
        """This is the constructor"""
        self.d = {}

        if isinstance(obj, (dict, Counter)):
            self.d.update(obj.items())
        elif isinstance(obj, list):
            self.d.update(Counter(obj))

    def __str__(self):
        """Helps in pretty printing"""
        cls = self.__class__.__name__
        return '%s(%s)' % (cls, str(self.d))

    __repr__ = __str__

    def __getitem__(self, key):
        """Enables indexing on Dict objects
            Now we can do Dict[key]
        """
        return self.d.get(key, 0)

    def __setitem__(self, key, value):
        """
            Set a value to a key

        """
        self.d[key] = value

    def __delitem__(self, key):
        """
        Delete an item from the dict

        :param key:
        :return: None
        """
        del self.d[key]

    def freq(self, key):
        """
        Return frequency for a given key

        :param key:
        :return: frequency: the value corresponding to the passed key
        """
        return self.d.get(key)

    def values(self):
        """
        Returns an unsorted sequence of values, which are basically keys of the dict

        :return: sequence of values
        """
        return self.d.keys()

    def items(self):
        """
        Returns a sequence of key, value pair of dict

        :return:
        """
        return self.d.items()


class Hist(Dict):
    pass

