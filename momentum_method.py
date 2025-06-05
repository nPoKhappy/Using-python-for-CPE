import time

BETA = 0.9  # Typical value for momentum
v_t = 0     # Initial velocity
theta = 4   # Initial parameter
LR = 0.1    # Learning rate
iteration = 0

while theta > 0.001:  # Stop when theta is close to 0
    time.sleep(1)
    # Step 1: Compute gradient at current theta
    g_t = 2 * theta
    # Step 2: Update velocity
    v_t = BETA * v_t + (1 - BETA) * g_t
    # Step 3: Update theta using the new velocity
    theta = theta - LR * v_t
    # Print results
    print(f"Iteration {iteration}:")
    print(f"theta = {theta:.3f}")
    print(f"step = {LR * v_t:.3f}")
    print(f"velocity = {v_t:.3f}")
    print(f"gradient = {g_t:.3f}")
    print("---")
    iteration += 1

