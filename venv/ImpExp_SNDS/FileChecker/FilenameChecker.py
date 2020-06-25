# -*- coding: utf-8 -*-
"""

"""


class FilenameChecker:
    """
    ceci constitue l'unique classe de mon_package.mon_module

    :param arg: argument du constructeur
    :type arg: integer
    """

    def __init__(self, filename):
        self._filename = self._is_valid_string(filename)


    @property
    def filename(self):
        """
        filename "getter"

        :return: the _filename attributes of a FilenameChecker object
        :rtype: String
        """
        return self._filename

    def _is_valid_string(self, value):
        """
        A method used on a value to know if it is suitable to become a filename.

        :param value: A value to check.
        :return: True if check results are OK.
        :rtype: boolean
        :raises ValueError: Error raised if the value trying to be use as a filename is wrong.
        It means that the value must be a string instance and has a length greater than 0.
        """
        if (isinstance(value, str)) and (len(value) > 0):
            return True
        elif isinstance(value, str) == False:
            raise TypeError("Given value \"{0}\" doesn't matche requirements ({0})".format(value))
        elif len(value) <= 0 == False:
            raise ValueError('String "{0}" is too short'.format(value))

    def is_doted(self, string):
        """
        A method used on a string to know if it contains a dot ('.').

        :param string: A string to check.
        :return: True if check results are OK.
        :rtype: boolean
        :raises ValueError: Error raised if the string trying to be use as a filename is wrong.

                            | It means that the string param given doesn't match one of these criteria :
                            | 1 : is a string instance
                            | 2 : has a length greater than 0 and
                            | 3: contains a dot ('.')
        """
        if is_valid_string(string):
            if '.' in string:
                return True
            else:
                raise ValueError("Given string ({0}) doesn't have a dot. ".format(string))