import pandas as pd
import  streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder


st.write("# Loan Application")

def inputs():
    Gender=st.selectbox("Gender",["Male","Female"])
    Married=st.selectbox("Married",["Yes","No"])
    Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox('Self Employed', ['Yes', 'No'])
    Dependents = st.selectbox('Enfants', ['0', '1', '2', '3+'])
    ApplicantIncome = st.slider('Applicant Income', 150, 81000, 200)
    CoapplicantIncome = st.slider('Coapplicant Income ', 0, 33837, 2000)
    LoanAmount = st.slider('Loan Amount', 9.0, 700.0, 200.0)
    Loan_Amount_Term = st.selectbox('Loan Amount Term',
                                            (360.0, 120.0, 240.0, 180.0, 60.0, 300.0, 36.0, 84.0, 12.0))
    Credit_History = st.selectbox('Credit History', (1.0, 0.0))
    Property_Area = st.selectbox('Property Area', ('Urban', 'Rural', 'Semiurban'))


    data={
    'Gender':Gender,
    'Married':Married,
    'Dependents': Dependents,
    'Education': Education,
    'Self_Employed': Self_Employed,
    'ApplicantIncome': ApplicantIncome,
    'CoapplicantIncome': CoapplicantIncome,
    'LoanAmount': LoanAmount,
    'Loan_Amount_Term': Loan_Amount_Term,
    'Credit_History': Credit_History,
    'Property_Area': Property_Area
    }
    df=pd.DataFrame(data,index=[0])
    return df
entree=inputs()

labelencode=LabelEncoder()
#for i in range(5):
    #entree[:,i]=labelencode.fit_transform(entree[:,i])
entree.Gender.replace({'Male':1,'Female':0},inplace=True)
entree.Married.replace({'Yes':1,'No':0},inplace=True)
entree.Education.replace({'Graduate':1,'Not Graduate':0},inplace=True)
entree.Self_Employed.replace({'Yes':1,'No':0},inplace=True)
entree.Property_Area.replace({'Urban':1,'Semiurban':0,'Rural':2},inplace=True)
entree.Dependents.replace({'3+':4},inplace=True)
st.write(entree)
model=pickle.load(open('loan_model.pkl','rb'))
pred=model.predict(entree)
lc = [str(i) for i in pred]
ans = int("".join(lc))
if ans == 0:
        st.error(
        'Hello  you will not get a loan as per the calculations of the bank.'
        )
else:
    st.success(
    'Hello Congratulations!! you will get the loan from Bank')
st.write(pred)
