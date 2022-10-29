#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)
# two underscore before and after = identification of coder


# In[4]:


__name__


# In[5]:


from flask import request,render_template

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
       
        model1 = joblib.load("regression.joblib")
        r1 = model1.predict([[rates]])
        
        model2 = joblib.load("tree.joblib")
        r2 = model2.predict([[rates]])
        
        return(render_template("index.html",result1=r1,result2=r2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))

# decorator is a fuction for flask that must be run before function is run 
# generator


# In[ ]:


if __name__ == "__main__":
    app.run()
    
# 127.0.0.1 is IP address reserved for local host (127.0.0.1:5000)
# port (equivalent to door, i.e. 5000, jupyter:8888/8889/8890)


# In[ ]:




