#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install translate


# In[19]:


import translate

def translate_text(text, src_lang, dest_lang):
  try:
    translator = translate.Translator(to_lang=dest_lang)
    result = translator.translate(text)
    return str(result)  # Convert to string for consistency
  except Exception as e:
    print(f"Translation failed: {e}")
    return "Translation error"


# In[21]:


text = input("Enter the text to translate: ")
src_lang = input("Enter the source language code (e.g., 'en' for English): ")
dest_lang = input("Enter the destination language code (e.g., 'fr' for French): ")

translation = translate_text(text, src_lang, dest_lang)
print(translation)


# In[ ]:




