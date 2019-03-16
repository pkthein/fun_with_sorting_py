# sorting algo
# Author : Phyo Htut
  
a = [int(i) for i in input().split()]

tmp = []

#Garage-Sort Reverse-Order (O(n^2))
mx = -1
idx = 0

for i in range(0, len(a)):
  tmp.append(a[i])
  
for i in range(0, len(a)):
  mx = tmp[i]
  idx = i
  for j in range(0, len(a)):
    if tmp[j] > mx:
      mx = tmp[j]
      idx = j
  a[i] = mx
  tmp[idx] = -9999999
  
print a

'''
#Bubble-Sort In-Order (O(n^2))
for i in range(len(a) - 1, 0, -1):        # goes from left to right
  for j in range(0, i):                   # j + 1
    if a[j] > a[j + 1]:
      tmp = a[j]
      a[j] = a[j + 1]
      a[j + 1] = tmp

print a
'''


'''
#Bubble-Sort Reverse-Order (O(n^2))
for i in range(0, len(a)):
  for j in range(len(a) - 1, i, -1):      # goes from right to left
    if a[j] > a[j - 1]:                   # j - 1
      tmp = a[j]
      a[j] = a[j - 1]
      a[j - 1] = tmp
      
print a
'''

'''
#Quick-Sort In-Order (wiki pseudocode) (O(n^2))
def quicksort(a, lo, hi):
  if len(a) <= 1:
    return
  if lo < hi:
    p = partition(a, lo, hi)
    quicksort(a, lo, p - 1)
    quicksort(a, p + 1, hi)
    
def partition(a, lo, hi):
  pivot = a[hi]
  i = lo - 1
  for j in range(lo, hi):
    if a[j] < pivot:              # greater than in reverse order
      i = i + 1
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
  if a[hi] < a[i + 1]:            # greater than in reverse order
    tmp = a[i + 1]
    a[i + 1] = a[hi]
    a[hi] = tmp
  return i + 1
  
quicksort(a, 0, len(a) - 1)

print a
'''

'''
#Quick-Sort Reverse-Order
def quicksort(a, lo, hi):
  if len(a) <= 1:
    return
  if lo < hi:
    p = partition(a, lo, hi)
    quicksort(a, lo, p - 1)
    quicksort(a, p + 1, hi)
    
def partition(a, lo, hi):
  pivot = a[hi]
  i = lo - 1
  for j in range(lo, hi):
    if a[j] > pivot:              # less than in reverse-order
      i = i + 1
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
  if a[hi] > a[i + 1]:            # less than in reverse-order
    tmp = a[i + 1]
    a[i + 1] = a[hi]
    a[hi] = tmp
  return i + 1
  
quicksort(a, 0, len(a) - 1)

print a
'''

'''
#Merge-Sort In-Order (wiki pseudocode) (O(n ln n))
def mergesort(m):
  if len(m) <= 1:
    return m
  
  left = []
  right = []
  
  for i in range(len(m)):
    if i < len(m) / 2:
      left.append(m[i])
    else:
      right.append(m[i])
  
  left = mergesort(left)
  right = mergesort(right)
  
  return merge(left, right)
  
def merge(left, right):
  result = []
  
  i = 0
  j = 0
  while len(left) > i and len(right) > j:
    if left[i] <= right[j]:                 #the only part that is different fro reverse-order
      result.append(left[i])
      i = i + 1
    else:
      result.append(right[j])
      j = j + 1
      
  while i < len(left):
    result.append(left[i])
    i = i + 1
  while j < len(right):
    result.append(right[j])
    j = j + 1
  
  return result

a = mergesort(a)

print a
'''

'''
#Merge-Sort Reverse-Order
def mergesort(m):
  if len(m) <= 1:
    return m
  
  left = []
  right = []
  
  for i in range(len(m)):
    if i < len(m) / 2:
      left.append(m[i])
    else:
      right.append(m[i])
  
  left = mergesort(left)
  right = mergesort(right)
  
  return merge(left, right)
  
def merge(left, right):
  result = []
  
  i = 0
  j = 0
  while len(left) > i and len(right) > j:
    if left[i] > right[j]:                  #the only part that is different from in-order
      result.append(left[i])
      i = i + 1
    else:
      result.append(right[j])
      j = j + 1
      
  while i < len(left):
    result.append(left[i])
    i = i + 1
  while j < len(right):
    result.append(right[j])
    j = j + 1
  
  return result

a = mergesort(a)

print a
'''
