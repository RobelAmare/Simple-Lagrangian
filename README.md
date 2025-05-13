# Simple-Lagrangian

## Overview

This project provides a Python script that utilizes the `SymPy` library to symbolically derive the equation of motion for a simple pendulum using the principles of **Lagrangian mechanics**.

---

## Theoretical Background

### Lagrangian Mechanics

Lagrangian mechanics offers an elegant and powerful approach to classical mechanics, particularly useful for systems with constraints. It is based on the concept of the Lagrangian, defined as the difference between kinetic energy (\( T \)) and potential energy (\( V \)):

\[
L = T - V
\]

The dynamics of the system are governed by the **Euler-Lagrange equation**:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/Screenshot%202025-05-13%20164833.png)

Where:
-  ![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/qi.png): The generalized coordinates describing the system's configuration.
-  ![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/qi_dot.png): The corresponding generalized velocities.

For a simple pendulum of mass \( m \) and length \( l \), the system can be fully described by a single generalized coordinate: the angle  θ, which the pendulum makes with the vertical.

---

## Formulas Used and Their Implementation

### 1. Kinetic Energy (\( T \))

Formula:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/kinetic%20formula.png)

For a simple pendulum, the velocity of the bob is ![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/velocity.png). Substituting this into the formula gives:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/kinetic%20energy%20second%20formula.png)

---

**Python Implementation:**

```python
T_sym = sympy.Rational(1, 2) * m_sym * (l_sym * theta_dot)**2
```

---

### 2. Potential Energy (\( V \))

Formula:

\[
V = m g h
\]

Taking the pivot point as the reference level (\( h = 0 \)), the height of the bob is ![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/height%20of%20the%20bob%20.png)
Substituting this gives:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/potential_energy.png)

**Python Implementation:**

```python
V_sym = -m_sym * g_sym * l_sym * sympy.cos(theta)
```

---

### 3. The Lagrangian (\( L \))

Formula:

\[
L = T - V
\]

Substituting the expressions for \( T \) and \( V \):

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/The%20Lagrangian%20.png)

**Python Implementation:**

```python
L_sym = T_sym - V_sym
```

---

### 4. Euler-Lagrange Equation

Formula:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/Euler-Lagrangef2.png)

For the simple pendulum, the generalized coordinate is \( \theta \). The equation becomes:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/for%20simple%20pendulum.png)

**Python Implementation:**

```python
# Partial derivatives
dL_d_theta_dot_sym = L_sym.diff(theta_dot)
dL_d_theta_sym = L_sym.diff(theta)

# Time derivative of the first partial derivative
d_dt_dL_d_theta_dot_sym = dL_d_theta_dot_sym.diff(t)

# Euler-Lagrange equation
euler_lagrange_eq_sym = d_dt_dL_d_theta_dot_sym - dL_d_theta_sym
```

---

### 5. Equation of Motion

Derived from the Euler-Lagrange equation:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/equation%20of%20motion%20from%20euler-lagrange.png)

Dividing through by mL² (assuming \( m, L ≠ 0 ) gives:

![image](https://github.com/RobelAmare/Simple-Lagrangian/blob/main/equation%20of%20motion%20final.png)

**Python Implementation:**

```python
equation_of_motion_sym = sympy.simplify(euler_lagrange_eq_sym)
angular_acceleration = sympy.solve(equation_of_motion_sym, theta_ddot)
```

---

## How to Use the Code

### Prerequisites

1. Ensure Python is installed.
2. Install the SymPy library:

   ```bash
   pip install sympy
   ```

### Steps

1. Save the Python code (provided separately) as a `.py` file (e.g., `pendulum_lagrangian.py`).
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the script using:

   ```bash
   python pendulum_lagrangian.py
   ```

### User Inputs

The script will prompt you to enter the following:
- The mass of the pendulum bob (\( m \)).
- The length of the pendulum (\( l \)).
- The acceleration due to gravity (\( g \)).

### Outputs

The script will display:
- Symbolic expressions for:
  - Kinetic Energy (\( T \)).
  - Potential Energy (\( V \)).
  - The Lagrangian (\( L \)).
  - Euler-Lagrange equation components.
  - The final equation of motion.
- Numerical results for the angular acceleration based on the provided inputs.

---

## Improving Output Readability (this feature hasnt been added in this project  !!!!!!)

### 1. Generate LaTeX Output

SymPy can convert symbolic expressions into LaTeX strings using `sympy.latex()`. You can then paste these strings into a LaTeX editor or a Markdown viewer that supports LaTeX to see the properly formatted equations.

**Example Code:**

```python
print("\n--- LaTeX Output ---")
print("Symbolic Lagrangian (LaTeX):")
print(sympy.latex(L_sym))
print("\nEquation of Motion (LaTeX):")
print(sympy.latex(equation_of_motion_sym))
```

### 2. Use Jupyter Notebook

For an interactive environment, consider running the script in a Jupyter Notebook, where formulas can be rendered directly in LaTeX format.

---

## Conclusion

This project demonstrates the power and elegance of **Lagrangian mechanics** and symbolic computation using Python and SymPy. Whether you're a student, educator, or enthusiast, this tool can help you explore the beauty of classical mechanics.

**its strongly advised to use the mentioned tools to view a better output result for better visibility.
**

# **the main code file can be found here**:https://github.com/RobelAmare/Simple-Lagrangian/blob/main/pendulum_lagrangian.py
