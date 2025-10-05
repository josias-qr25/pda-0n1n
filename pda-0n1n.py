def run_pda(input_string):

    # Initialize stack with bottom symbol.
    stack = ["Z0"]
    state = "q0"
    print(f"Start: State={state}, Stack={stack}, Input='{input_string}'")

    if not all(c in "01" for c in input_string):
        print("Input Error: String contains characters other than 0 or 1.")
        return "-- INPUT REJECTED --"

    # State q0. Transition to q1.
    if state == "q0":
        state = "q1"
        print(
            f"Transition (q0, epsilon, Z0) -> (q1, Z0). State={state}, Stack={stack}"
        )

    # State q1.
    i = 0
    while i < len(input_string):
        char = input_string[i]

        if state == "q1":
            if char == "0":
                top = stack[-1]
                if top == "X":
                    stack.append("X")
                    print(f"Read '0': (q1, 0, X) -> (q1, XX). Stack={stack}")
                elif top == "Z0":
                    stack.append("X")
                    print(f"Read '0': (q1, 0, Z0) -> (q1, XZ0). Stack={stack}")
                i += 1
            elif char == "1":
                if stack[-1] == "X":
                    stack.pop()
                    state = "q2"
                    print(f"Read '1': (q1, 1, X) -> (q2, epsilon). State={state}, Stack={stack}")    
                    i += 1
                else:
                    print("Read '1' in state q1.")
                    return "-- INPUT REJECTED --"
            else:
                print("Input format error. Must be 0s followed by 1s.")
                return "-- INPUT REJECTED --"

        elif state == "q2":
            if char == "1":
                if stack[-1] == "X":
                    stack.pop()
                    print(
                        f"Read '1': (q2, 1, X) -> (q2, epsilon). Stack={stack}"
                    )
                    i += 1
                else:
                    print("Error: More 1s than 0s.")
                    return "-- INPUT REJECTED --"
            else:
                print("Input format error. '0' cannot appear after a '1'.")
                return "-- INPUT REJECTED --"

    print(f"End of input: State={state}, Stack={stack}")
    if state == "q2" and stack == ["Z0"]:
        print("Final state is q2 and stack is empty.")
        return "++ INPUT ACCEPTED ++"
    else:
        print("Did not end in accepting state or stack not empty.")
        return "-- INPUT REJECTED --"


input_string = input()
run_pda(input_string)
