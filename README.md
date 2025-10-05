This PDA (pushdown automaton) recognizes the language L = 0^n1^n | n >= 0.

All the strings that are in this language have n amount of 0s followed by the same n amount of 1s.

If there is a discrepancy in the input string like a different amount of 0s and 1s, or if there is a different order of 0s and 1s,
it will not be a part of the language, and the PDA will reject the input string.

This automaton can achieve this, because it uses its stack as a way to count how many 0s it has read. Once it reads the first 1, it switches states from 
pushing (counting) to popping (removing). Since all the strings in this language have an equal amount of 0s and 1s, the PDA should consume the entire 
input and end up with an empty stack. If it still has items in the stack, or if the PDA tries to remove from the stack when the stack in empty, this is 
how it knows that the input string does not belong to language L.
