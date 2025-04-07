
# 👀 Snapchat for New Messages – A Smart Notification Checker

Ever felt overwhelmed by constant notifications from Snapchat or WhatsApp?  
This project is my personal attempt to fix that — a Python + Selenium script that quietly checks for new messages so I don’t have to stay glued to my phone all day 📵📱

---

## 💡 Why I Built This

I was struggling with screen time.  
Even when I didn’t *want* to check messages, I’d end up opening Snapchat or WhatsApp out of habit — and lose focus.

So I built a tool that:
- **Checks if I have a new message**
- **Tells me who it’s from**
- **Runs silently in the background**
- And helps me use tech *on my terms*

It’s a small automation, but it’s a big step toward digital mindfulness 🧠

---

## 🧰 Tech Stack

- **Language:** Python 🐍
- **Tools:** Selenium, Shell scripting
- **Concepts:** Web scraping, background scripting, `.env` config

---

## 🔄 How It Works

1. You run the script manually.
2. If there’s a message:
   - It notifies you instantly.
   - Then continues checking every hour.
3. If there’s no message:
   - It quietly checks again after 1 hour.
4. It stops automatically after **8 hours**, or you can manually kill it anytime.

---

## 🚀 Getting Started

[![Watch the video](https://img.youtube.com/vi/PW-qinmyEgQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=PW-qinmyEgQ)
**watch the above video on how to run the project**

### 1. Install Dependencies
```bash
./setup.sh
```

### 2. Set Up Your Environment
```bash
cp sampleenv.txt .env
```
Then fill in your credentials inside `.env`.

### 3. Run the Script
```bash
python main.py
```

To stop manually:  
`Ctrl + C`

---

## 🔮 What’s Next?

- [ ] Add support for WhatsApp Web  
- [ ] Enable desktop/email notifications  
- [ ] Auto-run using cron jobs or task scheduler  

---

## 🌐 Find Me Online

Want to connect or check out more of my work?

👉 [https://linktr.ee/your-link](https://linktr.ee/theankushrai)

Inside you’ll find:
- GitHub
- LeetCode
- GeeksForGeeks
- LinkedIn

---

## ✨ Final Thoughts

This project reflects my love for building small, useful tools using **Python**, and learning to automate everyday problems.  
I’m proud of how **Selenium** let me control the browser like magic 🪄  
If you're into automation or reducing digital distractions — give it a try!

Thanks for checking this out! 😊
```
