
##  Python দিয়ে স্ক্রিনশট নেওয়ার স্ক্রিপ্ট (তুমি চাইলে এটা চালাতে পারো):


```
platform-tools/
├── adb.exe
├── fastboot.exe
├── dmtracedump.exe
├── etc...
├── example.py
```

##### example.py

```python 
import subprocess

# adb কমান্ড চালাও
result = subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=subprocess.PIPE)

# আউটপুটকে ফাইলে লিখে দাও
with open('screenshot.png', 'wb') as f:
    f.write(result.stdout)

print("Screenshot saved as screenshot.png")
```


---


### কোডের ব্যাখ্যা
```python 
import subprocess
```
Python এর subprocess মডিউল ইমপোর্ট করছে, যা বাইরের কোনো প্রোগ্রাম বা কমান্ড চালানোর জন্য ব্যবহৃত হয়।

```python 
result = subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=subprocess.PIPE)
```

- এখানে `subprocess.run()` দিয়ে `adb exec-out screencap -p` কমান্ডটি চালানো হচ্ছে।
- `adb exec-out screencap -p` হলো Android ফোন থেকে স্ক্রিনশট নেওয়ার জন্য ADB কমান্ড।
- `stdout=subprocess.PIPE` মানে, কমান্ডের আউটপুট (যা স্ক্রিনশটের বাইনারি ডেটা) Python প্রোগ্রামে ক্যাপচার করা হবে `result.stdout` এ।


```python
with open('screenshot.png', 'wb') as f:
    f.write(result.stdout)
with open('screenshot.png', 'wb') as f: — 'screenshot.png' নামে একটি নতুন ফাইল তৈরি করছে বাইনারি মোডে (wb = write binary)।

f.write(result.stdout) — আগের কমান্ড থেকে পাওয়া বাইনারি ডেটা ওই ফাইলে লেখা হচ্ছে।
```

ফলে, ফোনের স্ক্রিনশট ‘screenshot.png’ নামে ফাইল হিসেবে সেভ হবে।

```python
print("Screenshot saved as screenshot.png")
শেষে প্রিন্ট করবে, কাজটি সফল হয়েছে।
```

এই কোডটি তোমার Android ফোন থেকে ADB এর মাধ্যমে স্ক্রিনশট নিয়ে সেটা Python দিয়ে তোমার পিসিতে PNG ফাইল হিসেবে সংরক্ষণ করে।




#### করণীয়:
- তোমার পিসিতে Python ইনস্টল থাকতে হবে।
- platform-tools এর adb.exe তোমার system PATH-এ থাকতে হবে অথবা subprocess.run এ adb এর ফুল পাথ দিবে।
- উপরের স্ক্রিপ্ট save করে চালাও।
- একই ফোল্ডারে screenshot.png ফাইল তৈরি হবে।





---

### Python দিয়ে adb ব্যবহার করে ফোনের সব ইনস্টল করা অ্যাপের তালিকা

```
import subprocess

# adb shell command to list all installed packages
result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)

# আউটপুটকে লাইন বাই লাইন ভাগ করো
packages = result.stdout.splitlines()

print("Installed apps packages on your phone:")
for package in packages:
    print(package)

```
 
### ১. ফোন থেকে ফাইল কপি করা (pull)
```python 
import subprocess

# ফোন থেকে পিসিতে ফাইল কপি করা
subprocess.run(['adb', 'pull', '/sdcard/Download/sample.txt', 'sample.txt'])
```

### ২. পিসি থেকে ফোনে ফাইল পাঠানো (push)

```python 
import subprocess

# পিসি থেকে ফোনে ফাইল পাঠানো
subprocess.run(['adb', 'push', 'myfile.txt', '/sdcard/Download/'])
```
### ৩. APK ইনস্টল করা

```python 
import subprocess

subprocess.run(['adb', 'install', 'path/to/app.apk'])
```

### ৪. APK আনইনস্টল করা
```python 
import subprocess

subprocess.run(['adb', 'uninstall', 'com.package.name'])
```

### ৫. Shell Access (কমান্ড চালানো)

```python 
import subprocess

result = subprocess.run(['adb', 'shell', 'ls', '/sdcard/Download'], capture_output=True, text=True)
print(result.stdout)
```


### 6 Python দিয়ে 1 মিনিট (60 সেকেন্ড) ভিডিও রেকর্ড করার উদাহরণ:

```python 
import subprocess

# 60 সেকেন্ড ভিডিও রেকর্ড করবে ফোনে /sdcard/demo.mp4 ফাইলে
subprocess.run(['adb', 'shell', 'screenrecord', '--time-limit', '60', '/sdcard/demo.mp4'])
```

এরপর পিসিতে ভিডিও কপি করার জন্য:
```python
# ফোন থেকে পিসিতে ভিডিও ফাইল কপি করা
subprocess.run(['adb', 'pull', '/sdcard/demo.mp4', 'demo.mp4'])
```

### 7 WhatsApp ওপেন করা ADB দিয়ে

```python 
import subprocess

# WhatsApp অ্যাপ চালু করা
subprocess.run([
    'adb', 'shell', 'monkey',
    '-p', 'com.whatsapp',
    '-c', 'android.intent.category.LAUNCHER',
    '1'
])
```

📝 ব্যাখ্যা:
- monkey: Android এ অ্যাপ স্টার্ট করার একধরনের টুল (monkey testing tool)
- -p com.whatsapp: প্যাকেজ নাম (WhatsApp এর জন্য)
- -c android.intent.category.LAUNCHER: launcher category ট্যাগ
- 1: একবারই চালাবে


### Whatsapp Open and Write Message and Send 
```python
import subprocess
import urllib.parse
import time

phone = "8801706656131"
message = "Hello from Python + ADB!"
encoded_message = urllib.parse.quote(message)
url = f"https://wa.me/{phone}?text={encoded_message}"

# Step 1: WhatsApp open
subprocess.run(['adb', 'shell', 'am', 'start','-a', 'android.intent.action.VIEW','-d', url])
result = subprocess.run(['adb','shell','dumpsys' ,'display'], capture_output=True, text=True)
subprocess.run(['adb','shell','input','tap','650','1450'])
```


### 8 App Force Stop
```
import subprocess

subprocess.run(['adb', 'shell', 'am', 'force-stop', 'com.whatsapp'])
```
চলমান অ্যাপ হঠাৎ বন্ধ করার জন্য।


### 📸 ৫. Multiple Screenshots Auto Loop
```python 
import time
for i in range(3):
    subprocess.run(['adb', 'exec-out', 'screencap', '-p'], stdout=open(f'screen{i}.png', 'wb'))
    time.sleep(5)  # প্রতি ৫ সেকেন্ডে স্ক্রিনশট
```



### 🧠 ৯. Device Info বের করা (Model, Version, Battery, Storage)

```python 
import subprocess

subprocess.run(['adb', 'shell', 'getprop'], text=True)
subprocess.run(['adb', 'shell', 'dumpsys', 'battery'], text=True)
subprocess.run(['adb', 'shell', 'df', '/sdcard'], text=True)
```
### 10. ADB দিয়ে কন্টাক্ট নাম্বার ও নাম দেখতে

```
subprocess.run(['adb', 'shell' ,'content', 'query', '--uri', 'content://contacts/phones/', '--projection', 'display_name:number']) 
```

### 11. ইনবক্সের এসএমএস মেসেজের জন্য

```
import subprocess

try:
    # Run adb shell command, capture raw bytes
    result = subprocess.run(
        ['adb', 'shell', 'content', 'query', '--uri', 'content://sms/inbox/'],
        capture_output=True,
        text=False  # Keep raw bytes
    )

    if result.stdout is None:
        print("No output from adb command.")
    else:
        # Decode using UTF-8, replace errors to avoid crashes on invalid bytes
        output = result.stdout.decode('utf-8', errors='replace')

        # Save output to UTF-8 encoded file
        with open('sms_inbox_bangla.txt', 'w', encoding='utf-8') as f:
            f.write(output)

        print("Bangla SMS saved successfully to sms_inbox_bangla.txt")

    # If adb returned an error, print it (also decoded properly)
    if result.returncode != 0:
        err = (result.stderr.decode('utf-8', errors='replace') 
               if result.stderr else "No error message")
        print(f"ADB error (code {result.returncode}): {err}")

except Exception as e:
    print("Exception:", e)
```

<h6> 
    
| অংশ                          | ব্যাখ্যা (বাংলায়)                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `adb`                        | Android Debug Bridge — কম্পিউটার থেকে ফোনে কমান্ড পাঠানোর জন্য ব্যবহৃত                                                     |
| `shell`                      | ফোনের ভিতরের Linux Shell-এ প্রবেশ করে কমান্ড চালানোর জন্য                                                                  |
| `content`                    | Android-এর Content Provider ব্যবস্থার অংশ — যেটা ফোনের ডেটাবেইস অ্যাক্সেস করতে দেয় (যেমন Contacts, SMS, Call Logs ইত্যাদি) |
| `query`                      | Content Provider থেকে তথ্য বের করে আনতে চাই, তাই `query` চালাই                                                             |
| `--uri`                      | URI (Uniform Resource Identifier) জানায়, কোন ধরনের তথ্য চাই                                                                |
| `content://contacts/phones/` | এই URI নির্দেশ করে আমরা **contacts database** থেকে **phone number সহ তথ্য** আনতে চাই                                       |
| `--projection`               | projection মানে কোন কোন ফিল্ড/কলাম চাই তা নির্দিষ্ট করা                                                                    |
| `display_name:number`        | দুটি ফিল্ড চাই: ১) Contact এর নাম (`display_name`), ২) Contact এর নাম্বার (`number`)       |

</h6>
---



Python দিয়ে যেকোনো ADB কমান্ড চালানো অনেক সহজ এবং আরও কাস্টমাইজড করা যায়।