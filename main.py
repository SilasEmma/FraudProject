import streamlit as st
import pickle


st.header("Predict Titanic Passenger Survival")

def main():
    st.subheader("Fill in Passenger details to get the Prediction")
    st.sidebar.title("Developer Contact")
    st.sidebar.caption("Junior Machine Learning Engineer & Data Analyst")
    st.sidebar.caption("Phone Number: 08086560086")
    st.sidebar.markdown('[Silas Emmanuel]'
                        '(https://www.linkedin.com/in/emmanuel-s-248454116/)')
    

    Pclass = st.selectbox('Pclass', [1, 2, 3])
    Sex = st.selectbox('Sex', [0, 1])
    Age = st.text_input(label="Age")
    SibSp = st.text_input(label="SibSp")
    Parch = st.text_input(label='Parch')
    Fare = st.text_input(label="Fare")
    Embarked = st.selectbox('Embarked', [0, 1, 2])
    
    # list of columns to predict
    results = [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]

    if st.button("Predict"):

        # Read and return an object from the pickle data stored in a file.
        filename = "KaggleTitanic.pkl"

        with open(filename, 'rb') as file:
            model = pickle.load(file)

        prediction = model.predict(results)
        if prediction[0] == 0:
            st.success('Passenger Survied.')
        elif prediction[0] == 1:
            st.error('Passenger did not Survied.')
    
if __name__ == '__main__':
    main()