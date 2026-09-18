
import streamlit as st
import random

st.title("My Math Quiz")

st.write("Welcome to my 5-question quiz!")

right_count = 0
wrong_count = 0

for i in range(5):

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = st.number_input(
        "What is " + str(num1) + " + " + str(num2) + "?",
        key=i
    )

    if st.button("Submit Question " + str(i + 1), key="button" + str(i)):

        if num1 + num2 == answer:
            st.success("Congrats! You are correct! The answer is: " + str(answer))
            right_count += 1
        else:
            st.error("Close, but the right answer is: " + str(num1 + num2))
            wrong_count += 1
