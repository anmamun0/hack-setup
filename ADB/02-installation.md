### ADB চালানোর জন্য কোনো কিছু install করতে হয় না। এটা portable টুল, সরাসরি কাজ করে।

- ✅ কী করতে হবে এখন?
- 📁 Step-by-step ADB চালানোর জন্য:
- 🥇 Step 1: Platform Tools ফোল্ডারে যাও
- যেখানে unzip করেছো, সেই ফোল্ডারে এই ফাইলগুলো থাকবে:

https://developer.android.com/tools/releases/platform-tools

```
platform-tools/
├── adb.exe
├── fastboot.exe
├── dmtracedump.exe
├── etc...
├── example.py
```

### 🥈 Step 2: Windows CMD (Command Prompt) ওপেন করো
Start menu > CMD লিখে Enter চাপো

অথবা Platform Tools ফোল্ডারে Shift + Right Click করে
➤ “Open PowerShell window here” / "Open Command Window Here" সিলেক্ট করো

###  🥉 Step 3: adb চালাও
```bash 
adb devices
```
প্রথমবার চালালে তোমার ফোনে “Allow USB Debugging?” popup আসবে
✔️ ফোনে “Allow” চাপো

⚠️ প্রয়োজনীয় শর্ত:
| নাম                                  | দরকার কেন           |
| ------------------------------------ | ------------------- |
| 📱 ফোনে USB Debugging                | ADB কাজ করার জন্য   |
| 📎 USB Cable দিয়ে ফোন পিসিতে সংযুক্ত |                     |
| 🖥️ PC তে adb.exe                    | Unzip করেছো, তাই OK |


🔍 Test করো:
```bash 
adb devices
```
ফলাফল যদি হয়:

```arduino
List of devices attached
YH8793KK	device
```

👉 তাহলে তুমি Ready! 🟢

#### 🎁 অতিরিক্ত টিপ:
- ADB কে সবখানে চালানোর জন্য তুমি platform-tools ফোল্ডারটিকে System PATH-এ অ্যাড করতে পারো।

- চাইলে আমি দেখাতে পারি কিভাবে system-wide PATH variable সেট করো — তাহলে যেকোনো জায়গা থেকে adb চালাতে পারবে।











ধাপে ধাপে ADB দিয়ে কাজ করার জন্য তোমাকে যা করতেই হবে:
### ১. ফোনে USB Debugging চালু করো

Settings → About phone → Build number এ ৭ বার ট্যাপ করো (Developer Options চালু করার জন্য)

##### তারপর Settings → Developer Options → USB Debugging চালু করো

###  ২. ফোন এবং কম্পিউটার USB দিয়ে কানেক্ট করো

ফোনে “Allow USB Debugging?” পপআপ আসলে Allow করো

##### USB মোড ‘File Transfer’ (MTP) সেট করো

###  ৩. Windows PowerShell/Command Prompt-এ Platform Tools ফোল্ডারে গিয়ে চালাও:

```powershell 
.\adb devices
```

ডিভাইস লিস্টে তোমার ফোনের সিরিয়াল নাম্বার আসবে

---

## এখন শুরু করা যাক কিছু গুরুত্বপূর্ণ ADB কমান্ড দিয়ে:

#### 📂 ফোন থেকে ফাইল পিসিতে কপি করা
```bash 
.\adb pull /sdcard/Download/sample.pdf C:\Users\YourUserName\Desktop\
```
#### 📂 পিসি থেকে ফোনে ফাইল পাঠানো
```bash 
.\adb push C:\Users\YourUserName\Desktop\file.txt /sdcard/Download/
```
#### 📲 ফোনে APK ইনস্টল করা
```bash 
.\adb install C:\path\to\app.apk
```

#### 📲 ফোন থেকে APK আনইনস্টল করা
```bash 
.\adb uninstall com.package.name
```
(যেমন: com.whatsapp)

#### 🐚 Shell Access (টার্মিনাল চালানো)

```bash 
.\adb shell
```
এখানে ফোনের লিনাক্স কমান্ড চালাতে পারবে।

📸 ফোন থেকে স্ক্রিনশট নেওয়া
```bash 
.\adb exec-out screencap -p > screen.png
```

বলো, কোনটা দিয়ে শুরু করতে চাও?
- ফাইল ট্রান্সফার?
- APK ইনস্টল/আনইনস্টল?
- Shell access?
- অন্য কিছু?

আমি তোমার জন্য step-by-step গাইড করবো। 👍