# Ceasar cipher implementation

## Author: Richard Whitehead

## Challenge

Create an encrypt function that takes in a plain text phrase and a numeric shift.
the phrase will then be shifted that many letters.
E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘acb’, 10) would return ‘klm’
shifts that exceed 26 should wrap around
E.g. encrypt(‘abc’,27) would return ‘bcd’
Create a decrypt method that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form as long as correct key is supplied.
Break the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
Devise a method for the computer to determine if code was broken with minimal human guidance.

## Architecture
Python 3.7.5
Pipenv
Pytest
nltk words collection
collections.Counter


## Sources 

https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

https://www.nltk.org/data.html