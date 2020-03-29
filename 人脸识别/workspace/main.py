import tensorflow as tf

hello = tf.compat.v1.constant("Hello TensorFlow!")

with  tf.Session() as sess:
    print sess.run(hello)
    print(hello.eval(session=sess))
