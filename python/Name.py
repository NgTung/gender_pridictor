import Constant
import numpy as np

from Dictionary import Dictionary


class Name:
    def __init__(self, name):
        self.dictionary = Dictionary()
        self.first_name, self.middle_name, self.last_name = self.__splitter(name)
        self.vector = self.__to_vector()

    def __to_vector(self):
        first_name_dict = self.dictionary.first_name_dict
        middle_name_dict = self.dictionary.middle_name_dict
        last_name_dict = self.dictionary.last_name_dict

        vector = np.array(self.vector_generator([self.first_name], first_name_dict))
        vector = np.concatenate((vector, np.array(self.vector_generator(self.middle_name, middle_name_dict))))
        vector = np.concatenate((vector, np.array(self.vector_generator([self.last_name], last_name_dict))))

        return np.concatenate((vector, Constant.FLAG_LABEL))

    @staticmethod
    def vector_generator(words, dict):
        dict_len = len(dict)
        vector = [0] * dict_len
        for word in words:
            for i in range(dict_len):
                if word.lower() == dict[i].lower():
                    vector[i] = 1
                else:
                    vector[i] = 0
        return np.array(vector)

    @staticmethod
    def __splitter(name):
        n = name.split(" ")
        first_name = n[0]
        middle_name = n[1: len(n) - 1]
        last_name = n[len(n) - 1]

        return first_name, middle_name, last_name
