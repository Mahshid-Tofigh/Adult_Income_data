#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:45:24 2023

@author: mahshidtofigh
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Adults Salaries")

st.subheader("Analysing Adults Salaries Based on Different Factors")

upload = st.file_uploader("Upload your dataset in CSV format.")

if upload is not None:
    data = pd.read_csv(upload)
    
if upload is not None:
     data_shape = st.radio("What dimension you need to check?",("Rows", "Columns"))
     if data_shape == "Rows":
         st.text("Number of Rows:")
         st.write(data.shape[0])
     if data_shape == "Columns":
         st.text("Number of Columns:")
         st.write(data.shape[1])    
         
if upload is not None:         
    if st.checkbox("Statistic Summary of Dataset"):
        st.write(data.describe())
        

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("First 5 Rows"):
            st.write(data.head())
        if st.button("Last 5 Rows"):
            st.write(data.tail())

if upload is not None:
    test = data.isnull().values.any()
    if test==True:
        st.warning("Dataset contains null values")
        
    else:
        st.success("There are no missing values in the Dataset") 


if upload is not None:
    ans = st.selectbox("Do you want to see the relationship between income and age?",("Select yes or no", "Yes", "No"))
    if ans == "Yes":
        sns.barplot(x="income", y="age", data= data)
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
    if ans == "No":
        st.text("No problem.")  

if upload is not None:
   data["workclass"] = data["workclass"].replace("?", np.nan)
   data["native-country"] = data["native-country"].replace("?", np.nan)


if upload is not None:
    work_class = st.radio("Do you want to see the distribution of the work classes?",("Yes", "No"))
    if work_class == "Yes":
        plt.figure(figsize= (15, 10))
        sns.countplot(x= "workclass", data= data)
        st.pyplot()
    if work_class == "No":
        st.text("No problem.")

if upload is not None:
    st.write("Number of people that have masters or bachelors degree:")
    st.write(sum(data["education"].isin(["Bachelors", "Masters"])))
    st.text("Number of People and their Native Countries: ")
    st.write(data["native-country"].value_counts())


if upload is not None:
    if st.checkbox("Male or Female Percentage having Bachelors"):
        if st.button("Male"):
            percent_male_bachelor = round(len(data[(data["education"] == "Bachelors") & (data["gender"] == "Male")]) * 100 / len(data))
           
            st.write(percent_male_bachelor)
        
        if st.button("Female"):
            percent_female_bachelor = round(len(data[(data["education"] == "Bachelors") & (data["gender"] == "Female")]) * 100 / len(data))
            
            st.write(percent_female_bachelor)
                       
if upload is not None:
    
    if st.checkbox("Relation Between Race & Education"):
        
        black =  round(len(data[data["race"] == "Black"]) * 100 / len(data))
        
        white = round(len(data[data["race"] == "White"]) * 100 / len(data))
        
        asian = round(len(data[data["race"] == "Asian-Pac-Islander"]) * 100 / len(data))
        
        other = round(len(data[data["race"] == "Other"]) * 100 / len(data))
        
        skimo = round(len(data[data["race"] == "Amer-Indian-Eskimo"]) * 100 / len(data))
        
        color = ["red", "pink", "green", "blue", "yellow"]
        
        race_list_num = [black, white, asian, other, skimo]
        race_list = ["African-American", "White", "Asian", "Skimo", "Other"]
        
        plt.pie(race_list_num, labels= race_list, colors= color, autopct= "%0.1f%%", radius= 0.75, textprops= {"fontsize":12})
        st.pyplot()

if upload is not None:
    st.write("Average work hours for Males and Females:")
    st.write(data.groupby("gender")["hours-per-week"].mean())            