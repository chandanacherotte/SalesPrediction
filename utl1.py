#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
from arima import get_trend_pic
import tkinter as tk
from sklearn.externals import joblib 
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os
warnings.filterwarnings("ignore")
plt.style.use("fivethirtyeight")
import pandas as pd
import statsmodels.api as sm
import matplotlib
from tkinter import messagebox
#  
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14

matplotlib.rcParams['ytick.labelsize'] = 14
matplotlib.rcParams['text.color'] = 'b';



#print("A")
def get_trend(item):

    get_trend_pic(item)    
    from PIL import ImageTk,Image  
    window= tk.Toplevel()  
    
    canvas = tk.Canvas(window, width = 1000, height = 1000)
    canvas.configure(background='black')
    canvas.pack()  
    img1=Image.open("temp.png")
    img2 = img1.resize((1008,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img2)  
    
    canvas.create_image(500,500,image=img)
                  
    
    window.mainloop()  

 
