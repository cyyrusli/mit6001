s = 'azcbobobegghakl'

# tracks length of biggest substring
max_len = 0

# tracks the indices at which substrings begin
i = 0
max_i = 0

while i < len(s):
    if (len(s) - i <= max_len):
        break

    cur_len = 1

    start_i = i
    while (i + 1 < len(s) and s[i] <= s[i + 1]):
        cur_len += 1
        i += 1

    if (cur_len > max_len):
        max_len = cur_len
        max_i = start_i

    i += 1

longest = s[max_i:max_i+max_len]
print ('Longest substring in alphabetical order is:', longest)