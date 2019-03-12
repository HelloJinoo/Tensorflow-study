import tensorflow as tf

cons1 = tf.constant(17.5)
cons2 = tf.constant(5.0)
sess = tf.Session()
#덧셈 함수
addbox = tf.add(cons1,cons2)
print(sess.run(addbox))

#뺄셈 함수
subbox = tf.subtract(cons1 , cons2)
print(sess.run(subbox))

#곱셈 함수
mulbox = tf.multiply(cons1 , cons2)
print(sess.run(mulbox))

#나눗셈 함수
divbox = tf.truediv(cons1 , cons2)
print(sess.run(divbox))

#나머지 함수
modbox = tf.mod(cons1, cons2)
print(sess.run(modbox))

#절대값 함수
absbox = tf.abs(-cons1)
print(sess.run(absbox))

#음수반환 함수
negbox = tf.negative(cons1)
print(sess.run(negbox))

#부호 함수
sigbox = tf.sign(cons1)  #양수면 1 , 0이면 0 음수면 -1
print(sess.run(sigbox))

#제곱 함수
squbox = tf.square(cons1)
print(sess.run(squbox))

#x제곱 함수
powbox = tf.pow(cons1 , 2) #pow(수 , x)  수를 x만큼 곱함
print(sess.run(powbox))

#둘중 큰값 찾는 함수
maxbox = tf.maximum(cons1,cons2)
print(sess.run(maxbox))

#둘중 작은값 찾는 함수
minbox = tf.minimum(cons1,cons2)
print(sess.run(minbox))

#지수값 함수
expbox = tf.exp(cons1)
print(sess.run(expbox))

#로그값 함수
logbox = tf.log(cons1)
print(sess.run(logbox))

#sin 함수
sinbox = tf.sin(cons1)
print(sess.run(sinbox))

#cos 함수
cosbox = tf.cos(cons1)
print(sess.run(cosbox))
