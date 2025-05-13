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

# Improving Output Readability (this feature hasnt been added in this project  !!!!!!)


## Overview

This step, while completely optional, may be necessary to view the code's output clearly and in a visually pleasing manner. It is included solely to demonstrate how the output can be better viewed and understood, **and it is not part of the main code itself**.

---

## Running the Project in Jupyter Notebook

Using Jupyter Notebook allows for enhanced output visibility, particularly for mathematical equations rendered in LaTeX format.

### Prerequisites

1. **Install Jupyter Notebook**
   Ensure that you have Jupyter Notebook installed. If not, you can install it using pip:
   ```bash
   pip install notebook
   ```

2. **Install SymPy**
   Ensure that the SymPy library is installed. You can install it with:
   ```bash
   pip install sympy
   ```

### Steps to Run the Project in Jupyter Notebook

1. **Create a Jupyter Notebook File**
   - Open your terminal or command prompt.
   - Navigate to the directory where the project is stored.
   - Start Jupyter Notebook by running:
     ```bash
     jupyter notebook
     ```
   - This will open a web interface in your default browser. Navigate to the directory and create a new Python notebook (`.ipynb` file).

2. **Write or Copy the Code**
   Copy the Python code from the project (e.g., `pendulum_lagrangian.py`) into a new code cell in the Jupyter Notebook.

3. **Render Mathematical Outputs in LaTeX**
   Use SymPy's `init_printing()` function to enable LaTeX rendering for mathematical expressions:
   ```python
   from sympy import init_printing
   init_printing()
   ```
   This ensures that any symbolic outputs (e.g., equations) are displayed in beautiful LaTeX format.

4. **Run the Notebook**
   Execute the cells step-by-step to see the outputs. Ensure that the cells with mathematical formulas are properly executed to render the LaTeX-formatted equations.


---

## Benefits of Using Jupyter Notebook 

1. **Improved Visualization**:
   - Equations and outputs are rendered in a visually appealing, LaTeX-based format, making them easier to understand.

2. **Interactive Exploration**:
   - Modify inputs and observe changes in real-time within the notebook.

3. **Exportability**:
   - Extract LaTeX outputs for documentation or presentations.

---



## Conclusion

This project provides a practical demonstration of applying Lagrangian mechanics to derive the equation of motion for a simple pendulum using the symbolic capabilities of the SymPy library in Python. By automating the calculation of kinetic energy, potential energy, the Lagrangian, and the application of the Euler-Lagrange equation, the script allows users to easily trace the steps of this fundamental derivation. This serves as a valuable tool for students and enthusiasts alike to deepen their understanding of analytical mechanics and symbolic computation. The resulting equation of motion, θ¨+Lg​sin(θ)=0, is a cornerstone result in classical mechanics, and this script offers a clear path to obtaining it from first principles.

**its strongly advised to use the mentioned tool to view a better output result for better visibility.
**

#### **The main code file can be found here**:       https://github.com/RobelAmare/Simple-Lagrangian/blob/main/pendulum_lagrangian.py
