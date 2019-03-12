import tensorflow as tf
'''
input = [1 ,2 ,3 , 4,5]
a = tf.placeholder(dtype=tf.int32)   #placeholder > tesnor자료형을 담기위함( 보통 학습 데이터를 담음 )
y = a + 5                            #수식
sess = tf.Session()                 # Session객체 생성
print(sess.run(y , feed_dict={a : input}))  #Session에 run을 하기위한 수식을 주고 입력값으로 a(placeholder)에 input학습데이터를 지정
'''

mathScore = [ 80, 76, 96, 100, 88]
englishScore = [ 100 , 90 , 80 , 70 , 60]
a = tf.placeholder(dtype=tf.int32) #int placeholder생성
b = tf.placeholder(dtype=tf.int32) #int placeholder생성
y = (a+b) /2 #평균값 구하는 수식
sess = tf.Session()
print(sess.run(y , feed_dict={ a : mathScore , b : englishScore})) # a에는 mathScore가 할당 , b에는 englishScore가 할당되서 y수식을 수행
