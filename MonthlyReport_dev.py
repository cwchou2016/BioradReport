#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pd.__version__


# In[3]:


try:
    df = pd.read_xml("p:/PrintOut_StatReportForExport.xml", xpath="//IHComTable")
except:
    df = pd.read_xml("PrintOut_StatReportForExport.xml", xpath="//IHComTable")


# In[4]:


# qc only
qc_df = df[df['SampleBarcode'].str.contains("QC")]
qc_df = qc_df.copy()
qc_df['BGText'] = qc_df['BGText'].fillna("")
qc_df['BGTextABScrDAT'] = qc_df['BGTextABScrDAT'].fillna("")
# remove not interpretable
qc_df = qc_df[~(qc_df['BGText'].str.contains("not"))]
qc_df = qc_df[~(qc_df['BGTextABScrDAT'].str.contains("not"))]


# In[5]:


group = qc_df.groupby(['SampleBarcode','TestDate'])


# In[6]:


sample_df_list=[]

for key in group.groups.keys():
    sample_df = group.get_group(key).set_index("WellName")
    sample_result_series = sample_df.FinalResultText
    
    sample_df['ResultText'] = sample_df['BGText']+sample_df['BGTextABScrDAT']
    sample_info_series = sample_df.iloc[0][['TestDate','SampleBarcode','VerifiedByUser', 'ResultText']]

    sample_df_list.append(pd.DataFrame(pd.concat([sample_info_series, sample_result_series])).T)
    


# In[7]:


result_df = pd.concat(sample_df_list)
result_df=result_df[~result_df['VerifiedByUser'].isna()]
result_df.fillna("", inplace=True)
result_df = result_df.replace("DP", np.nan).dropna()
result_df.set_index("TestDate", inplace=True)

result_df.sort_index(inplace=True)


# In[8]:


f_name = pd.Timestamp.now().strftime('%Y%m%d_%H%M')

try:
    result_df.to_excel(f"F:/Printer/QC_{f_name}.xlsx")
except OSError:
    result_df.to_excel(f"QC_{f_name}.xlsx")
    


# In[9]:


print(result_df)


# In[ ]:





# In[ ]:




