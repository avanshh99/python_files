import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    print("Time's up!")

# Example usage
seconds = int(input("Enter the countdown duration in seconds: "))
countdown_timer(seconds)
