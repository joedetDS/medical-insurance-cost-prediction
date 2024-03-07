#import the necessary libraries
import streamlit as st
import time
import json
import requests

#Load the model
url = "https://med-api-jbgd.onrender.com/med_prediction"

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
        
    
    #Store all data in dictionary
    input_data_for_model = {
        
        'age': age,
        'gender': mod_gender,
        'bmi': bmi,
        'children': children,
        'smoke': mod_smoking_status,
        'region': mod_region,
       
        }
    
    #Store in a json format
    input_json = json.dumps(input_data_for_model)

    #Post the data to the url 
    response = requests.post(url, data=input_json)
    
    # Return the response
    return response.text

def main():
    #Title of the page
    st.title("Medical Insurance Cost Predictor")
    
    
    
    #Prompt user to enter the details
    age = st.slider('Age', min_value=0, max_value=100)
    st.success(f'Selected Age: {age}')
    
    gender=st.selectbox('Select your gender',['Male','Female'])
    st.success(f'Selected Gender: {gender}')
    
    bmi = st.slider('BMI (kg/m²)', min_value=0, max_value=100)
    st.success(f'Selected BMI: {bmi}')
    
    children=st.text_input('Number of Children')
    st.success(f'Selected children: {children}')
    
    smoke=st.selectbox('Do you Smoke',['Yes','No'])
    st.success(f'Selected smoke status: {smoke}')
    
    region=st.selectbox('Select your region',['southeast','southwest','northeast','northwest'])
    st.success(f'Selected region: {region')
    
    #Customize the button
    if st.button("Show Cost"):
        
        #Display an error if an input field is left empty
        if (not age or  not bmi or not children):
            st.error("No input field should be left blank!")
            
        #Display an error if its not a number    
        elif (age == 0 or bmi == 0):
            st.error("Please enter a valid values for age and BMI")
            
        else: 
            #Display a spinner while waiting
            with st.spinner('Processing...'):
                time.sleep(5)
                
            #enter arguments to the function and round the result to 2 decimal place
            cost= float (modified_input_data(age,gender,bmi,children,smoke,region))
            
            #format the cost
            formatted_cost = "{:,.2f}".format(cost)
            
            #add text to the cost
            cost_text="Your insurance cost is #"+ str(formatted_cost)
            
            #Display the cost
            st.success(cost_text)

#Run the main function
if __name__ =='__main__':
    main()
