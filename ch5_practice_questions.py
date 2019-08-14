# 1. What does the code for an empty dictionary look like?
# ANS: empty_dict = {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
# ANS: myDict = {'foo':42}

# 3. What is the main difference between a dictionary and a list?
# ANS: A dictionary maps a key to a value; A list simply contains a series of
# values in order (dicionaries are NOT ordered)

# 4. What happens if you try to access `spam['foo']` if `spam = {'bar':100}`?
# ANS: You will be returned with a `KeyError` because the key 'foo' is NOT in
# the dictionary

# 5. If a dictionary is stored in `spam`, what is the difference between the
# expressions 'cat' in `spam` and 'cat' in `spam.keys()`?
# ANS: 'cat' in `spam` is short for `'cat' in spam.keys()` so there is NO
# difference

# 6. If a dictionary is stored in `spam`, what is the difference between the
# expressions 'cat' in `spam` and 'cat' in `spam.values()`?
# ANS: In the first case, 'cat' would be a key; in the second case 'cat' would
# be a value

# 7. What is a shortcut for the following code?
# if 'color' not in spam:
#     spam['color'] = 'black'
# ANS: The shortcut is `spam.setdefault('color', 'black')`

# 8. What module and function can be used to "pretty print" dictionary values?
# ANS: pprint.pprint()
