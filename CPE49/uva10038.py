def is_jolly_jumper(sequence):
    n = len(sequence)
    if n == 1:
        return True  # A single element is always a Jolly Jumper

    # Calculate absolute differences
    differences = set(abs(sequence[i] - sequence[i - 1]) for i in range(1, n))

    # Check if the differences match {1, 2, ..., n-1}
    return differences == set(range(1, n))

while True:
    try:
        # Read input
        num_list = list(map(int, input().split()))  # Convert all input to integers
        n = num_list[0]  # The first number is the length of the sequence
        sequence = num_list[1:]  # The remaining numbers are the sequence

        # Check if the sequence is Jolly
        if is_jolly_jumper(sequence):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break
