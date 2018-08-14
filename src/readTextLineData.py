#!/home/coffee/envs/tensorflow/bin/python

import numpy as np
import tensorflow as tf

file_name = './data/testing.dat'
#dataset = tf.data.Dataset.TextLineDataset([file_name])
my_dataset = tf.data.TextLineDataset([file_name])
#dataset = tf.data.Dataset.range(100)
my_iterator = my_dataset.make_one_shot_iterator()
my_next_element = my_iterator.get_next()
sess = tf.Session()
for i in range(100):
	value = sess.run(my_next_element)
	print(value)


#

#print(dataset.output_types)
#print(sess.run(dataset.output_types))

