from nltk.corpus import words
from collections import Counter


words_list= words.words()

def encrypt_(plain, key):
  """Function that takes in a plain text phrase and a numeric key and encrypts it using caesar cipher with the shift equals to key. The plain text can be anything in english letters, function will return encrypted lowercased text with the original punctuation marks and spaces"""

  plain = plain.lower()

  encrypted_plain = ''
  key = key % 26

  for char in plain:

    if ord(char) not in range(97, 123):
      shifted_ascii = ord(char)
      encrypted_plain += chr(shifted_ascii)
      continue
    

    elif (ord(char)+key) > 122:
      steps_from_z = (122 - ord(char)) 
      steps_from_a = key  - steps_from_z - 1
      shifted_ascii = 97 + steps_from_a

    else:
      shifted_ascii = (ord(char)+ key) 
      encrypted_plain += chr(shifted_ascii)
  return encrypted_plain

def decrypt_(cipher, key):
  """Function that takes in encrypted text and numeric key which will restore the encrypted text back to its original form as long as correct key is supplied"""

  return encrypt_(cipher, -key)


def break_cipher(cipher):
  letters_count = Counter(cipher)
  del letters_count[',']
  del letters_count[' ']
  del letters_count['.']
  del letters_count[':']

  en_fingerprint = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p','g','w', 'y','b','v','k','x','j','q','z']
  possible_e = letters_count.most_common(1)[0][0]

  for letter in en_fingerprint:
    key = ord(possible_e) - ord(letter)
    decrypted_text = decrypt_(cipher, key)
    if is_english(decrypted_text):
      return decrypted_text
    return "Not English"
      

def is_english(text):
  """Helper function to find out if the given text is english text or not"""
  words = text.split()
  word_count = 0
  for word in words:
    if word in words_list:
      word_count += 1
  
  if (word_count/len(words)) > 0.5:
    return True
  else: 
    return False