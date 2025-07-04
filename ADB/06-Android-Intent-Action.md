🧠 Intent কীভাবে কাজ করে?
একটি Intent সাধারণত ৩টি গুরুত্বপূর্ণ অংশে ভাগ করা যায়:


| অংশ          | ব্যাখ্যা                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------- |
| **Action**   | কী কাজ করবে (যেমন: দেখানো, কল করা, এডিট করা ইত্যাদি)                                      |
| **Data**     | কোন ডাটা নিয়ে কাজ করবে (যেমন URL, ফোন নম্বর, ছবি)                                         |
| **Category** | কোন ধরণের অ্যাপ এটি হ্যান্ডেল করতে পারবে (যেমন LAUNCHER ক্যাটাগরি মানে হোম স্ক্রিন অ্যাপ) |




## 1️⃣ কিছু গুরুত্বপূর্ণ Intent Action

| Action String                           | কাজের বর্ণনা                                         |
| --------------------------------------- | ---------------------------------------------------- |
| `android.intent.action.VIEW`            | কোনো ডাটা (যেমন URL, ছবি, ভিডিও) দেখানো              |
| `android.intent.action.SEND`            | অন্য অ্যাপের কাছে ডাটা পাঠানো (শেয়ার করা)            |
| `android.intent.action.MAIN`            | অ্যাপের মেইন entry point চালানো                      |
| `android.intent.action.DIAL`            | ডায়ালার খুলে কল করার জন্য নম্বর দেখানো               |
| `android.intent.action.CALL`            | সরাসরি কল করা (permission লাগবে)                     |
| `android.intent.action.EDIT`            | ডাটা এডিট করার জন্য অ্যাপ চালানো                     |
| `android.intent.action.PICK`            | ইউজারকে ডাটা নির্বাচন করতে দেয় (যেমন কনট্যাক্ট, ছবি) |
| `android.intent.action.DELETE`          | ডাটা ডিলেট করার জন্য Intent                          |
| `android.intent.action.INSERT`          | নতুন ডাটা যোগ করার জন্য Intent                       |
| `android.intent.action.SENDTO`          | কেবল পাঠানোর জন্য (যেমন SMS)                         |
| `android.intent.action.POWER_CONNECTED` | পাওয়ার সংযুক্ত হলে ট্রিগার হয়                        |
| `android.intent.action.BOOT_COMPLETED`  | ফোন বুট হলে ট্রিগার হয়                               |



## 2️⃣  Intent Category (ক্যাটাগরি)

| ক্যাটাগরি                           | ব্যাখ্যা                                    |
| ----------------------------------- | ------------------------------------------- |
| `android.intent.category.LAUNCHER`  | হোম স্ক্রিনে যে অ্যাপ দেখা যায়              |
| `android.intent.category.BROWSABLE` | ব্রাউজার বা ওয়েবভিত্তিক লিংক ওপেন করার জন্য |
| `android.intent.category.DEFAULT`   | সাধারণ Action এর জন্য লাগবেই                |


## 3️⃣ Android Intent Data  

Intent Data মানে হলো — Intent যখন কোনো কাজ করতে যায় (যেমন ওয়েবসাইট দেখানো, কল করা, ছবি খোলা), তখন সে কোন ডাটা নিয়ে কাজ করবে সেটা -d (data) দিয়ে বলে দিতে হয়।


সহজ করে বললে:
- Intent Action → কী কাজ করবে?
- Intent Data → কোন জিনিসের উপর কাজ করবে?

উদাহরণসহ ব্যাখ্যা:

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


<h6>
 
| উদাহরণ (Command)                                           | ব্যাখ্যা                                                   |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| `-d https://www.google.com`                                | ওয়েবসাইট ব্রাউজারে খুলবে                                   |
| `-d tel:01712345678`                                       | ফোন ডায়ালারে ওই নম্বর দেখাবে                               |
| `-d sms:01712345678`                                       | SMS অ্যাপে ওই নম্বরে নতুন মেসেজ লেখার পেজ খুলবে            |
| `-d mailto:someone@example.com`                            | ইমেইল অ্যাপে ওই ঠিকানায় ইমেইল পাঠানোর পেজ খুলবে            |
| `-d geo:37.7749,-122.4194`                                 | ম্যাপে নির্দিষ্ট latitude, longitude লোকেশন দেখাবে         |
| `-d geo:0,0?q=1600+Amphitheatre+Parkway,+Mountain+View`    | ম্যাপে সার্চ কুয়েরি পাঠাবে (address বা জায়গার নাম)         |
| `-d content://contacts/people/1`                           | কন্টাক্টের ID=1 এর তথ্য দেখাবে বা এডিট করবে                |
| `-d file:///sdcard/Download/sample.pdf`                    | ফাইল ম্যানেজার বা পিডিএফ রিডারে ঐ ফাইল খুলবে               |
| `-d content://media/external/images/media/123`             | গ্যালারিতে ছবির ID=123 ওপেন করবে                           |
| `-d market://details?id=com.example.app`                   | Google Play Store এ নির্দিষ্ট অ্যাপের পেজ খুলবে            |
| `-d "https://wa.me/8801700000000?text=Hello%20from%20ADB"` | WhatsApp এ সরাসরি নির্দিষ্ট নম্বরে মেসেজ পাঠানোর পেজ খুলবে |
| `-d "fb-messenger://user/USER_ID"`                         | Facebook Messenger এ USER\_ID এর চ্যাট খুলবে               |
| `-d "tg://resolve?domain=username"`                        | Telegram এ নির্দিষ্ট username এর চ্যাট খুলবে               |
</h6>


### আরও কিছু URI Scheme এর উদাহরণ
<h6>
 
| URI Scheme              | কাজের বর্ণনা                                    | উদাহরণ                            |
| ----------------------- | ----------------------------------------------- | --------------------------------- |
| `http://` বা `https://` | ওয়েব পেজ ব্রাউজারে খোলা                         | `https://www.example.com`         |
| `tel:`                  | ফোন নম্বর ডায়ালার খোলা                          | `tel:01712345678`                 |
| `sms:`                  | SMS অ্যাপ মেসেজ পাঠানো                          | `sms:01712345678`                 |
| `mailto:`               | ইমেইল অ্যাপ ইমেইল পাঠানো                        | `mailto:test@example.com`         |
| `geo:`                  | ম্যাপে লোকেশন দেখানো                            | `geo:37.7749,-122.4194`           |
| `content://`            | ফোনের ডেটাবেস থেকে ডাটা (কন্টাক্ট, ছবি ইত্যাদি) | `content://contacts/people/1`     |
| `file://`               | লোকাল ফাইল ওপেন করা                             | `file:///sdcard/Download/doc.pdf` |
| `market://`             | Google Play Store অ্যাপ পেজ                     | `market://details?id=com.app`     |

</h6> 

| অপশন | কাজ                                    |
| ---- | -------------------------------------- |
| `-a` | Action (যেমন: VIEW, SEND)              |
| `-d` | Data (যেমন: URL, ফোন নম্বর)            |
| `-t` | টাইপ (MIME type: text/plain, image/\*) |
| `-n` | নির্দিষ্ট অ্যাপ বা Activity চালানো     |
| `-p` | কোন প্যাকেজে চালাবে                    |
| `-c` | Category (যেমন: LAUNCHER)              |
| `-e` | Extra ডাটা পাঠানো                      |

                                         
### -a type (Action)
-a হলো Intent এর সবচেয়ে গুরুত্বপূর্ণ অংশ, যা বলে দেয় কি কাজ করতে হবে। প্রতিটি Action এর আলাদা ব্যবহার ও উদ্দেশ্য থাকে।
আরও উদাহরণ বা বিস্তারিত চাইলে জানাও!

```bash 
# ডাটা বা ইউআরএল দেখানোর জন্য ব্যবহার হয়।
adb shell am start -a android.intent.action.VIEW -d https://www.google.com

# কল ডায়ালারের UI ওপেন করার জন্য।
adb shell am start -a android.intent.action.DIAL -d tel:01712345678

# অন্য অ্যাপে টেক্সট শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.TEXT "Hello from ADB"

# ইউজারকে ছবি বা ফাইল সিলেক্ট করতে বলবে।
adb shell am start -a android.intent.action.PICK -t image/*

# কন্টাক্ট এডিট করার জন্য।
adb shell am start -a android.intent.action.EDIT -d content://contacts/people/1

# SMS অ্যাপ ওপেন করবে নির্দিষ্ট নম্বর সহ।
adb shell am start -a android.intent.action.SENDTO -d sms:01712345678

# ফোনের সেটিংস অ্যাপ চালু করবে।
adb shell am start -a android.intent.action.MAIN -n com.android.settings/.Settings

# ওয়েবসাইট ব্রাউজারে দেখাবে।
adb shell am start -a android.intent.action.VIEW -d https://www.example.com

# WhatsApp চালু করবে।
adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1

# Telegram এ নির্দিষ্ট ইউজারের সাথে চ্যাট শুরু করবে।
adb shell am start -a android.intent.action.VIEW -d "tg://resolve?domain=username"
```

### -d type (Data)
-d দিয়ে Intent-এ ডাটা বা URI/URL পাঠানো হয়। এটি নির্ধারণ করে অ্যাপ কোন তথ্য নিয়ে কাজ করবে।

```perl 
# ব্রাউজারে গুগল ওয়েবসাইট খুলবে।
adb shell am start -a android.intent.action.VIEW -d https://www.google.com

# ম্যাপে সান ফ্রান্সিসকোর লোকেশন দেখাবে।
adb shell am start -a android.intent.action.VIEW -d geo:37.7749,-122.4194

# ফোন ডায়ালারে নির্দিষ্ট নম্বর দেখাবে।
adb shell am start -a android.intent.action.DIAL -d tel:01712345678

# SMS অ্যাপে নির্দিষ্ট নম্বর সেট করবে।
adb shell am start -a android.intent.action.SENDTO -d sms:01712345678

# ইমেইল অ্যাপে নির্দিষ্ট ইমেইল ঠিকানা দিয়ে খুলবে।
adb shell am start -a android.intent.action.SENDTO -d mailto:someone@example.com

# কন্টাক্ট এডিট পেজ খুলবে নির্দিষ্ট আইডি দিয়ে।
adb shell am start -a android.intent.action.EDIT -d content://contacts/people/1

# গ্যালারি থেকে নির্দিষ্ট ছবি দেখাবে।
adb shell am start -a android.intent.action.VIEW -d content://media/external/images/media/123

# ফাইল ম্যানেজারে নির্দিষ্ট ফাইল খুলবে।
adb shell am start -a android.intent.action.VIEW -d file:///sdcard/Download/sample.pdf

# WhatsApp এ নির্দিষ্ট নম্বরে মেসেজ পাঠানোর URL।
adb shell am start -a android.intent.action.VIEW -d "https://wa.me/8801700000000?text=Hello%20from%20ADB"

# Facebook এ নির্দিষ্ট প্রোফাইল খুলবে।
adb shell am start -a android.intent.action.VIEW -d "https://www.facebook.com/profile.php?id=1000123456789"
যদি বাকিটা (-t, -n, -c, -e) দরকার হয়, বলো।
আশা করি এই উদাহরণগুলো কাজে লাগবে!
```


 
### -t type (MIME Type)
-t দিয়ে অ্যাপে কোন ধরনের ডাটা পাঠানো হচ্ছে তা বোঝানো হয়। এতে অ্যাপ ঠিক মতো ডাটা প্রসেস করতে পারে।

```bash 
# প্লেইন টেক্সট শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.TEXT "Hello World"

# ইমেইল পাঠানোর সময় plain text টাইপ দিয়ে।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.SUBJECT "Subject Here"

# ছবি শেয়ার করার জন্য MIME টাইপ।
adb shell am start -a android.intent.action.SEND -t image/jpeg -d file:///sdcard/Pictures/photo.jpg

# ভিডিও শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t video/mp4 -d file:///sdcard/Videos/video.mp4

# অডিও ফাইল শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t audio/mpeg -d file:///sdcard/Music/song.mp3

# HTML কন্টেন্ট শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t text/html -e android.intent.extra.TEXT "<h1>Hello</h1>"

# PDF ফাইল ওপেন করার জন্য।
adb shell am start -a android.intent.action.VIEW -t application/pdf -d file:///sdcard/Download/sample.pdf

# ওয়েব পেজ শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t text/uri-list -d https://www.example.com

# কাস্টম MIME টাইপ (যেমন JSON)।
adb shell am start -a android.intent.action.SEND -t application/json -e android.intent.extra.TEXT '{"key":"value"}'

# কন্টাক্ট কার্ড শেয়ার করার জন্য।
adb shell am start -a android.intent.action.SEND -t text/vcard -d content://contacts/people/1
```
### -n component (Component Name)
 -n দিয়ে তুমি সরাসরি কোন অ্যাপের নির্দিষ্ট Activity চালাতে পারো, যা অ্যাপের ভিতরের নির্দিষ্ট স্ক্রিন।
 
```bash
# ফোনের সেটিংস অ্যাপের স্পেসিফিক Activity চালানো।
adb shell am start -n com.android.settings/.Settings

# Chrome ব্রাউজারের মেইন Activity চালানো।
adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main

# WhatsApp অ্যাপ চালানো।
adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1

# Facebook অ্যাপের মেইন Activity চালানো।
adb shell am start -n com.facebook.katana/.MainActivity

# Telegram অ্যাপ চালানো।
adb shell monkey -p org.telegram.messenger -c android.intent.category.LAUNCHER 1

# Gmail অ্যাপ চালানো।
adb shell am start -n com.google.android.gm/.ConversationListActivityGmail

# YouTube অ্যাপ চালানো।
adb shell monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1

# Google Maps এর স্পেসিফিক Activity চালানো।
adb shell am start -n com.google.android.apps.maps/.MapActivity

# Instagram অ্যাপ চালানো।
adb shell monkey -p com.instagram.android -c android.intent.category.LAUNCHER 1

# Twitter অ্যাপ চালানো।
adb shell monkey -p com.twitter.android -c android.intent.category.LAUNCHER 1
```
### -c category (Category)
-c দিয়ে Intent এর ক্যাটেগরি বা ধরণ নির্ধারণ করা হয়, যা সিস্টেম বুঝতে সাহায্য করে কোন ধরনের অ্যাপ বা কার্যকরী অংশ চালাতে হবে।

```bash
# অ্যাপ লঞ্চার থেকে অ্যাপ চালানো।
adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1

# হোম স্ক্রিন থেকে চালানোর জন্য।
adb shell am start -a android.intent.action.MAIN -c android.intent.category.HOME

# ডিফল্ট ব্রাউজার হিসেবে চালানো।
adb shell am start -a android.intent.action.VIEW -d https://www.google.com -c android.intent.category.BROWSABLE

# অ্যাপ উইন্ডো হিসেবে চালানো।
adb shell am start -a android.intent.action.MAIN -c android.intent.category.APP_BROWSER

# রিসিভার হিসেবে কাজ করার জন্য।
adb shell am start -a android.intent.action.SEND -c android.intent.category.DEFAULT

# গেম হিসেবে চালানোর জন্য।
adb shell monkey -p com.mygame.app -c android.intent.category.GAME 1

# ইমেইল ক্লায়েন্ট হিসেবে চালানো।
adb shell am start -a android.intent.action.SENDTO -c android.intent.category.APP_EMAIL -d mailto:someone@example.com

# ওয়েব পেজ ব্রাউজারের জন্য।
adb shell am start -a android.intent.action.VIEW -c android.intent.category.BROWSABLE -d https://example.com

# ডকুমেন্ট ওপেন করার জন্য।
adb shell am start -a android.intent.action.VIEW -c android.intent.category.DEFAULT -d file:///sdcard/Download/sample.pdf

# মিডিয়া প্লেয়ার হিসেবে চালানোর জন্য।
adb shell monkey -p com.android.music -c android.intent.category.APP_MUSIC 1
```

### -e extra (Extra data)
-e মানে: Intent এ অতিরিক্ত (extra) key-value পেয়ার হিসেবে ডাটা পাঠানো হয়।
-e দিয়ে অতিরিক্ত তথ্য key-value পেয়ার আকারে পাঠানো হয়, যা Intent গ্রহণকারী অ্যাপ প্রয়োজনমতো ব্যবহার করে।

```bash 
# টেক্সট শেয়ার করার সময় অতিরিক্ত ডাটা পাঠানো।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.TEXT "Hello from ADB"

# ইমেইলের সাবজেক্ট সেট করা।
adb shell am start -a android.intent.action.SENDTO -d mailto:someone@example.com -e android.intent.extra.SUBJECT "Meeting Schedule"

# SMS পাঠানোর জন্য অতিরিক্ত বার্তা।
adb shell am start -a android.intent.action.SENDTO -d sms:01712345678 -e sms_body "Hello from ADB"

# ছবি শেয়ার করার সময় ক্যাপশন পাঠানো।
adb shell am start -a android.intent.action.SEND -t image/jpeg -e android.intent.extra.TEXT "My photo caption"

# মেসেজিং অ্যাপে অতিরিক্ত ফোন নম্বর পাঠানো।
adb shell am start -a android.intent.action.SENDTO -d sms:01712345678 -e exit_on_sent true

# ব্রাউজারে ইউআরএল শেয়ার করার সময় টাইটেল।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.TITLE "My URL Title"

# ভিডিও শেয়ার করার সময় অতিরিক্ত বিবরণ।
adb shell am start -a android.intent.action.SEND -t video/mp4 -e android.intent.extra.TEXT "Check out this video"

# অডিও শেয়ার করার সময় শিল্পীর নাম।
adb shell am start -a android.intent.action.SEND -t audio/mpeg -e android.intent.extra.ARTIST "Artist Name"

# কাস্টম কী-ভ্যালু পেয়ার পাঠানো।
adb shell am start -a android.intent.action.VIEW -e my_custom_key "custom_value"

# ফেসবুকে ইউআরএল শেয়ার করার সময় শিরোনাম।
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.SUBJECT "Facebook Post"
```

### Random Example
```
# ম্যাপে সান ফ্রান্সিসকো লোকেশন দেখাবে
adb shell am start -a android.intent.action.VIEW -d geo:37.7749,-122.4194

# অন্য অ্যাপে টেক্সট শেয়ার করার জন্য Intent
adb shell am start -a android.intent.action.SEND -t text/plain -e android.intent.extra.TEXT "Hello from ADB"

# কন্টাক্ট এডিট পেজ খুলবে (id=1)
adb shell am start -a android.intent.action.EDIT -d content://contacts/people/1

# ইউজারকে ছবি সিলেক্ট করতে বলবে
adb shell am start -a android.intent.action.PICK -t image/*

# সরাসরি কল শুরু করবে (permission লাগবে)
adb shell am start -a android.intent.action.CALL -d tel:1234567890

# ফোনের সেটিংস অ্যাপ চালু করবে
adb shell am start -a android.intent.action.MAIN -n com.android.settings/.Settings

# ইমেইল ক্লায়েন্ট চালু করবে এবং ইমেইল পাঠানোর জন্য প্রস্তুত করবে
adb shell am start -a android.intent.action.VIEW -d mailto:someone@example.com

# WhatsApp চালু করবে (Home screen থেকে)
adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1

# WhatsApp এ সরাসরি মেসেজ পাঠানোর জন্য (WhatsApp URL scheme)
adb shell am start -a android.intent.action.VIEW -d "https://wa.me/8801700000000?text=Hello%20from%20ADB"

# Facebook অ্যাপ চালু করবে (Home screen থেকে)
adb shell monkey -p com.facebook.katana -c android.intent.category.LAUNCHER 1

# Facebook এর নির্দিষ্ট URL খুলবে ব্রাউজারে অথবা ফেসবুক অ্যাপে
adb shell am start -a android.intent.action.VIEW -d "https://www.facebook.com/profile.php?id=1000123456789"

# Messenger অ্যাপ চালু করবে (Home screen থেকে)
adb shell monkey -p com.facebook.orca -c android.intent.category.LAUNCHER 1

# Messenger এ নির্দিষ্ট contact কে মেসেজ পাঠানোর intent (Messenger URI scheme)
adb shell am start -a android.intent.action.VIEW -d "fb-messenger://user/USER_ID"

# Telegram চালু করবে (Home screen থেকে)
adb shell monkey -p org.telegram.messenger -c android.intent.category.LAUNCHER 1

# Telegram এ সরাসরি চ্যাট শুরু করার জন্য URL scheme
adb shell am start -a android.intent.action.VIEW -d "tg://resolve?domain=username"

# ওয়েবসাইট ওপেন করা
adb shell am start -a android.intent.action.VIEW -d https://www.google.com

# ফোন ডায়ালার ওপেন করে নম্বর দেখানো
adb shell am start -a android.intent.action.DIAL -d tel:01712345678

# SMS অ্যাপ ওপেন করে নম্বর সেট করা
adb shell am start -a android.intent.action.SENDTO -d sms:01712345678

# ইমেইল অ্যাপ চালু করা
adb shell am start -a android.intent.action.SENDTO -d mailto:someone@example.com

# ম্যাপে লোকেশন দেখানো
adb shell am start -a android.intent.action.VIEW -d geo:37.7749,-122.4194

# গ্যালারিতে ছবি দেখানো (content URI)
adb shell am start -a android.intent.action.VIEW -d content://media/external/images/media/123

# ফাইল ওপেন করা
adb shell am start -a android.intent.action.VIEW -d file:///sdcard/Download/sample.pdf

```

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



```
adb shell am start -a android.intent.action.VIEW -d https://www.google.com
```
> -a android.intent.action.VIEW → দেখাতে হবে (View action) <br>
> -d https://www.google.com → গুগল ওয়েবসাইট URL পাঠাবে <br>

```bash 
adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1
```

> -p com.whatsapp → WhatsApp অ্যাপ টার্গেট করবে <br>
> -c android.intent.category.LAUNCHER → অ্যাপ লঞ্চার থেকে চালানো হচ্ছে <br>
> 1 → ১ বার চালাবে 