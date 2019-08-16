"""
1. What are escape characters?
ANS: Escape characters such as \' and \" take away the special nature of the
' and " characters and allow them to be used as literal characters in a string

2. What do the \n and \t escape characters represent?
ANS: \n denotes a newline and \t denotes a tab

3. How can you put a \ backslash character into a string?
ANS: By using '\\'

4. The string value "Howl's Moving Castle" is a valid string. Why isn't it a
problem that the single quote character in the word `Howl's` isn't escaped?
ANS: The single quote is not an issue because double quotes are used to
capture the entire string

5. If you don't want to put \n in your string, how can you write a string with
newlines in it?
ANS: Use triple quotes (either single or double)

6. What do the following expressions evaluate to?
- 'Hello world!'[1] (evaluates to 'e')
- 'Hello world!'[0:5] (evaluates to 'Hello')
- 'Hello world!'[:5] (same as above)
- 'Hello world!'[3:] (evaluates to 'lo world!')

7. What do the following expressions evaluate to?
- 'Hello'.upper() [evaluates to 'HELLO']
- 'Hello'.upper().isupper() [evaluates to True]
- 'Hello'.upper().lower() [evaluates to 'hello']

8. What do the following expressions evaluate to?
- 'Remember, remember, the fifth of November.'.split()
- '-'.join('There can be only one.'.split())
ANS: In the first case we are returned a list with six elements:
     ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

     In the second case, we are returned a string:
     'There-can-be-only-one.'

9. What string methods can you use to right-justify, left-justify, and center
a string?
ANS: string.rjust(), string.ljust(), and string.center()

10. How can you trim whitespace characters from the beginning or end of a
string?
ANS: string.rstrip(), string.lstrip(), string.strip()
"""
