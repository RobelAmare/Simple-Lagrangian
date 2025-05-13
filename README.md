# Simple-Lagrangian

## Overview

This project provides a Python script that utilizes the `SymPy` library to symbolically derive the equation of motion for a simple pendulum using the principles of **Lagrangian mechanics**. It's a useful tool for understanding the Lagrangian formulation and verifying the derivation of the pendulum's dynamics.

---

## Theoretical Background

### Lagrangian Mechanics
Lagrangian mechanics offers an elegant and powerful approach to classical mechanics, particularly useful for systems with constraints. It is based on the concept of the Lagrangian, defined as the difference between the system's **kinetic energy (T)** and **potential energy (V)**:

\[
L = T - V
\]

The dynamics of the system are governed by the **Euler-Lagrange equation**:

\[
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = 0
\]

Where:
- \( q_i \): The generalized coordinates describing the system's configuration.
- \( \dot{q}_i \): The corresponding generalized velocities.

For a simple pendulum of mass \( m \) and length \( l \), the system can be fully described by a single generalized coordinate: the angle \( \theta \), which the pendulum makes with the vertical.

---

## Formulas Used and Their Implementation

### 1. Kinetic Energy (\( T \))
Formula:
\[
T = \frac{1}{2} m v^2
\]

For a simple pendulum, the velocity of the bob is \( v = l \dot{\theta} \). Substituting this into the formula gives:
\[
T = \frac{1}{2} m (l \dot{\theta})^2 = \frac{1}{2} m l^2 \dot{\theta}^2
\]

**Python Implementation:**
```python
T_sym = sympy.Rational(1, 2) * m_sym * (l_sym * theta_dot)**2
```

### 2. Potential Energy (\( V \))
Formula:
\[
V = m g h
\]

Taking the pivot point as the reference (\( h = 0 \)), the height of the bob is \( h = -l \cos(\theta) \). Substituting this gives:
\[
V = -m g l \cos(\theta)
\]

**Python Implementation:**
```python
V_sym = -m_sym * g_sym * l_sym * sympy.cos(theta)
```

### 3. The Lagrangian (\( L \))
Formula:
\[
L = T - V
\]

Substituting the expressions for \( T \) and \( V \):
\[
L = \frac{1}{2} m l^2 \dot{\theta}^2 + m g l \cos(\theta)
\]

**Python Implementation:**
```python
L_sym = T_sym - V_sym
```

### 4. Euler-Lagrange Equation
Formula:
\[
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}}\right) - \frac{\partial L}{\partial \theta} = 0
\]

For the simple pendulum, the generalized coordinate is \( \theta \). The equation becomes:
\[
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}}\right) - \frac{\partial L}{\partial \theta} = 0
\]

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

### 5. Equation of Motion
Derived from Euler-Lagrange:
\[
m l^2 \ddot{\theta} + m g l \sin(\theta) = 0
\]

Dividing by \( m l^2 \) (assuming \( m, l \neq 0 \)):
\[
\ddot{\theta} + \frac{g}{l} \sin(\theta) = 0
\]

**Python Implementation:**
```python
equation_of_motion_sym = sympy.simplify(euler_lagrange_eq_sym)
angular_acceleration = sympy.solve(equation_of_motion_sym, theta_ddot)
```

---

## How to Use the Code

### Prerequisites
1. Make sure Python is installed.
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
- Numerical results for the angular acceleration (\( \ddot{\theta} \)) based on the provided inputs.

---

## Improving Output Readability

While the console output is structured, displaying mathematical formulas perfectly in a standard terminal is challenging. Here are some ways to improve readability:

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

This project demonstrates the power and elegance of **Lagrangian mechanics** and symbolic computation using Python and SymPy. Whether you're a student, educator, or enthusiast, this tool can help deepen your understanding of classical mechanics and symbolic mathematics.
