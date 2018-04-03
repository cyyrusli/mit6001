word = 'bob'
count = 0
word_len = len('bob')

for i in range(len(s)):
    result = s.find('bob', i, i + word_len)
    if (result > -1):
        count += 1

print ('Number of times bob occurs is: ' , count)