# ADB Command

## Shortcut Mind Map (for Memorization)

```
🔹 Start:            adb devices           → কানেক্টেড ডিভাইস চেক করো
🔹 Access Shell:     adb shell             → ডিভাইসে প্রবেশ করো (Linux shell)

🛠️ System Info:
├── getprop                                  → ডিভাইস properties দেখো (OS version, model)
├── dumpsys battery                          → ব্যাটারির অবস্থা দেখো
├── ip addr show wlan0                       → ডিভাইসের IP দেখো
├── dumpsys display                          → ডিসপ্লের রেজুলেশন ও স্কেলিং জানো
├── dumpsys cpuinfo                          → CPU ব্যবহার দেখো
├── df -h                                    → স্টোরেজ স্পেস দেখো

📦 App Control:
├── pm list packages                         → Installed apps দেখো
├── pm list packages | grep name             → নির্দিষ্ট app খুঁজো
├── pm path <package>                        → APK path খুঁজো
├── install app.apk                          → অ্যাপ ইনস্টল করো
├── uninstall <pkg>                          → অ্যাপ আনইনস্টল করো
├── pm clear <pkg>                           → অ্যাপের data ক্লিয়ার করো
├── am start -n <pkg>/.MainActivity          → নির্দিষ্ট অ্যাপ চালু করো
├── am force-stop <pkg>                      → অ্যাপ forcefully বন্ধ করো
├── am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:<pkg>
│                                            → অ্যাপের Info Settings খুলো
├── monkey -p <pkg> -c android.intent.category.LAUNCHER 1
│                                            → অ্যাপ monkey দিয়ে চালু করো

📲 Input Automation:
├── input tap X Y                            → স্ক্রিনে নির্দিষ্ট স্থানে ট্যাপ করাও
├── input text "Hello"                       → লেখা টাইপ করাও
├── input swipe X1 Y1 X2 Y2                  → স্ক্রিনে swipe effect দাও
├── input keyevent 3                         → Home বাটনে ক্লিক
├── input keyevent 4                         → Back বাটনে ক্লিক
├── input keyevent 26                        → Power বাটন প্রেস

📷 Screen Capture:
├── screencap -p > file.png                  → স্ক্রিনশট নাও
├── exec-out screencap -p > file.png         → Fast screenshot
├── screenrecord /sdcard/demo.mp4            → স্ক্রিন ভিডিও রেকর্ড করো
├── pull /sdcard/demo.mp4                    → ভিডিও ফাইল পিসিতে নিয়ে আসো

📁 File Management:
├── ls /sdcard/                              → ফোল্ডার ব্রাউজ করো
├── ls -R /sdcard/                           → সম্পূর্ণ sdcard ফোল্ডার গাছ দেখো
├── rm /sdcard/file.txt                      → ফাইল ডিলিট করো
├── mkdir /sdcard/MyFolder                   → নতুন ফোল্ডার বানাও
├── mv /sdcard/a.txt /sdcard/Docs/           → ফাইল সরাও
├── cp /sdcard/a.txt /sdcard/backup.txt      → ফাইল কপি করো

📂 File Transfer:
├── push <file> /sdcard/                     → পিসি → ফোনে ফাইল পাঠাও
├── pull /sdcard/<file>                      → ফোন → পিসিতে ফাইল নাও
├── adb pull /sdcard/DCIM/ ./DCIM            → পুরো ইমেজ ফোল্ডার নাও

🌐 Network Tools:
├── netstat                                  → নেটওয়ার্ক কানেকশন স্ট্যাটাস
├── ping 8.8.8.8                             → ইন্টারনেট কানেক্টিভিটি টেস্ট
├── ifconfig / ip addr                       → নেটওয়ার্ক ইন্টারফেস তথ্য
├── settings get global http_proxy           → প্রক্সি তথ্য জানো

🧪 Developer Tools:
├── logcat                                   → লাইভ লগ দেখো
├── bugreport                                → সম্পূর্ণ সিস্টেম রিপোর্ট বের করো
├── uiautomator dump                         → UI layout export করো
├── pull /sdcard/window_dump.xml             → UI ডাম্প পিসিতে নাও
├── tcpip 5555                               → Wireless ADB চালু করো
├── connect <ip>:5555                        → IP দিয়ে ফোন কানেক্ট করো

🧰 App Backup:
├── adb backup -apk -shared -all -f backup.ab → ব্যাকআপ নাও
├── adb restore backup.ab                    → ব্যাকআপ ফিরিয়ে আনো

```

 
### 🧩 1. App Management

| 📌 কাজ                           | 💻 কমান্ড                                                                                     |
|----------------------------------|-----------------------------------------------------------------------------------------------|
| সব installed apps দেখো           | `adb shell pm list packages`                                                                  |
| নির্দিষ্ট app খুঁজো              | `adb shell pm list packages | grep facebook`                                                 |
| অ্যাপ ইনস্টল করো (APK ফাইল থেকে) | `adb install app.apk`                                                                         |
| অ্যাপ আনইনস্টল করো               | `adb uninstall com.whatsapp`                                                                  |
| অ্যাপের ডেটা ক্লিয়ার করো         | `adb shell pm clear com.facebook.katana`                                                      |
| অ্যাপ চালু করো (main activity)   | `adb shell am start -n com.facebook.katana/.MainActivity`                                     |
| অ্যাপ চালু করো (monkey shortcut) | `adb shell monkey -p com.facebook.katana -c android.intent.category.LAUNCHER 1`               |
| অ্যাপ forcefully বন্ধ করো        | `adb shell am force-stop com.facebook.katana`                                                 |
| অ্যাপ info/settings page খোল     | `adb shell am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:com.whatsapp` |


### 🎯 2. UI Automation

| 📌 কাজ                | 💻 কমান্ড                            |
| --------------------- | ------------------------------------ |
| UI layout dump        | `adb shell uiautomator dump`         |
| XML pull করো          | `adb pull /sdcard/window_dump.xml`   |
| স্ক্রিনে ট্যাপ করাও   | `adb shell input tap X Y`            |
| লেখা টাইপ করাও        | `adb shell input text "Hello_World"` |
| স্ক্রিনে swipe effect | `adb shell input swipe X1 Y1 X2 Y2`  |
| Home key press        | `adb shell input keyevent 3`         |
| Back key press        | `adb shell input keyevent 4`         |
| Power button press    | `adb shell input keyevent 26`        |

###  ⌨️ Input Commands

| Command | কাজ |
|---------|-----|
| `adb shell input text 'Hello_World'` | লেখা টাইপ করে |
| `adb shell input tap X Y` | স্ক্রিনের X,Y লোকেশনে ট্যাপ করে |
| `adb shell input swipe X1 Y1 X2 Y2` | স্ক্রিনে swipe effect দেয় |
| `adb shell input keyevent 3` | Home বাটনে ক্লিকের মতো কাজ করে |
| `adb shell input keyevent 4` | Back বাটনে ক্লিকের মতো কাজ করে |

### 📱 3. Device Info
| 📌 কাজ             | 💻 কমান্ড                                    |
| ------------------ | -------------------------------------------- |
| OS version         | `adb shell getprop ro.build.version.release` |
| Device name        | `adb shell getprop ro.product.model`         |
| Brand name         | `adb shell getprop ro.product.brand`         |
| সব properties দেখো | `adb shell getprop`                          |
| Battery info       | `adb shell dumpsys battery`                  |
| Storage info       | `adb shell df -h`                            |
| CPU info           | `adb shell dumpsys cpuinfo`                  |
| Display info       | `adb shell dumpsys display`                  |

### 🎥 4. Screenshot & Video
| 📌 কাজ              | 💻 কমান্ড                                                 |
| ------------------- | --------------------------------------------------------- |
| Screenshot (PNG)    | `adb exec-out screencap -p > screenshot.png`              |
| Screen record       | `adb shell screenrecord /sdcard/demo.mp4`                 |
| Record limit 60 sec | `adb shell screenrecord --time-limit 60 /sdcard/demo.mp4` |
| Pull ভিডিও          | `adb pull /sdcard/demo.mp4`                               |
   

### 🌐 5. Network & IP Info

| 📌 কাজ          | 💻 কমান্ড                                  |
| --------------- | ------------------------------------------ |
| WiFi IP দেখো    | `adb shell ip addr show wlan0`             |
| সব IP দেখো      | `adb shell ifconfig`                       |
| Ping টেস্ট করো  | `adb shell ping 8.8.8.8`                   |
| HTTP proxy জানো | `adb shell settings get global http_proxy` |

### 🔌 6. File Transfer

| 📌 কাজ         | 💻 কমান্ড                       |
| -------------- | ------------------------------- |
| ফোন → পিসি     | `adb pull /sdcard/myfile.txt`   |
| পিসি → ফোন     | `adb push myfile.txt /sdcard/`  |
| ফোল্ডার ব্রাউজ | `adb shell ls /sdcard/`         |
| ফাইল ডিলিট করো | `adb shell rm /sdcard/file.txt` |

### 🛠️ 7. Developer / Advanced
| 📌 কাজ                 | 💻 কমান্ড                                    |
| ---------------------- | -------------------------------------------- |
| Realtime log           | `adb logcat`                                 |
| Wireless ADB চালু      | `adb tcpip 5555`                             |
| IP দিয়ে কানেক্ট করো    | `adb connect 192.168.1.190:5555`             |
| অ্যাপ debug mode চালাও | `adb shell am start -D -n package/.Activity` |
| bugreport তৈরী করো     | `adb bugreport > bug.zip`                    |
| সব permission দেখো     | `adb shell dumpsys package package.name`     |

## 8. dumpsys ("Dump System information")
- এটা Android-এর একটি ADB (Android Debug Bridge) কমান্ড যা বিভিন্ন সিস্টেম সার্ভিসের তথ্য (info/status/debug) বের করতে ব্যবহৃত হয়।
- dumpsys হলো Android ডিভাইসের ভেতরের সব সিস্টেম সার্ভিস (যেমন battery, wifi, activity, account, etc.) সম্পর্কে detail রিপোর্ট বের করার টুল।

<h6> 

| সেবা (`dumpsys` module) | কাজ / তথ্য                                                     |
| ----------------------- | -------------------------------------------------------------- |
| `battery`               | ব্যাটারির অবস্থা (level, charging status, temperature ইত্যাদি) |
| `activity`              | চলমান অ্যাপ, টাস্ক, ফোকাসড অ্যাপ                               |
| `window`                | UI window সম্পর্কে তথ্য                                        |
| `package`               | ইনস্টল করা অ্যাপ, পারমিশন, অ্যাক্টিভিটি                        |
| `meminfo`               | মেমোরি ব্যবহার সম্পর্কিত তথ্য                                  |
| `cpuinfo`               | CPU usage সম্পর্কে তথ্য                                        |
| `wifi`                  | WiFi অবস্থা, সংযোগ, signal strength                            |
| `bluetooth_manager`     | ব্লুটুথ অবস্থা ও ডিভাইস                                        |
| `location`              | GPS ও লোকেশন সার্ভিস                                           |
| `connectivity`          | মোবাইল/WiFi/ডেটা নেটওয়ার্ক অবস্থা                              |
| `diskstats`             | স্টোরেজ ব্যবস্থাপনা                                            |
| `notification`          | বর্তমান সক্রিয় নোটিফিকেশন                                      |
| `account`               | লগইন করা গুগল/অন্য অ্যাকাউন্ট                                  |
| `media.audio_flinger`   | অডিও প্লেব্যাক সম্পর্কিত তথ্য                                  |
| `media.session`         | মিডিয়া প্লেয়ার কন্ট্রোল                                        |
| `input`                 | ইনপুট ডিভাইস ও ইভেন্ট                                          |
| `power`                 | পাওয়ার ম্যানেজমেন্ট                                            |
| `netstats`              | ডেটা ব্যবহারের পরিসংখ্যান                                      |
| `procstats`             | প্রসেস স্ট্যাটাস                                               |
| `usagestats`            | অ্যাপ ইউসেজ রিপোর্ট                                            |
| `vibrator`              | ভাইব্রেশন কন্ট্রোল সম্পর্কিত                                   |

</h6>

```
adb shell dumpsys battery
adb shell dumpsys account
adb shell dumpsys activity
adb shell dumpsys wifi
```


9. System Databases (Content Providers)
[Learn More](https://github.com/anmamun0/hack-setup/blob/main/ADB/05-Android-App-System-Database-Access.md)


কিছু সিস্টেম ডেটা তুমি adb shell content দিয়ে query করতে পারো।

```bash
adb shell content query --uri content://contacts/phones/
adb shell content query --uri content://com.android.calendar/events
adb shell content query --uri content://call_log/calls
adb shell content query --uri content://sms/
```
 
### 10. Android Intent Action
 
[Learn More](https://github.com/anmamun0/hack-setup/blob/main/ADB/06-Android-Intent-Action.md)

Android অ্যাপে কোনো নির্দিষ্ট কাজ করানোর জন্য দেওয়া একটি নির্দেশনা (command), যেটা সিস্টেম বা অন্য অ্যাপ বুঝে নেয় এবং সেই কাজটি সম্পাদন করে।

 
##### একটি Intent সাধারণত ৩টি গুরুত্বপূর্ণ অংশে ভাগ করা যায়:
<h6>
 
| অংশ          | ব্যাখ্যা                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------- |
| **Action**   | কী কাজ করবে (যেমন: দেখানো, কল করা, এডিট করা ইত্যাদি)                                      |
| **Data**     | কোন ডাটা নিয়ে কাজ করবে (যেমন URL, ফোন নম্বর, ছবি)                                         |
| **Category** | কোন ধরণের অ্যাপ এটি হ্যান্ডেল করতে পারবে (যেমন LAUNCHER ক্যাটাগরি মানে হোম স্ক্রিন অ্যাপ) |

</h6>
 

1. website open করা:
```bash
adb shell am start -a android.intent.action.VIEW -d https://www.google.com
```

<h6>
🔹 Action: VIEW (দেখাও) <br>
🔹 Data: https://www.google.com → এটা ব্রাউজারে ওপেন হবে<br>
</h6>

2. কল করার জন্য নম্বর সেট করা (dial):
```bash 
adb shell am start -a android.intent.action.DIAL -d tel:01700000000
```
<h6>
🔹 Action: DIAL <br>
🔹 Data: tel:01700000000 → এই নম্বর কল স্ক্রিনে আসবে
</h6>

3.  লোকেশন ম্যাপে দেখানো:
```bash 
adb shell am start -a android.intent.action.VIEW -d geo:37.7749,-122.4194
```
<h6>
🔹 Action: VIEW <br>
🔹 Data: geo: URI → ম্যাপে লোকেশন দেখাবে
</h6>

4.  ইমেইল পাঠানোর জন্য প্রস্তুত করা:
```bash 
adb shell am start -a android.intent.action.VIEW -d mailto:someone@example.com
```
<h6>
🔹 Action: VIEW <br>
🔹 Data: mailto: URI → ইমেইল অ্যাপে ওপেন হবে
</h6>

5.  নির্দিষ্ট কন্টেন্ট ID (যেমন কনট্যাক্ট):
```bash 
adb shell am start -a android.intent.action.EDIT -d content://contacts/people/1
```
<h6>
🔹 Action: EDIT <br>
🔹 Data: content://contacts/people/1 → ID 1-এর কনট্যাক্ট এডিট করতে
</h6>


```
# অন্য অ্যাপে টেক্সট শেয়ার করার জন্য শেয়ার ডায়ালগ খুলবে এবং পাঠানো টেক্সট হবে "This is a test message"।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.TEXT "This is a test message"

# SMS অ্যাপ খুলবে, যেখানে রিসিপিয়েন্ট নম্বর হবে ০১৭১২৩৪৫৬৭৮ এবং SMS বডিতে আগে থেকে লেখা থাকবে "Hello from ADB"।
adb shell am start -a android.intent.action.SENDTO -d sms:01712345678 --es sms_body "Hello from ADB"

# নম্বর ০১৭১২৩৪৫৬৭৮-এ সরাসরি কল শুরু করবে (কল করার অনুমতি থাকতে হবে)।
adb shell am start -a android.intent.action.CALL -d tel:01712345678

# ক্যালেন্ডার ইভেন্ট তৈরির পেজ খুলবে, যেখানে ইভেন্টের শিরোনাম হবে "Meeting", শুরু সময় ও শেষ সময় মিলিসেকেন্ড ইউনিক্স টাইমস্ট্যাম্প হিসেবে সেট থাকবে।
adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/event -e title "Meeting" -e beginTime 1688476800000 -e endTime 1688480400000

```
 
### 11. Monkey কী?
[Learn More](https://github.com/anmamun0/hack-setup/blob/main/ADB/07_Monkey_Tool_Android_Intent-Action)

- 👉 monkey হলো Android-এর একটি testing tool,
- যেটা অ্যাপে random UI event পাঠিয়ে অ্যাপের stability ও performance পরীক্ষা করে।

#### কাজ:
- অ্যাপের ওপর এলোমেলো touch, scroll, back press ইত্যাদি simulate করে
- অ্যাপ ক্র্যাশ হয় কিনা সেটা বোঝা যায়
- Automation বা Stress Test এর জন্য ব্যবহৃত হয়

🔸 Facebook চালাতে চাই Home screen থেকে:
```bash 
adb shell monkey -p com.facebook.katana -c android.intent.category.LAUNCHER 1
```
###### → এটা শুধু অ্যাপ চালাবে। কোথা থেকে চালাচ্ছো তা দেখায় না।

🔸 Facebook এর নির্দিষ্ট Activity চালাতে চাইলে:
```bash
adb shell am start -n com.facebook.katana/.MainActivity
```
###### → এখানে তুমি সম্পূর্ণ control পাচ্ছো — চাইলে extra data, MIME type দিতে পারো।



---

## ADB Command Map (With বাংলা ব্যাখ্যা)

| 🔢     | কমান্ড                                    | মানে / কাজ                                       | মনে রাখার টিপস           |
| ------ | ----------------------------------------- | ------------------------------------------------ | ------------------------ |
| 1️⃣    | `adb shell`                               | ফোনের Linux shell চালু করে                       | Root access gateway      |
| 2️⃣    | `adb devices`                             | ফোন কানেক্ট আছে কি না দেখে                       | সবার আগে এটা verify      |
| 3️⃣    | `adb install app.apk`                     | অ্যাপ ইনস্টল করে                                 | App → install            |
| 4️⃣    | `adb uninstall package.name`              | অ্যাপ আনইনস্টল                                   | App → uninstall          |
| 5️⃣    | `adb pull /path/file`                     | ফোন → পিসি ফাইল নিয়ে আসে                         | Pull = P for PC          |
| 6️⃣    | `adb push file /sdcard/`                  | পিসি → ফোনে ফাইল পাঠায়                           | Push = P for Phone       |
| 7️⃣    | `adb getprop`                             | ফোনের সকল property দেখায় (OS version, Model etc) | Get info = getprop       |
| 8️⃣    | `adb shell dumpsys battery`               | ব্যাটারি অবস্থা জানায়                            | Dump system info         |
| 9️⃣    | `adb shell ip addr show wlan0`            | WiFi IP অ্যাড্রেস দেখায়                          | Network info             |
| 🔟     | `adb shell pm list packages`              | ফোনে installed সব প্যাকেজ লিস্ট দেখায়            | **pm** = package manager |
| 1️⃣1️⃣ | `adb shell input tap x y`                 | নির্দিষ্ট স্ক্রিনে ট্যাপ করে                     | Tap, swipe, text টাইপ    |
| 1️⃣2️⃣ | `adb shell input text Hello`              | টাইপ করে দেয়                                     | Input text = টাইপ        |
| 1️⃣3️⃣ | `adb shell screenrecord /sdcard/demo.mp4` | ফোনের স্ক্রিন রেকর্ড করে                         | Record video             |
| 1️⃣4️⃣ | `adb exec-out screencap -p > ss.png`      | স্ক্রিনশট নেয়                                    | Screenshot               |
| 1️⃣5️⃣ | `adb logcat`                              | Real-time log দেখা যায়                           | Debug logs for devs      |
