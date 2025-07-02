# মোবাইলের ডেটা ল্যাপটপে এক্সেস করার সহজ উপায় (যদি একই WiFi থাকে)

এই গাইডে দেখানো হবে কীভাবে একই WiFi নেটওয়ার্কে থাকা অবস্থায় মোবাইল ডিভাইস থেকে ল্যাপটপে সহজে ডেটা এক্সেস করা যায়।


```
C:\Users\almam>nmap -sn 192.168.1.149-198
Starting Nmap 7.97 ( https://nmap.org ) at 2025-07-03 00:44 +0600
Nmap scan report for host.docker.internal (192.168.1.149)
Host is up.

Nmap scan report for 192.168.1.190
Host is up (0.12s latency).
MAC Address: B0:18:B7:8F:24:34 (Samsung Electronics)

Nmap scan report for 192.168.1.198
Host is up (0.071s latency).
MAC Address: A6:2A:75:FF:45:BE (Unknown)

Nmap done: 50 IP addresses (3 hosts up) scanned in 14.60 seconds
```

-- আমি 192.168.1.190 এই Ip access devise এর data কি করে আমার leptop এ নিযে আসবো


## Step 1: বুঝে নাও – 192.168.1.190 কোন ধরনের ডিভাইস?
যেহেতু MAC address বলছে Samsung Electronics, এটা সাধারণত হয়:

✅ Android ফোন
✅ Samsung Smart TV
✅ ট্যাবলেট / IoT Device

তুমি যদি নিশ্চিত হও এটা Samsung মোবাইল ফোন, তাহলে  

## Step 2: মোবাইল থেকে ল্যাপটপে ডেটা আনার ৩টি সহজ পদ্ধতি
### 🔹 পদ্ধতি ১: ফোনে FTP Server চালাও (সবচেয়ে সহজ)
#### 🔧 ফোনে যা করতে হবে:
- Play Store থেকে এই অ্যাপটি ইনস্টল করো: FTP Server
- অ্যাপ ওপেন করে "Start Server" চাপো।
- তুমি একটা FTP URL দেখতে পাবে, যেমন:

```cpp 
ftp://192.168.1.190:2221
```

### 💻 ল্যাপটপে যা করতে হবে:
- Windows File Explorer-এ এই URL টাইপ করো:
```cpp 
ftp://192.168.1.190:2221
```
or
```perl
ftp://android:android@192.168.1.190:2221
```

#### অথবা CMD-তে:
```bash 
start ftp://192.168.1.190:2121
```
##### ➡️ ফাইল ব্রাউজ করে কপি করে নিতে পারো!





## 🔹 পদ্ধতি ২: Xender / ShareIt / Snapdrop দিয়ে
### ফোনে:
- Snapdrop.net খুলো Chrome-এ।

###  ল্যাপটপে:
একই WiFi-তে থেকে ল্যাপটপেও সেই সাইটে ঢোকো।
➡️ যেকোনো ফাইল ল্যাপটপে ট্রান্সফার করতে পারবে সহজে।


### 🔹 পদ্ধতি ৩: মোবাইলে Python HTTP সার্ভার চালাও (চাইলেই)

মোবাইলে **Pydroid 3** ইনস্টল করে রান করো:

```python
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
```


 
### ➡️ তারপর ল্যাপটপে ওপেন করো:

```cpp 
http://192.168.1.190:8000
```

#### 🛑 গুরুত্বপূর্ণ টিপস:
- মোবাইল ও ল্যাপটপ একই WiFi নেটওয়ার্কে থাকতে হবে।
- মোবাইলে থাকা Data Saver, VPN, Firewall অফ রাখলে স্ক্যানিং ও সংযোগ ভালো কাজ করে।
- চাইলে Termux + openssh দিয়ে SSH চালিয়ে ফাইল আনতে পারো — চাইলে আমি সেটা নিয়েও গাইড করতে পারি।
