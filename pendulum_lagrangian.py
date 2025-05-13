# Import the SymPy library for symbolic mathematics
import sympy

# --- 1. Define Symbols and Generalized Coordinates ---
# We need to define time and any constants like gravity or mass.
t = sympy.symbols('t')  # Time
# Symbolic constants for derivation
g_sym, m_sym, l_sym = sympy.symbols('g m l', positive=True)

# Define generalized coordinates as functions of time
# For a simple pendulum, the generalized coordinate is the angle theta.
theta = sympy.Function('theta')(t)

# Define the first time derivative of the generalized coordinate (angular velocity)
theta_dot = theta.diff(t)

# Define the second time derivative of the generalized coordinate (angular acceleration)
theta_ddot = theta_dot.diff(t)

# --- 2. Define Kinetic and Potential Energy (Symbolically) ---
# Kinetic Energy (T) = 1/2 * m * v^2
# For a pendulum, v = l * theta_dot
T_sym = sympy.Rational(1, 2) * m_sym * (l_sym * theta_dot)**2

# Potential Energy (V) = m * g * h
# Using h = -l * cos(theta) with the pivot as the h=0 reference
V_sym = -m_sym * g_sym * l_sym * sympy.cos(theta)

# --- 3. Formulate the Lagrangian (L) (Symbolically) ---
# L = T - V
L_sym = T_sym - V_sym

# --- 4. Apply the Euler-Lagrange Equation (Symbolically) ---
# The Euler-Lagrange equation is: d/dt (dL/d(q_dot)) - dL/dq = 0
# For our system, q = theta
dL_d_theta_dot_sym = L_sym.diff(theta_dot)
d_dt_dL_d_theta_dot_sym = dL_d_theta_dot_sym.diff(t) # Time derivative
dL_d_theta_sym = L_sym.diff(theta)

# Form the Euler-Lagrange equation
euler_lagrange_eq_sym = d_dt_dL_d_theta_dot_sym - dL_d_theta_sym

# Simplify the equation to get the equation of motion
equation_of_motion_sym = sympy.simplify(euler_lagrange_eq_sym)

# --- Function to get valid float input from the user ---
def get_float_input(prompt_message):
    """
    Prompts the user for a float input and ensures the input is valid.
    Keeps asking until a valid float is entered.
    """
    while True:
        try:
            value_str = input(prompt_message)
            value_float = float(value_str)
            return value_float
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# --- 5. Get User Input for System Parameters ---
print("--- Please Provide System Parameters ---")
print("Please enter the following values when prompted.")

m_val = get_float_input("Enter the mass of the pendulum bob (e.g., in kg): ")
l_val = get_float_input("Enter the length of the pendulum (e.g., in meters): ")
g_val = get_float_input("Enter the acceleration due to gravity (e.g., 9.81 m/s^2): ")

# Create a dictionary for substituting these values into symbolic expressions
params = {m_sym: m_val, l_sym: l_val, g_sym: g_val}

# --- 6. Display Results (Symbolic and with User Values) ---
print("\n" + "="*50)
print("--- Simple Pendulum Lagrangian Mechanics Analysis ---")
print("="*50 + "\n")

print("--- 1. System Definition ---")
print(f"Generalized Coordinate: {theta}")
print(f"Generalized Velocity:   {theta_dot}")
print(f"Generalized Acceleration: {theta_ddot}")
print("-" * 20)

print("\n--- 2. Energies ---")
print("   Symbolic Kinetic Energy (T):")
print(f"   T = {T_sym}")
print("\n   Symbolic Potential Energy (V):")
print(f"   V = {V_sym}")

# Substitute numerical values into the symbolic energy expressions
T_num = T_sym.subs(params)
V_num = V_sym.subs(params)
print("\n   Energies with Your Values:")
print(f"   Kinetic Energy (T): {T_num}")
print(f"   Potential Energy (V): {V_num}")
print("-" * 20)

print("\n--- 3. Lagrangian ---")
print("   Symbolic Lagrangian (L = T - V):")
print(f"   L = {L_sym}")

# Substitute numerical values into the symbolic Lagrangian
L_num = L_sym.subs(params)
print("\n   Lagrangian with Your Values:")
print(f"   L = {L_num}")
print("-" * 20)


print("\n--- 4. Euler-Lagrange Equation ---")
print("   Equation Form: d/dt (dL/d(theta_dot)) - dL/d(theta) = 0")
print("\n   Components (Symbolic):")
print(f"   dL/d(theta_dot) = {dL_d_theta_dot_sym}")
print(f"   d/dt (dL/d(theta_dot)) = {d_dt_dL_d_theta_dot_sym}")
print(f"   dL/d(theta) = {dL_d_theta_sym}")

print("\n   Euler-Lagrange Equation (Symbolic Form):")
print(f"   {euler_lagrange_eq_sym} = 0")

# Substitute numerical values into the Euler-Lagrange equation
euler_lagrange_eq_num = euler_lagrange_eq_sym.subs(params)
print("\n   Euler-Lagrange Equation (With Your Values):")
print(f"   {euler_lagrange_eq_num} = 0")
print("-" * 20)

print("\n--- 5. Simplified Equation of Motion ---")
print("   Symbolic Form:")
print(f"   {equation_of_motion_sym} = 0")

try:
    # Attempt to solve the simplified equation for theta_ddot
    solved_eq_of_motion_sym = sympy.solve(equation_of_motion_sym, theta_ddot)
    if solved_eq_of_motion_sym:
        print("\n   Symbolic Solution for theta_ddot:")
        print(f"   theta_ddot = {solved_eq_of_motion_sym[0]}")
    else:
        print("\n   Could not symbolically solve for theta_ddot.")
except Exception as e:
    print(f"\n   Error symbolically solving for theta_ddot: {e}")


# Substitute numerical values into the simplified equation of motion
equation_of_motion_num = equation_of_motion_sym.subs(params)
print("\n   Simplified Equation of Motion (With Your Values):")
print(f"   {equation_of_motion_num} = 0")
try:
    # If symbolic solve was successful, substitute numerical values into the solved expression.
    # Otherwise, try solving the numerically substituted equation directly.
    if solved_eq_of_motion_sym:
        solved_eq_of_motion_num = solved_eq_of_motion_sym[0].subs(params)
        print("\n   Solution for theta_ddot (With Your Values):")
        print(f"   theta_ddot = {solved_eq_of_motion_num}")
    else: # Try solving the numeric equation directly if symbolic solve failed
        solved_eq_of_motion_num_direct = sympy.solve(equation_of_motion_num, theta_ddot)
        if solved_eq_of_motion_num_direct:
            print("\n   Solution for theta_ddot (With Your Values - Direct Solve):")
            print(f"   theta_ddot = {solved_eq_of_motion_num_direct[0]}")
        else:
            print("\n   Could not solve for theta_ddot with your values.")

except Exception as e:
    print(f"\n   Error solving for theta_ddot with your values: {e}")
    print("\n   The raw equation of motion with your values is still valid:")
    print(f"   {equation_of_motion_num} = 0")

print("\n" + "="*50)
print("--- End of Analysis ---")
print("="*50 + "\n")
