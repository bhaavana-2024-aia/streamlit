import streamlit as st

def binary_search_guess(low, high, guess_count):
    """ Binary search algorithm to guess the number """
    return (low + high) // 2

def game():
    st.title("Computer Guesses Your Number Using Binary Search")
    
    low = 0
    high = 100
    
    if low >= high:
        st.sidebar.error("Lower bound must be less than upper bound.")
        return
    
    st.header("Think of a number between {} and {}!".format(low, high))
    st.subheader("Then, help the computer by answering its guesses!")

    guess_count = 0
    guess = binary_search_guess(low, high, guess_count)

    while True:
        guess_count += 1
        st.write(f"Guess #{guess_count}: Is your number {guess}?")
        
        feedback = st.radio(
            "Is the guess correct?",
            ('Correct', 'Too High', 'Too Low'),
            key=f"guess_{guess_count}"
        )
        
        if feedback == 'Correct':
            st.success(f"Yay! The computer guessed your number, {guess}, in {guess_count} guesses!")
            break
        elif feedback == 'Too High':
            high = guess - 1
        elif feedback == 'Too Low':
            low = guess + 1
        
        guess = binary_search_guess(low, high, guess_count)

game()