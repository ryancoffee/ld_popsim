#!/home/coffee/envs/tensorflow/bin/python

import numpy as np
import tensorflow as tf

file_name = './data/testing.dat'
#dataset = tf.data.Dataset.TextLineDataset([file_name])
test_dataset = tf.data.TextLineDataset([file_name])
#dataset = tf.data.Dataset.range(100)
my_iterator = test_dataset.make_one_shot_iterator()
initable_iterator = test_dataset.make_initializable_iterator()
my_next_element = my_iterator.get_next()
my_next_initable_element = initable_iterator.get_next()
sess = tf.Session()
for i in range(15):
	value = sess.run(my_next_element)
	print(value)

print("\n\n")
sess.run(initable_iterator.initializer)
#test_dataset.batch(batch_size = 2,drop_remainder=True)
for i in range(10):
	value = sess.run(my_next_initable_element)
	value2 = sess.run(my_next_element)
	print((value,value2))

with sess.as_default():
	print(tf.get_default_session())

print(tf.get_default_session()) ## None since out of scope defined as 'with sess.as_default():' context
				## Actually, the default session seems only to be switched into when in the 'with' context manager
print(sess)			## This, however, works just fine, but I still need to figure out how to run multiple sessions and move in and out of them

sess2 = tf.Session()
with sess2.as_default(): ## This sets the scope for sess2... the shoortcut way is to use: 'with tf.Session() as sess2:'
	print(tf.get_default_session())
	values = tf.data.TextLineDataset("data/values.dat")
	labels = tf.data.TextLineDataset("data/labels.dat")

	dataset = tf.data.Dataset.zip((values, labels))

	#iterator = dataset.make_initializable_iterator() ## this fails... needs to be one_shot_iterator() for get_next() it seems
	one_shot_iterator = dataset.make_one_shot_iterator()
	get_next = one_shot_iterator.get_next() ## this works
	#get_next = iterator.get_next()  ## this fails... needs to be one_shot_iterator() for get_next() it seems
	for i in range(2):
		#print(sess2.run(dataset)) ## this fails
		print(sess2.run(get_next))

devices = sess2.list_devices()
for d in devices:
	print(d.name)

##sess2.exit() ## these fail... I must be confused about __enter__ and __exit__
##sess.enter()
value = sess.run(my_next_initable_element)
value2 = sess.run(my_next_element)
print((value,value2))
##sess.exit()

sess.close()
sess2.close()

#Now try to write out a tf_record
"""
tfr_filename = './data/outputfile.tfrecords'
# open the TFRecords file
tfr_writer = tf.python_io.TFRecordWriter(tfr_filename)
"""

#

#print(dataset.output_types)
#print(sess.run(dataset.output_types))

