from string import ascii_letters, digits, punctuation
import random


def generate_random_string(length=30):
    return "".join(random.choices(ascii_letters + digits + punctuation, k=length))
