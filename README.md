# Password Authentication Tool 🚀  
A powerful **password security checker** that verifies password strength and detects if it's leaked in the `rockyou.txt` wordlist.  

---

## **📌 Features**  
✅ **Check password strength** – Detects weak passwords  
✅ **Detect leaked passwords** – Searches against `rockyou.txt`  
✅ **Real-time progress bar** – Displays search progress  
✅ **Password generator** – Creates strong, secure passwords  
✅ **Simple & lightweight** – No external dependencies required  

---

## **📂 Project Structure**
After setting up `rockyou.txt`, your project directory should look like this:

📁 Password-Authentication-Tool ├── 📜 app.py # Main script ├── 📜 rockyou.txt # Password wordlist (MUST be in the same directory) ├── 📜 README.md # Project description



---

## **📌 How to Set Up `rockyou.txt` Automatically**
### **🔹 Option 1: Extract from Kali Linux (Recommended)**
If you have **Kali Linux**, `rockyou.txt` is already included!  
Just **extract and copy it** to your project folder:
```sh
mkdir -p Password-Authentication-Tool
```
```sh
cp /usr/share/wordlists/rockyou.txt.gz Password-Authentication-Tool/
```
```sh
cd Password-Authentication-Tool
```
```sh
gzip -d rockyou.txt.gz
```
(This will copy and extract rockyou.txt into your project.)

🔹 Option 2: Download Manually
If you're on Windows or another OS, follow these steps:

1️⃣ Download rockyou.txt from: 🔗 RockYou.txt on Kaggle

2️⃣ Move it to your project folder:

```sh
mkdir -p Password-Authentication-Tool
mv ~/Downloads/rockyou.txt Password-Authentication-Tool/
3️⃣ Check if the file is in the right place:

```sh
ls Password-Authentication-Tool/
```
✔️ If you see rockyou.txt, you're good to go!

🚀 How to Use the Tool
1️⃣ Clone the Repository:

```sh
git clone https://github.com/hasanqadomy/password-auth-tool.git
```
```sh
cd password-auth-tool
```
2️⃣ Ensure rockyou.txt is Inside the Project Folder!
(If it's missing, follow the steps above to download it.)

3️⃣ Run the Script:

```sh
python app.py
```
4️⃣ Choose an Option:
```sh
1 – Check Password Strength
2 – Generate a Secure Password
999 – Exit
```
```sh
🔐 Example Usage :

Choose an option:
1 - Password Checker
2 - Password Generator
999 - Exit

Enter Your Password: mypassword123
🔍 Searching in rockyou.txt... [############          ] 60%
❌ Your password is leaked in rockyou.txt! Please choose a stronger password.

🔹 Final Score: 2/5
⚠️ Your password is weak! Consider using uppercase letters, numbers, and special characters.
```
📌 Why Use This Tool?
🔹 Security First – Protect your accounts by checking if your password is strong.
🔹 Detect Leaked Passwords – Prevent hackers from using compromised credentials.
🔹 Generate Strong Passwords – Easily create unbreakable passwords.
🔹 Lightweight & Fast – No unnecessary dependencies.

💻 Contribute & Improve
Want to make this tool better? Fork the repo, submit PRs, and contribute! 🚀

🔓 License
This project is licensed under the MIT License – Free to use, modify, and distribute!

👨‍💻 Developed by d3f4ult – Because security matters! 🔥

🌟 Star this repo if you found it useful! ⭐
Let me know if you need any more modifications! 🚀💻

---

### **✅ What’s New in This README?**
✅ **Added `rockyou.txt` auto-extraction and copying commands**  
✅ **Simplified setup for both Kali Linux and Windows users**  
✅ **Explained how to move `rockyou.txt` to the correct folder automatically**  
✅ **Formatted everything to be beginner-friendly**  

---
