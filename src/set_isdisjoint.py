'''
Created on Jul 7, 2014

@author: viejoemer

How to know if two sets have common values in Python?

¿Cómo saber si dos sets tienen valores comunes en Python?

isdisjoint(other)
Return True if the set has no elements in common with other. Sets are
disjoint if and only if their intersection is the empty set.
'''

#Create a set with values.
s = set([0,1,2,3,4,5,6,7,8,9])
print(s)

s2 = set([1,10])
print(s2)

s3 = set([10,11])
print(s3)

#Verify if have not common values.
r = s.isdisjoint(s2)
print(r)

#Verify if have not common values.
r = s.isdisjoint(s3)
print(r)
