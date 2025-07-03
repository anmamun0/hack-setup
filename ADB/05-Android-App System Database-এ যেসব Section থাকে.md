
# System App Database URI (Content Provider)
তুমি চাইলেই বিভিন্ন সিস্টেম App এর ডেটা URI দিয়ে Access করতে পারো:

# Android Content URI List (with Bangla Notes)
<h6> 

 | Data (তথ্য) | URI (ঠিকানা) | মন্তব্য (Notes) |
|-------------|--------------|------------------|
| **Contacts (যোগাযোগ)** | `content://contacts/phones/` | ফোনের সকল যোগাযোগ বা ফোন নম্বরের জন্য। |
|  | `content://contacts/contacts` | সমস্ত যোগাযোগ ডেটা (নাম, ফোন, ইমেল ইত্যাদি)। |
|  | `content://contacts/emails` | যোগাযোগের ইমেল ডেটার জন্য। |
| **SMS (মেসেজ)** | `content://sms/inbox/` | ইনবক্সের এসএমএস মেসেজের জন্য। |
|  | `content://sms/sent` | পাঠানো এসএমএস মেসেজের জন্য। |
|  | `content://sms/draft` | ড্রাফ্ট এসএমএস মেসেজের জন্য। |
|  | `content://sms/` | সমস্ত এসএমএস মেসেজের জন্য। |
| **Call Logs (কল লগ)** | `content://call_log/calls/` | সমস্ত কল রেকর্ডের জন্য (ইনকামিং, আউটগোয়িং, মিসড কল)। |
| **Chrome History (ক্রোম ইতিহাস)** | `content://com.android.chrome.browser/bookmarks` | ক্রোম ব্রাউজারের বুকমার্ক এবং ইতিহাসের জন্য (অনেক সময় ইতিহাসও এর অন্তর্ভুক্ত থাকে)। |
| **Calendar (ক্যালেন্ডার)** | `content://com.android.calendar/events` | ক্যালেন্ডারের ইভেন্ট বা অনুষ্ঠানের জন্য। |
|  | `content://com.android.calendar/calendars` | ডিভাইসের ক্যালেন্ডার অ্যাকাউন্টের তথ্যের জন্য। |
| **Images (ছবি)** | `content://media/external/images/media` | ডিভাইসের এক্সটার্নাল স্টোরেজে থাকা সমস্ত ছবির জন্য। |
| **Audio (অডিও)** | `content://media/external/audio/media` | ডিভাইসের এক্সটার্নাল স্টোরেজে থাকা সমস্ত অডিও/মিউজিক ফাইলের জন্য। |
| **Videos (ভিডিও)** | `content://media/external/video/media` | ডিভাইসের এক্সটার্নাল স্টোরেজে থাকা সমস্ত ভিডিও ফাইলের জন্য। |
| **Downloads (ডাউনলোড)** | `content://downloads/public_downloads` | পাবলিক ডাউনলোডের জন্য (Android 10+ এর জন্য বেশি প্রযোজ্য)। |
| **System Settings (সিস্টেম সেটিংস)** | `content://settings/system` | ডিভাইসের সিস্টেম সেটিংসের জন্য (যেমন রিংটোন, স্ক্রিন ব্রাইটনেস)। |
|  | `content://settings/secure` | সিকিউর সিস্টেম সেটিংসের জন্য (যেমন ADB, ইন্সটল সোর্স)। |
|  | `content://settings/global` | গ্লোবাল সিস্টেম সেটিংসের জন্য। |
| **MMS (মাল্টিমিডিয়া মেসেজ)** | `content://mms/` | সমস্ত MMS মেসেজের জন্য। |
| **Browser Bookmark/History (সাধারণ)** | `content://browser/bookmarks` | অ্যান্ড্রয়েডের ডিফল্ট বা সাধারণ ব্রাউজার বুকমার্ক/ইতিহাসের জন্য (ক্রোমের জন্য আলাদা)। |
</h6>



## Access all the system app databases using their respective Content Providers (URIs)

```
import subprocess

# 🔹 Contacts
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://contacts/phones/', '--projection', 'display_name:number'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://contacts/contacts'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://contacts/emails'])

# 🔹 SMS
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://sms/inbox/'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://sms/sent'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://sms/draft'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://sms/'])

# 🔹 Call Logs
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://call_log/calls/'])

# 🔹 Chrome Bookmarks/History
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://com.android.chrome.browser/bookmarks'])

# 🔹 Calendar
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://com.android.calendar/events'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://com.android.calendar/calendars'])

# 🔹 Images
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://media/external/images/media'])

# 🔹 Audio
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://media/external/audio/media'])

# 🔹 Videos
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://media/external/video/media'])

# 🔹 Downloads (public)
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://downloads/public_downloads'])

# 🔹 System Settings
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://settings/system'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://settings/secure'])
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://settings/global'])

# 🔹 MMS
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://mms/'])

# 🔹 Browser (Default Android Browser)
subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://browser/bookmarks'])
```
---

# 📦 Android App Database Sections (বাংলায়)

এই ডকুমেন্টে Android ডিভাইসের বিভিন্ন App ও System Database-এর বিস্তারিত তথ্য ও তাদের অবস্থান উল্লেখ করা হয়েছে। Rooted অথবা Developer Access থাকলে এই তথ্যগুলো ADB বা File Pull করে দেখা যায়।

---

## 🧑‍🤝‍🧑 1. Contacts

* **তথ্য:** নাম, নাম্বার, ইমেইল, কাস্টম ringtone, photo URI
* **DB Path:**

```
/data/data/com.android.providers.contacts/databases/contacts2.db
```

* **Tables:** contacts, raw\_contacts, data

---

## 📩 2. SMS / MMS

* **তথ্য:** Sender number, message body, timestamp, read status
* **DB Path:**

```
/data/data/com.android.providers.telephony/databases/mmssms.db
```

* **Tables:** sms, pdu, threads, canonical\_addresses

---

## 📞 3. Call Logs

* **তথ্য:** Call type (incoming, outgoing, missed), duration, number, date/time
* **DB Path:**

```
/data/data/com.android.providers.contacts/databases/calllog.db
```

* **Tables:** calls

---

## 🌐 4. Browser History (Chrome)

* **তথ্য:** URL, title, visit count, last visited
* **DB Path:**

```
/data/data/com.android.chrome/app_chrome/Default/History
```

* **Tables:** urls, visits

---

## 🗓️ 5. Calendar / Events

* **তথ্য:** Event title, description, location, start/end time
* **DB Path:**

```
/data/data/com.android.providers.calendar/databases/calendar.db
```

* **Tables:** events, calendars, attendees

---

## 💬 6. WhatsApp (Chat History)

* **তথ্য:** Message, media, sender/receiver ID, timestamps
* **DB Path:**

```
/data/data/com.whatsapp/databases/msgstore.db
```

* **Tables:** messages, chat\_list, media

---

## 🎵 7. Media Store (Music / Videos)

* **তথ্য:** song title, artist, album, duration
* **DB Path:**

```
/data/data/com.android.providers.media/databases/external.db
```

* **Tables:** audio, video, images

---

## 📂 8. Downloads

* **তথ্য:** filename, MIME type, status, download date
* **DB Path:**

```
/data/data/com.android.providers.downloads/databases/downloads.db
```

* **Tables:** downloads

---

## 🛠️ Access Commands:

```bash
adb root                           # Root access দরকার হলে
adb shell                         # ডিভাইসে প্রবেশ
adb pull <path/to/db>            # DB ফাইল পিসিতে টানো
sqlite3 file.db                  # ডেটাবেসে query চালাও
```

Example:

```bash
adb pull /data/data/com.whatsapp/databases/msgstore.db
sqlite3 msgstore.db
sqlite> .tables
sqlite> SELECT * FROM messages LIMIT 5;
```

---

## ⚠️ Note:

* Rooted ডিভাইস না হলে `/data/data/...` path এ access পাওয়া যায় না
* অনেক অ্যাপ (যেমনঃ Facebook, Banking apps) ডেটাবেস Encrypt করে রাখে
* Chrome DB দেখতে SQLite Viewer দরকার হয়

---

## ✅ Summary Table

| Section      | DB File          | Need Root | Example Table(s)     |
| ------------ | ---------------- | --------- | -------------------- |
| Contacts     | contacts2.db     | ❌ / ✅     | contacts, data       |
| SMS/MMS      | mmssms.db        | ✅         | sms, threads         |
| Call Logs    | calllog.db       | ✅         | calls                |
| Chrome Hist. | History (SQLite) | ✅         | urls, visits         |
| Calendar     | calendar.db      | ✅         | events               |
| WhatsApp     | msgstore.db      | ✅         | messages, chat\_list |
| Media Store  | external.db      | ❌ / ✅     | audio, video         |
| Downloads    | downloads.db     | ✅         | downloads            |

---

> 🧠 তৈরি করেছেন: [AN Mamun](https://anmamun0.vercel.app) — Android Forensics & Automation শেখার জন্যে ❤️
