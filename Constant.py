import tensorflow as tf
a = tf.constant(1) #Tensor자료형 상수 선언
b = tf.constant(2)
ad = tf.add(a, b) #add
sess = tf.Session() #하나의 흐름 실행을 위한 session생성
print(sess.run(ad))  #session으로 run