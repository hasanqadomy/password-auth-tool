import time
import sys
import random
import string
import os

name = '''
┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓   ┏━╸╻ ╻┏━╸┏━╸╻┏ ┏━╸┏━┓   ╺┳╸┏━┓┏━┓╻  
┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃   ┃  ┣━┫┣╸ ┃  ┣┻┓┣╸ ┣┳┛    ┃ ┃ ┃┃ ┃┃  
╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛   ┗━╸╹ ╹┗━╸┗━╸╹ ╹┗━╸╹┗╸    ╹ ┗━┛┗━┛┗━╸
Ｂｙ：ｄ３ｆ４ｕｌｔ
'''

print(name)

ROCKYOU_PATH = os.path.join(os.path.dirname(__file__), "rockyou.txt")  # Define rockyou.txt path

def progress_bar(duration=5, steps=20):
    for i in range(steps + 1):
        time.sleep(duration / steps)
        percent = int((i / steps) * 100)
        bar = "#" * i + "." * (steps - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
    
    print("\n✅ Done! \n")

def check_length(password, min_len=8):
    return len(password) >= min_len

def check_repeated_chars(password):
    return len(set(password)) > 2  # Ensure password isn't just repeating the same character

def check_rockyou(password):
    if not os.path.exists(ROCKYOU_PATH):
        print("❌ rockyou.txt file not found. Ensure it's in the same directory as app.py.")
        return False
    
    try:
        print("🔍 Searching in rockyou.txt...")
        file_size = os.path.getsize(ROCKYOU_PATH)
        with open(ROCKYOU_PATH, "r", encoding="latin-1") as file:
            checked_size = 0
            sys.stdout.write("\r🔍 Searching: [" + " " * 50 + "] 0%")
            sys.stdout.flush()
            for line in file:
                checked_size += len(line)
                percent = int((checked_size / file_size) * 100)
                bar_length = percent // 2
                sys.stdout.write(f"\r🔍 Searching: [" + "#" * bar_length + " " * (50 - bar_length) + f"] {percent}%")
                sys.stdout.flush()
                if password == line.strip():
                    print("\n❌ Your password is leaked in rockyou.txt wordlist! Please choose a stronger password.")
                    return False
        print("\n✔️ Your password was NOT found in rockyou.txt.")
    except Exception as e:
        print(f"❌ Error reading rockyou.txt: {e}")
        return False
    return True

def password_checker():
    while True:
        password = input("Enter Your Password: ")
        if check_length(password, 8) and check_repeated_chars(password) and check_rockyou(password):
            break
        print("⚠️ Please enter a stronger password! It should not be too short, repetitive, or commonly used.\n")

    score = 0

    def check_uppercase(password):
        nonlocal score
        if any(char.isupper() for char in password):
            print("✔️ Uppercase check done!")
            score += 1

    def check_lowercase(password):
        nonlocal score
        if any(char.islower() for char in password):
            print("✔️ Lowercase check done!")
            score += 1

    def check_digit(password):
        nonlocal score
        if any(char.isdigit() for char in password):
            print("✔️ Digit check done!")
            score += 1

    def check_special_char(password):
        nonlocal score
        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
        if any(char in special_chars for char in password):
            print("✔️ Special character check done!")
            score += 1

    def check_common_passwords(password):
        nonlocal score
        COMMON_PASSWORDS = {"123456", "password", "123456789", "qwerty", "abc123"}
        if password.lower() not in COMMON_PASSWORDS:
            print("✔️ Common password check passed!")
            score += 1
        else:
            print("❌ Password is too common, choose a stronger one!")
            score = 0  # Set score to 0 if the password is too common

    print("Let's check your password . . .")
    progress_bar(2, 50)

    check_uppercase(password)
    check_lowercase(password)
    check_digit(password)
    check_special_char(password)
    check_common_passwords(password)

    print(f"🔹 Final Score: {score}/5")
    
    if score < 3:
        print("⚠️ Your password is weak! Consider using a mix of uppercase letters, lowercase letters, numbers, and special characters for better security.")

def password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    print(f"🔑 Generated Password: {generated_password}")

while True:
    print("\nChoose an option:")
    print("1 - Password Checker")
    print("2 - Password Generator")
    print("999 - Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        password_checker()
    elif choice == "2":
        password_generator()
    elif choice == "999":
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, please enter 1, 2, or 999.")
