import time
import random

def greet():
    print("Hi！How can I help you today？")
    
def deepthink(question: str, duration: int | float = 5):
    text = f'<think>Okay, the user is asking about \"{question}\" '

    # Stream output
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.001, 0.1))

    # Loading effect
    start_time = time.time()
    while time.time() - start_time < duration:
        dots = int((time.time() - start_time) * 2) % 3 + 1
        loading = f"{'.' * dots}{' ' * (3 - dots)}"
        print(f"\r{text}{loading}", end='', flush=True)
        time.sleep(0.1)

def suck():
    print("\rSorry, that's beyond my current scope. Let's talk about something else.", flush=True)

def main():
    greet()
    while True:
        user_input = input("Message：")
        deepthink(user_input)
        suck()

if __name__ == "__main__":
    main()
