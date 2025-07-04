import subprocess
from tabulate import tabulate
from datetime import datetime

# ADB command run
result = subprocess.run(
    ['adb', 'shell', 'content', 'query', '--uri', 'content://call_log/calls'],
    capture_output=True, text=True, encoding='utf-8'
)

# sms Log History view
# adb', 'shell', 'content', 'query', '--uri', 'content://sms/

# Contact List Show
# content://contacts/phones/

# আউটপুট লাইন বাই লাইন ভাগ করা
output = result.stdout.strip().split('\n')

rows = []
toggle = 0

for line in output:
    if not line.startswith("Row:"):
        continue
    parts = line.split(' ', 2) 
    if len(parts) < 3:
        continue
    data_str = parts[2]
    data_items = data_str.split(' ')
    data_dict = {} 
    for item in data_items:
        if '=' in item:
            k, v = item.split('=', 1)
            data_dict[k] = v
    rows.append(data_dict)

# কল টাইপের মান বাংলায় দেখানোর জন্য ম্যাপিং (optional)
type_map = {
    '1': 'Incoming',
    '2': 'Outgoing',
    '3': 'Missed Call',
    '4': 'Voicemail',
    '5': 'Rejected/Other',
    '6': 'Outgoing (Forwarded)'
}


# প্রাসঙ্গিক কলাম নির্বাচন
columns = ['number', 'date', 'duration', 'type']

# Timestamp formating and Call Type Converting 
for row in rows:
    if 'date' in row:
        try:
            ts = int(row['date']) // 1000
            row['date'] = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        except:
            pass
    if 'type' in row:
        row['type'] = type_map.get(row['type'], row['type'])
        
for a , b in rows[0].items():
    print(a)

# Convert Table Formate 
table_str = tabulate(rows, headers='keys', tablefmt='grid')

# Createing File
with open('call_log.txt', 'w', encoding='utf-8') as f:
    f.write(table_str)

print("Call log saved to call_log.txt")