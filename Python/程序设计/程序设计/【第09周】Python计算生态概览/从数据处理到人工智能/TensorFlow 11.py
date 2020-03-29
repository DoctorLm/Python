#TensorFlow:AlphaGo背后的机器学习计算框架
import tensorflow as tf

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
res = sess.run(result)
print('result:',res)
