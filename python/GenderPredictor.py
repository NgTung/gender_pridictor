from Name import Name

import sys
import os
import tensorflow as tf
import numpy as np


class GenderPredictor:
    def __init__(self):
        pass

    @staticmethod
    def predict(predict_name):
        name = Name(predict_name)
        vector_data = name.vector
        label_size = 2  # Male and Female
        data_size = len(vector_data) - label_size

        x = tf.placeholder(tf.float32, [None, data_size], name="x")
        y = tf.placeholder(tf.float32, [None, label_size], name="y")
        W = tf.Variable(tf.zeros([data_size, label_size]), tf.float32, name="W")
        b = tf.Variable(tf.zeros([label_size]), tf.float32, name="b")

        linear_model = tf.matmul(x, W) + b
        softmax = tf.nn.softmax(linear_model)

        sess = tf.Session()
        saver = tf.train.Saver()
        saver.restore(sess, os.path.abspath("python/saved_model/softmax_model.ckpt"))

        result = sess.run(tf.argmax(softmax, 1), feed_dict={
            x: np.array([vector_data[0:data_size]]),
            y: np.array([vector_data[data_size:data_size + label_size]])
        })

        return result


def main(predict_name):
    result = GenderPredictor.predict(predict_name)
    formater = lambda s: str(s).strip('[]')  # Format list result to string

    print formater(result)


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Disable tensorflow's warning

    main(sys.argv[1])
