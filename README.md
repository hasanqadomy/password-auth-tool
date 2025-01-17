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
After downloading `rockyou.txt`, your project directory should look like this:

📁 Password-Authentication-Tool ├── 📜 app.py # Main script ├── 📜 rockyou.txt # Password wordlist (MUST be in the same directory) ├── 📜 README.md # Project description

yaml
Copy
Edit

---

## **🔹 How to Download `rockyou.txt`**
The tool **requires `rockyou.txt`** to check for leaked passwords.  

### **Option 1: Download from Kali Linux**
If you have **Kali Linux**, you can find `rockyou.txt` in:
```sh
/usr/share/wordlists/rockyou.txt.gz
```
To extract it, run:

```sh
gzip -d /usr/share/wordlists/rockyou.txt.gz
```
Then copy the file to your project directory.

Option 2: Download Manually
Download rockyou.txt from: 🔗 RockYou.txt on Kaggle
Move it into your project folder (Password-Authentication-Tool/).
🚀 How to Use the Tool
1️⃣ Clone the Repository:

sh
Copy
Edit
git clone https://github.com/hasanqadomy/password-auth-tool.git
cd password-auth-tool
2️⃣ Make Sure rockyou.txt is Inside the Project Folder!
(If it's missing, follow the steps above to download it.)

3️⃣ Run the Script:

sh
Copy
Edit
python app.py
4️⃣ Choose an Option:

1 – Check Password Strength
2 – Generate a Secure Password
999 – Exit
🔐 Example Usage
vbnet
Copy
Edit
Choose an option:
1 - Password Checker
2 - Password Generator
999 - Exit

Enter Your Password: mypassword123
🔍 Searching in rockyou.txt... [############          ] 60%
❌ Your password is leaked in rockyou.txt! Please choose a stronger password.

🔹 Final Score: 2/5
⚠️ Your password is weak! Consider using uppercase letters, numbers, and special characters.
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

yaml
Copy
Edit

---

## **🔹 What’s New in This README?**
✅ **Added clear steps to download `rockyou.txt`**  
✅ **Explained the directory structure**  
✅ **Simplified setup & usage instructions**  
✅ **Included direct links to `rockyou.txt`**  
✅ **Formatted it to be easy to follow**  

---

### **✅ Next Steps**
1. **Replace your current `README.md`** with this version.
2. **Commit & push to GitHub**:
   ```sh
   git add README.md
   git commit -m "Updated README with rockyou.txt instructions"
   git push origin main
