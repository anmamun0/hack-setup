# 🐒 Android Monkey Tool

## 🐵 Monkey কী?

**Monkey** হলো Android-এর একটি testing tool, যা অ্যাপের মধ্যে এলোমেলো (random) ভাবে user event পাঠিয়ে অ্যাপের stability পরীক্ষা করে।

এটি Android SDK-এর অংশ এবং `adb shell` কমান্ড দিয়ে চালানো যায়।

---

## 🎯 কেন Monkey ব্যবহার করা হয়?

- অ্যাপ ক্র্যাশ হয় কিনা সেটা দেখার জন্য
- অ্যাপ ফ্রিজ বা ল্যাগ হয় কিনা বোঝার জন্য
- অ্যাপের বিভিন্ন UI-তে touch, scroll, button press ইত্যাদি ইভেন্ট simulate করতে
- UI automation এবং stress testing এর জন্য

---

## 🧪 Monkey কিভাবে কাজ করে?

Monkey অ্যাপ চালিয়ে অসংখ্য random UI event পাঠায়, যেমন:

- ✅ Touch
- ✅ Scroll
- ✅ Volume press
- ✅ Menu press
- ✅ Back button
- ✅ Screen rotate
- ✅ অন্যান্য user interaction

এগুলো simulate করে যেন মনে হয় অ্যাপ একজন রিয়েল ইউজার ব্যবহার করছে। এর ফলে অ্যাপের স্টেবিলিটি বোঝা যায়।

---

### 🔧 Monkey এর সাধারণ কমান্ড

```bash
adb shell monkey -p com.facebook.katana -c android.intent.category.LAUNCHER 1
```

| অংশ  | কাজ                                       |
| ---- | ------------------------------------------- |
| `-p` | কোন অ্যাপের উপর monkey চালাবে (প্যাকেজ নাম) |
| `-c` | কোন ক্যাটাগরি থেকে চালাবে (Launcher)        |
| `1`  | কতটি event পাঠাবে (এখানে 1 বার চালাবে)      |


### 📝 আরেকটি উদাহরণ:

```bash 
adb shell monkey -p com.instagram.android -v 500
``` 
###### → Instagram অ্যাপে ৫০০টা random event পাঠাবে।

### 🧠 Monkey এর কিছু গুরুত্বপূর্ণ অপশন:

| অপশন             | ব্যাখ্যা                                |
| ---------------- | --------------------------------------- |
| `-p`             | টার্গেট অ্যাপের প্যাকেজ                 |
| `-v`             | Verbose — কি হচ্ছে সেটা দেখায়           |
| `--pct-touch 80` | টাচ ইভেন্টের শতকরা হার বাড়ায়            |
| `--throttle 500` | প্রতিটি event এর মাঝে 500ms গ্যাপ       |
| `-s`             | Random seed ব্যবহার করে repeatable test |

### সতর্কতা:
- এটা random ইভেন্ট পাঠায়, তাই গুরুত্বপূর্ণ অ্যাপে চালালে ডেটা মুছে ফেলতেও পারে!
- শুধুমাত্র testing বা automation উদ্দেশ্যে ব্যবহার করো।


```
# Facebook অ্যাপ হোম স্ক্রিন থেকে চালাবে।
adb shell monkey -p com.facebook.katana -c android.intent.category.LAUNCHER 1

# YouTube অ্যাপ চালানো
adb shell am start -n com.google.android.youtube/.HomeActivity
```

তুমি ঠিক ধরেছো — Facebook অ্যাপ চালাতে আমরা monkey ইউজ করেছি, আর YouTube-এর জন্য am start।
দুটোই অ্যাপ চালাতে পারে, কিন্তু তারা আলাদা context-এ কাজ করে।

পার্থক্য ব্যাখ্যা:
<h6> 

| বিষয়                 | `monkey`                                                  | `am start`                                                     |
| -------------------- | ----------------------------------|------------------------- |
| ⚙️ Tool এর নাম       | UI/Application Exerciser Monkey         | Activity Manager (AM) |
| 🧠 উদ্দেশ্য          | Random UI ইভেন্ট simulate করতে, user behavior emulate করা | নির্দিষ্ট অ্যাপ/Activity চালানো  |
| 🎯 Target         | শুধুমাত্র অ্যাপ Package চালানো  | নির্দিষ্ট `Activity`, `Intent`, `Data` সহ চালানো যায়           |
| 🧪 Random Input | দেয় (যেমন: tap, swipe) — testing এর জন্য    | না — শুধু অ্যাপ চালায়, কোনো UI event simulate করে না|
| 📱 ইউজ কবে করবো? | Just অ্যাপ চালাতে চাইলে সহজভাবে (e.g. home launcher থেকে) | Specific Activity বা Intent চালাতে চাইলে|
| ⛓️ Component Control | Limited — শুধু অ্যাপ চালায় | Full Control — Activity, data, MIME type, extra সব সেট করা যায় |
| 🧑‍💻 Syntax  | `adb shell monkey -p <package> -c <category> 1`  | `adb shell am start -n <component>` অথবা `-a`, `-d`, `-t`, etc |


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


####  কোনটা কবে ব্যবহার করবে?

| প্রয়োজন                                       | টুল ব্যবহার |
| --------------------------------------------- | ----------- |
| শুধু অ্যাপ চালাতে হবে                         | `monkey`    |
| স্পেসিফিক স্ক্রিন বা intent/action চালাতে হবে | `am start`  |
| automation বা testing করতে হবে                | `monkey`    |
| deep linking বা intent manipulation করতে হবে  | `am start`  |


</h6>

### 🐒 8. Monkey Command Reference
| কাজ                                     | কমান্ড                                                                       | বর্ণনা                                                                           |
| ----------------- | ------------------------------ | --------------------------------------------- |
| অ্যাপ চালু করো (shortcut method)  | `adb shell monkey -p com.package.name -c android.intent.category.LAUNCHER 1` | অ্যাপ লঞ্চ করার সহজ উপায়, মূল অ্যাপ চালায় |
| নির্দিষ্ট অ্যাপের উপর Monkey Test চালাও | `adb shell monkey -p com.package.name -v <events>`| নির্দিষ্ট অ্যাপে র‍্যান্ডম ইনপুট ইভেন্ট দিয়ে টেস্ট করে  |
| Monkey Test চালাও নির্দিষ্ট থ্রোটল দিয়ে | `adb shell monkey --throttle <ms> -p com.package.name -v <events>`| ইভেন্টের মধ্যে specified মিলিসেকেন্ড অপেক্ষা করে টেস্ট চালায় |
| Monkey Test verbose mode চালাও | `adb shell monkey -v -v -p com.package.name <events>` | টেস্ট চলাকালীন বিস্তারিত লগ দেখায়    |  
| সিস্টেম-wide Monkey Stress Test চালাও | `adb shell monkey --throttle 500 -v -v -v 1000`   | পুরো সিস্টেমে ১০০০ ইভেন্ট দিয়ে স্ট্রেস টেস্ট চালায়|
| Monkey Test চালাও random seed দিয়ে| `adb shell monkey --seed <number> -p com.package.name -v <events>` | নির্দিষ্ট seed ব্যবহার করে টেস্ট চালায় (repeatable test)|
| Monkey Test stop on crash | `adb shell monkey --monitor-native-crashes -p com.package.name -v <events>`  | ক্র্যাশ হলে টেস্ট থামিয়ে দেয়|
| Monkey Test stop on ANR| `adb shell monkey --monitor-crashes -p com.package.name -v <events>` | ANR (Application Not Responding) হলে টেস্ট থামায়|
| Monkey Test random throttle (min-max)  | `adb shell monkey --throttle <min>-<max> -p com.package.name -v <events>`| ইভেন্টের মাঝে র‍্যান্ডম অপেক্ষা সময় (মিনিমাম থেকে ম্যাক্সিমাম) ব্যবহার করে টেস্ট |