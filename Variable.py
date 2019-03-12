import tensorflow as tf
a = tf.Variable(1) #변수 선언
b = tf.Variable(2)
c = tf.multiply(a ,b) #Mul하는 그래프 생성
init = tf.global_variables_initializer()  #*변수 사용을 위해 초기화를 해줘야함!
sess = tf.Session()  #흐름 실행을 위한 Session생성
sess.run(init)      #초기화 수행 후
print(sess.run(c))   #c 실행
