# ADB Command

## Shortcut Mind Map (for Memorization)
```
🔹 Start:            adb devices           → কানেক্টেড ডিভাইস চেক করো
🔹 Access Shell:     adb shell             → ডিভাইসে প্রবেশ করো (Linux shell)

🛠️ System Info:
├── getprop                         → ডিভাইস properties দেখো (OS version, model)
├── dumpsys battery                 → ব্যাটারির অবস্থা দেখো
├── ip addr show wlan0             → ডিভাইসের IP দেখো

📦 App Control:
├── pm list packages               → Installed apps দেখো
├── pm list packages | grep name  → নির্দিষ্ট app খুঁজো
├── install app.apk               → অ্যাপ ইনস্টল করো
├── uninstall <pkg>               → অ্যাপ আনইনস্টল করো
├── pm clear <pkg>                → অ্যাপের data ক্লিয়ার করো
├── am start -n <pkg>/.MainAct    → নির্দিষ্ট অ্যাপ চালু করো
├── am force-stop <pkg>           → অ্যাপ forcefully বন্ধ করো
├── am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:<pkg>
│                                 → অ্যাপের Info Settings পেইজ খুল

📲 Input Automation:
├── input tap X Y                 → স্ক্রিনে নির্দিষ্ট স্থানে ট্যাপ করাও
├── input text "Hello"            → লেখা টাইপ করাও
├── input swipe X1 Y1 X2 Y2       → স্ক্রিনে swipe effect দাও
├── input keyevent 3              → Home বাটনে ক্লিক
├── input keyevent 4              → Back বাটনে ক্লিক

📷 Screen Capture:
├── screencap -p > file.png       → স্ক্রিনশট নাও
├── screenrecord /sdcard/demo.mp4 → স্ক্রিন ভিডিও রেকর্ড করো
├── pull /sdcard/demo.mp4         → ভিডিও ফাইল পিসিতে নিয়ে আসো

📁 File Transfer:
├── push <file> /sdcard/          → পিসি → ফোনে ফাইল পাঠাও
├── pull /sdcard/<file>           → ফোন → পিসিতে ফাইল নাও


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

| কাজ                            | কমান্ড                                          |
| ------------------------------ | ----------------------------------------------- |
| স্ক্রিনে ডাম্প (UI XML Layout) | `adb shell uiautomator dump`                    |
| ডাম্প pull করো                 | `adb pull /sdcard/window_dump.xml`              |
| ট্যাপ করাও                     | `adb shell input tap x y`                       |
| টাইপ করাও                      | `adb shell input text Hello_World`              |
| কীবোর্ড key press              | `adb shell input keyevent 3` (HOME), `4` (BACK) |

## ⌨️ Input Commands

| Command | কাজ |
|---------|-----|
| `adb shell input text 'Hello_World'` | লেখা টাইপ করে |
| `adb shell input tap X Y` | স্ক্রিনের X,Y লোকেশনে ট্যাপ করে |
| `adb shell input swipe X1 Y1 X2 Y2` | স্ক্রিনে swipe effect দেয় |
| `adb shell input keyevent 3` | Home বাটনে ক্লিকের মতো কাজ করে |
| `adb shell input keyevent 4` | Back বাটনে ক্লিকের মতো কাজ করে |

📱 3. Device Info
| কাজ          | কমান্ড                                       |
| ------------ | -------------------------------------------- |
| OS version   | `adb shell getprop ro.build.version.release` |
| Device name  | `adb shell getprop ro.product.model`         |
| Brand name   | `adb shell getprop ro.product.brand`         |
| Full list    | `adb shell getprop`                          |
| Battery info | `adb shell dumpsys battery`                  |


🎥 4. Screenshot & Video
| কাজ           | কমান্ড                                    |
| ------------- | ----------------------------------------- |
| Screenshot    | `adb exec-out screencap -p > ss.png`      |
| Record Screen | `adb shell screenrecord /sdcard/demo.mp4` |
| Pull video    | `adb pull /sdcard/demo.mp4`               |

🌐 5. Network & IP Info

| কাজ     | কমান্ড                         |
| ------- | ------------------------------ |
| WiFi IP | `adb shell ip addr show wlan0` |
| All IP  | `adb shell ifconfig`           |
| Ping    | `adb shell ping 8.8.8.8`       |

🔌 6. File Transfer

| কাজ        | কমান্ড                        |
| ---------- | ----------------------------- |
| ফোন → পিসি | `adb pull /sdcard/myfile.txt` |
| পিসি → ফোন | `adb push file.txt /sdcard/`  |


🛠️ 7. Developer / Advanced
| কাজ                   | কমান্ড                                       |
| --------------------- | -------------------------------------------- |
| Logcat (realtime log) | `adb logcat`                                 |
| Wireless ADB          | `adb tcpip 5555` → তারপর IP দিয়ে connect করো |
| Debug specific app    | `adb shell am start -D -n package/.Activity` |


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
