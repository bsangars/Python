import tensorflow as tf 
tf.disable_eager_execution()

T, F = 1., -1.

bias= 1.

train_in =[
    [T, T, bias],
    [T, F, bias],
    [F, T, bias],
    [F, F, bias],
]
train_out = [
    [T],
    [F],
    [F],
    [F],
]

w= tf.Variable(tf.random_normal([3,1]))

# defining the activation function

def step(x):
    is_greater= tf.greater(x,0)
    as_float= tf.to_float(is_greater)
    doubled = tf.multiply(as_float,2)
    return tf.subtract(doubled,1)

output= step(tf.matmul(train_in,w))
error= tf.subtract(train_out,output)
meansquared = tf.reduce_mean(tf.square(error))

delta= tf.matmul(train_in,error, transpose_a=True)
train = tf.assign(w,tf.add(w,delta))
sess = tf.Session()
sess.run(tf.initialize_all_variables())

err, target = 1, 0
start_time, max_time = 0, 10
while err>target and start_time<max_time:
    start_time +=1
    err, _ = sess.run([meansquared,train])
    print('start_time:', start_time,'meansquared:', err)


