#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = 'Python Exercises, PHP exercises.'
text = text.replace(' ', ':')
text = text.replace(',', ':')
text = text.replace('.', ':')

print(text)


# In[2]:


import pandas as pd
import re

data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)
df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'[^\w\s]|XXXXX|\d+', '', x))

print(df)


# In[3]:


def find_words(string):
    pattern = re.compile(r'\b\w{4,}\b')
    words = pattern.findall(string)
    return words
string = 'This is a sample string for example purposes only'
words = find_words(string)
print(words)


# In[4]:


def find_words(string):
    pattern = re.compile(r'\b\w{3,5}\b')
    words = pattern.findall(string)
    return words
string = 'This is a sample string for example purposes only'
words = find_words(string)
print(words)


# In[5]:


import re

def remove_parenthesis(lst):
    pattern = re.compile(r'\([^)]\)')
    new_lst = [pattern.sub('', s).strip().replace('(', '').replace(')', '') for s in lst]
    return new_lst
lst = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
new_lst = remove_parenthesis(lst)
print(new_lst)


# In[6]:


import re

def remove_parenthesis(lst):
    pattern = re.compile(r'\([^)]\)')
    new_lst = [pattern.sub('', s).strip().replace('(', '').replace(')', '') for s in items]
    return items
items = ["example(.com)", "hr@fliprobo(.com)", "github(.com)", "Hello (Data Science World)","Data (Scientist)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)","",item))
items = remove_parenthesis(items)
print(items)


# In[7]:


import re

text = "ImportanceOfRegularExpressionsInPython"
result = re.findall(r'(?<=[a-z])(?=[A-Z])|[A-Z][a-z]*', text)

print(result)


# In[8]:


def insert_spaces(text):
    output = []
    for i in range(len(text)):
        if i > 0 and text[i-1].isdigit() and not text[i].isdigit():
            output.append(" ")
        output.append(text[i])
    return "".join(output)
text = "RegularExpression1IsAn2ImportantTopic3InPython"
print(insert_spaces(text)) 


# In[9]:


import re

def insert_spaces(text):

    words = re.findall('[A-Z\d][^A-Z\d]*', text)
    
    return ' '.join(words)

text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(text)
print(result)


# In[10]:


import numpy as np
import pandas as pd
url='https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df=pd.read_csv(url)

df['first_five_letters'] = df['Country'].str[:6]

print(df.head())


# In[11]:


import re

def match_string(s):
    
    pattern = r'^[a-zA-Z0-9_]+$'
    
    match = re.match(pattern, s)
    
    return bool(match)
string1 = "Hello_world123"
string2 = "Hello World"
string3 = "Hello_world"
string4 = "Hello world123"
print(match_string(string1))
print(match_string(string2))
print(match_string(string3))
print(match_string(string4))


# In[12]:


def starts_with_number(s, n):
    
    n_str = str(n)
    
    return s.startswith(n_str)


string1 = "123abc"
string2 = "456def"
string3 = "789ghi"
print(starts_with_number(string1, 123))  
print(starts_with_number(string2, 456))  
print(starts_with_number(string3, 321)) 


# In[13]:


def remove_leading_zeros(ip_address):
    components = ip_address.split('.')
    components = [str(int(c)) for c in components]
    new_ip_address = '.'.join(components)
    return new_ip_address

ip_address1 = "192.168.001.001"
ip_address2 = "010.001.010.001"
print(remove_leading_zeros(ip_address1))  
print(remove_leading_zeros(ip_address2))  


# In[14]:


import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b([A-Z][a-z]+) \d{1,2}(?:st|nd|rd|th)? \d{4}\b"

matches = re.search(pattern, text)
print(matches)


# In[15]:


import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.findall(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[16]:


String = 'The quick brown fox jumps over the lazy dog.'
Search = 'fox'
print("Original String : ", String)
print("Searched Word : ", Search)
index = String.find(Search)
print("Index of '", Search, "' : ", index)


# In[17]:


String = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
print("Original String : ", String)
print("Searched Word : ", pattern)

occurrences = []
for i in range(len(String)):
    if String[i:i+len(pattern)] == pattern:
        occurrences.append((i, i+len(pattern)-1))

for start, end in occurrences:
    print("Substring '", pattern, "' found at position",
          start, "to", end, ":", String[start:end+1])


# In[18]:


text = "hello world, hello universe"
substring = "hello"
occurrences = []
start = 0
while True:
    start = text.find(substring, start)
    if start == -1:
        break
    occurrences.append(start)
    start += len(substring)
print("Occurrences of substring:")
for i, start in enumerate(occurrences):
    print(f"{i+1}. {substring} found at position {start}")


# In[19]:


date = "2022-10-31"

year, month, day = date.split("-")

new_date = f"{day}-{month}-{year}"
print(f"Original date: {date}")
print(f"New date: {new_date}")


# In[20]:


import re

def find_decimal_numbers(text):
    pattern = re.compile(r"\b\d+\.\d{1,2}\b")
    matches = pattern.findall(text)
    return matches
text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
matches = find_decimal_numbers(text)
print(matches)


# In[21]:


text = "There are 12 apples, 15 oranges, and 7 bananas in the basket."
numbers = []
for i, word in enumerate(text.split()):
    if word.isdigit():
       numbers.append((int(word), i))
for number in numbers:
    print(f"Number: {number[0]} found at position {number[1]+1}")


# In[22]:


import re
text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
matches = re.findall(r"\d+", text)
maximum = max(map(int, matches))
print(maximum)


# In[23]:


def insert_spaces(text):
    new_text = text[0]
    for i in range(1, len(text)):
        if text[i].isupper() and text[i-1].islower():
            new_text += " "
        new_text += text[i]
    return new_text
text = "RegularExpressionIsAnImportantTopicInPython"
new_text = insert_spaces(text)
print(new_text)


# In[24]:


import re
text = "Hello world! How are you today? IHopeYouAreDoingWell. DidYouEnjoyTheWeatherYesterday?"
pattern = r"[A-Z][a-z]+"
matches = re.findall(pattern, text)
print(matches)


# In[25]:


import re
text = "Hello hello world world"
new_text = re.sub(r"\b(\w+)( \1\b)+", r"\1", text)
print(new_text)


# In[26]:


import re
text = input("Enter a string ending with an alphanumeric character: ")
if re.search(r"\w$", text):
    print("String is valid.")
else:
    print("String is invalid.")


# In[27]:


import re

text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'
hashtags = re.findall(r"#\w+", text)

print(hashtags)


# In[28]:


import re

text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

clean_text = re.sub('<U\+[\dA-F]{4}>', '', text)

print(clean_text)


# In[29]:


import re
text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."

dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
print(dates)


# In[30]:


import re

def remove_short_words(string):
    pattern = re.compile(r'\b\w{2,4}\b')
    return pattern.sub('', string)

# Example usage
text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
text_without_short_words = remove_short_words(text)
print(text_without_short_words)


# In[ ]:




