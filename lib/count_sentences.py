#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, stringVal):
     if isinstance(stringVal, str):
      self._value = stringVal
     else:
         print("The value must be a string.")


  sentences = ["This, well, is a sentence. This is too!! And so is this, I think? Woo..."]

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    sentences = self._value.replace('!', ".").replace('?','.').split('.')
    return sum(1 for sentence in sentences if sentence.strip())
    
    
    # pattern = r'[.?!]+'
    # matches = re.findall(pattern, self.value)
    # return len(matches)
