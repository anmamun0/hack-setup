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
├── am start -n <pkg>/.MainAct               → নির্দিষ্ট অ্যাপ চালু করো
├── am force-stop <pkg>                      → অ্যাপ forcefully বন্ধ করো
├── am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:<pkg>
│                                            → অ্যাপের Info Settings পেইজ খুল
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

📁 File Transfer:
├── push <file> /sdcard/                     → পিসি → ফোনে ফাইল পাঠাও
├── pull /sdcard/<file>                      → ফোন → পিসিতে ফাইল নাও
├── ls /sdcard/                              → ফোল্ডার ব্রাউজ করো
├── rm /sdcard/file.txt                      → ফাইল ডিলিট করো

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

📦 App Backup (Optional):
├── adb backup -apk -shared -all -f backup.ab → ব্যাকআপ নাও
├── adb restore backup.ab                    → ব্যাকআপ ফিরিয়ে আনো


```

 
🧩 1. App Management

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


🎯 2. UI Automation

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

## ⌨️ Input Commands

| Command | কাজ |
|---------|-----|
| `adb shell input text 'Hello_World'` | লেখা টাইপ করে |
| `adb shell input tap X Y` | স্ক্রিনের X,Y লোকেশনে ট্যাপ করে |
| `adb shell input swipe X1 Y1 X2 Y2` | স্ক্রিনে swipe effect দেয় |
| `adb shell input keyevent 3` | Home বাটনে ক্লিকের মতো কাজ করে |
| `adb shell input keyevent 4` | Back বাটনে ক্লিকের মতো কাজ করে |

📱 3. Device Info
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

🎥 4. Screenshot & Video
| 📌 কাজ              | 💻 কমান্ড                                                 |
| ------------------- | --------------------------------------------------------- |
| Screenshot (PNG)    | `adb exec-out screencap -p > screenshot.png`              |
| Screen record       | `adb shell screenrecord /sdcard/demo.mp4`                 |
| Record limit 60 sec | `adb shell screenrecord --time-limit 60 /sdcard/demo.mp4` |
| Pull ভিডিও          | `adb pull /sdcard/demo.mp4`                               |
    |

🌐 5. Network & IP Info

| 📌 কাজ          | 💻 কমান্ড                                  |
| --------------- | ------------------------------------------ |
| WiFi IP দেখো    | `adb shell ip addr show wlan0`             |
| সব IP দেখো      | `adb shell ifconfig`                       |
| Ping টেস্ট করো  | `adb shell ping 8.8.8.8`                   |
| HTTP proxy জানো | `adb shell settings get global http_proxy` |

🔌 6. File Transfer

| 📌 কাজ         | 💻 কমান্ড                       |
| -------------- | ------------------------------- |
| ফোন → পিসি     | `adb pull /sdcard/myfile.txt`   |
| পিসি → ফোন     | `adb push myfile.txt /sdcard/`  |
| ফোল্ডার ব্রাউজ | `adb shell ls /sdcard/`         |
| ফাইল ডিলিট করো | `adb shell rm /sdcard/file.txt` |

🛠️ 7. Developer / Advanced
| 📌 কাজ                 | 💻 কমান্ড                                    |
| ---------------------- | -------------------------------------------- |
| Realtime log           | `adb logcat`                                 |
| Wireless ADB চালু      | `adb tcpip 5555`                             |
| IP দিয়ে কানেক্ট করো    | `adb connect 192.168.1.190:5555`             |
| অ্যাপ debug mode চালাও | `adb shell am start -D -n package/.Activity` |
| bugreport তৈরী করো     | `adb bugreport > bug.zip`                    |
| সব permission দেখো     | `adb shell dumpsys package package.name`     |


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
