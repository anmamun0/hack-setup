🔧 ADB (Android Debug Bridge) কী?
ADB হচ্ছে Android-এর জন্য একটি কমান্ড লাইন টুল, যার মাধ্যমে তুমি তোমার ফোনকে পিসি/ল্যাপটপ থেকে নিয়ন্ত্রণ করতে পারো।

🔁 এটি মূলত “ফোন ↔️ কম্পিউটার” এর মধ্যে এক ধরনের debugging connection তৈরি করে।

🔑 ADB দিয়ে কী করা যায়?

| কাজ                            | ব্যাখ্যা                                |
| ------------------------------ | --------------------------------------- |
| 📂 ফাইল পাঠানো/নেওয়া           | ফোন থেকে কম্পিউটারে ফাইল কপি বা উল্টোটা |
| 📱 App install/uninstall       | .apk ফাইল ইনস্টল বা রিমুভ করা           |
| 🐚 Shell access                | ফোনে টার্মিনাল access (Linux shell)     |
| 📸 Screenshot তোলা             | স্ক্রিনশট নিয়ে PC তে save করা           |
| 📲 ফোনের log দেখা              | App crash log, system log               |
| 🔧 Reboot/Recovery mode চালানো | Reboot, fastboot mode                   |
| 📦 System partition পড়া        | (Root লাগলে)                            |


##📌 কিভাবে ADB চালানো হয়?
##### 🧪 Step-by-Step:
#### ✅ Step 1: ফোনে Developer Mode অন করো
Settings → About Phone → Build number এ ৭ বার চাপো → Developer Mode অন হবে

#### ✅ Step 2: USB Debugging অন করো
Settings → Developer Options → USB Debugging অন করো

#### ✅ Step 3: ADB ডাউনলোড করো
Windows-এর জন্য ADB Tools:
🔗 https://developer.android.com/studio/releases/platform-tools

#### ✅ Step 4: CMD দিয়ে চালাও
```bash 
adb devices
```
or
```bash 
.\adb devices
```

#### ফোনে popup আসবে “Allow USB Debugging?” → Allow করো




🧪 কিছু জনপ্রিয় ADB কমান্ড:




| কমান্ড                           | কাজ                        |
| -------------------------------- | -------------------------- |
| `adb devices`                    | কানেক্টেড ডিভাইস লিস্ট     |
| `adb shell`                      | ফোনে টার্মিনাল ওপেন        |
| `adb pull /sdcard/file.txt`      | ফোন থেকে পিসিতে ফাইল কপি   |
| `adb push file.txt /sdcard/`     | পিসি থেকে ফোনে ফাইল পাঠানো |
| `adb install app.apk`            | APK ইনস্টল                 |
| `adb uninstall com.package.name` | App আনইনস্টল               |
| `adb logcat`                     | সিস্টেম লগ দেখা            |


### 🛡️ নিরাপত্তা বিষয়:
- তোমার ফোন শুধু তখনই ADB দিয়ে কন্ট্রোল করা যাবে যদি তুমি USB Debugging allow করো
- ফোনে পাসওয়ার্ড/লক থাকলে ADB shell limited হয়ে যায়
- কিছু advanced কাজের জন্য Root access লাগবে

### 🎯 সংক্ষেপে:
ADB হলো Android ডিভাইসকে পিসি থেকে নিয়ন্ত্রণ করার জন্য শক্তিশালী টুল — File transfer, App management, Automation সহ অনেক কিছু সম্ভব।

