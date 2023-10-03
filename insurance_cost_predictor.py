# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:22:46 2023

@author: Edet Joseph
"""
#import the necessary libraries
import numpy as np
import streamlit as st
import joblib
import time

#Load the model
model=joblib.load("C:/Users/Edet Joseph/Desktop/Machine L/Medical Insurance Cost Prediction/regressor")

#Function to predict
def modified_input_data(age,gender,bmi,children,smoker_status,region):
    
    age=int(age)
    bmi=float(bmi)
    children=int(children)
    
    #encode the gender
    if gender=='Female':
        mod_gender=1
    else:
        mod_gender=0
        
    
    #encode the smoker status
    if smoker_status=='yes':
        mod_smoking_status=1
    else:
        mod_smoking_status=0
    
    #encode the region
    if region=='southeast':
        mod_region=0
    elif region=='southwest':
        mod_region=1
    elif region=='northeast':
        mod_region=2
    else:
        mod_region=3
        
    
    #Store all data in tuple
    input_data=(age,mod_gender,bmi,children,mod_smoking_status,mod_region)
    
    #Convert the data to array
    input_data_array=np.asarray(input_data)
    
    #reshape the data
    input_data_reshaped=input_data_array.reshape(1,-1)
    
    #make predictions on the reshaped data
    prediction=model.predict(input_data_reshaped)

    return prediction[0]

def main():
    #Title of the page
    st.title("Medical Insurance Cost Predictor")
    
    
    
    #Prompt user to enter the details
    age=st.text_input('Age')
    
    gender=st.selectbox('Select your gender',['Male','Female'])
    
    bmi=st.text_input('BMI (kg/m²)')
    
    children=st.text_input('Number of Children')
    
    smoke=st.selectbox('Do you Smoke',['Yes','No'])
    
    region=st.selectbox('Select your region',['southeast','southwest','northeast','northwest'])
    
    
    #Customize the button
    if st.button("Show Cost"):
        
        #Display an error if an input field is left empty
        if (not age or  not bmi or not children):
            st.error("No input field should be left blank!")
        else: 
            #Display a spinner while waiting
            with st.spinner('Processing...'):
                time.sleep(5)
                
                
            
            #enter arguments to the function and round the result to 2 decimal place
            cost=modified_input_data(age,gender,bmi,children,smoke,region)
            
            #format the cost
            formatted_cost = "{:,.2f}".format(cost)
            
            #add text to the cost
            cost_text="Your annual insurance cost is $"+ str(formatted_cost)
            
            #Display the cost
            st.success(cost_text)

#Run the main function
if __name__ =='__main__':
    main()