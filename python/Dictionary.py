import Constant
import numpy as np


class Dictionary:
    first_name_dict = []
    middle_name_dict = []
    last_name_dict = []

    def __init__(self):
        self.__load_from_file()

    @staticmethod
    def __load_from_file():
        Dictionary.first_name_dict = np.genfromtxt(Constant.__DIR__ + Constant.FIRST_NAME_DICTIONARY_FILE, dtype=None)
        Dictionary.middle_name_dict = np.genfromtxt(Constant.__DIR__ + Constant.MIDDLE_NAME_DICTIONARY_FILE, dtype=None)
        Dictionary.last_name_dict = np.genfromtxt(Constant.__DIR__ + Constant.LAST_NAME_DICTIONARY_FILE, dtype=None)
