import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.write("""NEWTON METHOD""")
st.write("""Using python to find a root and using Streamlit for running in web browser""")
st.write("""Web App version 1.0""")

def to_superscript(n):
        superscripts = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
        return ''.join(superscripts[char] for char in str(n))

# Getting an equation from the user
degree = st.number_input("Enter the degree of the polynomial:", min_value=0, step=1)
if degree < 0:
    st.error("Degree should be a non-negative integer.")

coefficients = []


for i in range(degree + 1):
    coefficient = st.number_input(f"Enter the coefficient of x^{degree - i}:", key=f"coef_{i}", format="%.2f", step=0.01)
    coefficients.append(coefficient)

# Creating the equation
equation = ' + '.join([f'{coefficients[i]}x^{degree - i}' for i in range(degree + 1)])
equation1= ' + '.join([f'{coefficients[i]}x{to_superscript(degree - i)}' for i in range(degree + 1)])

# Printing the equation
st.write("The equation is:", equation1)

# Defining the range of x values
x_values = np.linspace(-20, 20, 200)

# Evaluating the user-entered equation
y_values = np.polyval(coefficients, x_values)

# creating the derivative equation of the polynomial equation
derivative_coefficients = np.polyder(coefficients)
derivative_equation = ' + '.join([f'{derivative_coefficients[i]}x^{degree - i - 1}' for i in range(degree)])
derivative_equation1 = ' + '.join([f'{derivative_coefficients[i]}x{to_superscript(degree - i - 1)}' for i in range(degree)])


# Evaluating the derivative equation
derivative_y_values = np.polyval(derivative_coefficients, x_values)

st.write("The derivation equation is:", derivative_equation1)

initial_guess = st.number_input("Enter the initial guess:", key="initial_guess")
iter = st.number_input("Enter the number of Iterations to calculate the root:", min_value=1, step=1, key="num_iterations")

# Create a list to store iteration values
iteration_values = []

k = 1
while(k <= iter):
    equation_value = np.polyval(coefficients, initial_guess)
    derivative_equation_value = np.polyval(derivative_coefficients, initial_guess)
    root = initial_guess - (equation_value / derivative_equation_value)
    iteration_values.append({"Iteration": k, "Root": root})
    k += 1
    initial_guess = root

# Display iteration values in a table
st.write("Iteration Values:")
st.table(iteration_values)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'Original: $y = {equation1}$')
plt.plot(x_values, derivative_y_values, label=f'Derivative: $y = {derivative_equation1}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph")
plt.grid(True)
plt.legend()
st.pyplot(plt)

st.write("""-By Prakash Dulal""")
