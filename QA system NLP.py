#!/usr/bin/env python
# coding: utf-8

# ## Dependencies

# In[1]:


import nltk
import pandas as pd
import PyPDF2
import tabula
import textract
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)


# ## Data

# In[4]:


open_filename_WS = open(r"C:\Users\Asus\Downloads\Witness Statement Pack.pdf", 'rb')
open_filename_DB = open(r"C:\Users\Asus\Downloads\Digital Bundle.pdf", 'rb')
open_filename_ET = open(r"C:\Users\Asus\Downloads\ET unmarked.pdf", 'rb')

WS = PyPDF2.PdfFileReader(open_filename_WS)

DB = PyPDF2.PdfFileReader(open_filename_DB)

ET = PyPDF2.PdfFileReader(open_filename_ET)
#print (open_filename)


# In[7]:


WS.getDocumentInfo()


# In[9]:


DB.getDocumentInfo()


# In[10]:


ET.getDocumentInfo()


# In[12]:


total_pages_WS = WS.numPages
print(total_pages_WS)

total_pages_DB = DB.numPages
print(total_pages_DB)

total_pages_ET = ET.numPages
print(total_pages_ET)


# In[16]:


count_WS = 0
text_WS  = ''

# Lets loop through, to read each page from the pdf file
while(count_WS < total_pages_WS):
    # Get the specified number of pages in the document
    mani_pageWS  = WS.getPage(count_WS)
    # Process the next page
    count_WS += 1
    # Extract the text from the page
    text_WS += mani_pageWS.extractText()
print(text_WS)


# In[18]:


count_DB = 0
text_DB  = ''

# Lets loop through, to read each page from the pdf file
while(count_DB < total_pages_DB):
    # Get the specified number of pages in the document
    mani_pageDB  = DB.getPage(count_DB)
    # Process the next page
    count_DB += 1
    # Extract the text from the page
    text_DB += mani_pageDB.extractText()
print(text_DB)


# In[19]:


count_ET = 0
text_ET  = ''

# Lets loop through, to read each page from the pdf file
while(count_ET < total_pages_ET):
    # Get the specified number of pages in the document
    mani_pageET  = ET.getPage(count_ET)
    # Process the next page
    count_ET += 1
    # Extract the text from the page
    text_ET += mani_pageET.extractText()
print(text_ET)


# In[20]:


nltk.download('punkt')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




