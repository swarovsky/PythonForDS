
# coding: utf-8

# In[39]:

#Tests Xrange/Map/Reduce...
a=1000
for i in xrange(10):
    a=a+1
print(a)
a=1000
for i in xrange(1,10):
    a=a+1
print(a)

print map(lambda x:x*x, xrange(1,5))
print map(lambda x:x*(x+1), xrange(1,5))

print filter(lambda x:x>10,range(1,10))

print [x for x in range(20) if x>15]

#Xrange Contains:
for i in xrange(1,5):
    print i 
#Sum 
print reduce(lambda x,y:x+y,xrange(1,5))
#Factorielle
def fact(n):
    if n<2:
                return 1
    else:
                return n*fact(n-1)
print(fact(4))
print reduce(lambda x,y:x*y, xrange(1,5))

