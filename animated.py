import time


def animated_message(message: str):
    for i in range(5):
        print(f"{message}{"."*i}", end="\r")
        time.sleep(0.5)
    print("\n")