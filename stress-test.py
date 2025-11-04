# stress-test.py
import os

print("=== STRESS TEST WEBSITE BY GITHUB ===")
url = input("Nhập URL website của bạn (vd: https://example.com): ").strip()
if not url.startswith("http"):
    url = "https://" + url

print("\nChọn mức độ mạnh:")
print("1. Nhẹ (100 user)")
print("2. Trung bình (500 user)")
print("3. Mạnh (1000 user)")
print("4. SIÊU MẠNH (5000 user)")

level = input("Chọn (1-4): ").strip()

targets = { "1": 100, "2": 500, "3": 1000, "4": 5000 }
target = targets.get(level, 1000)

# Tạo k6-script.js
k6_script = f'''import http from 'k6/http';
import {{ check, sleep }} from 'k6';
import {{ htmlReport }} from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';
import {{ textSummary }} from 'https://jslib.k6.io/k6-summary/0.0.1/index.js';

export let options = {{
  stages: [
    {{ duration: '30s', target: {target} }},
    {{ duration: '1m', target: {target} }},
    {{ duration: '30s', target: 0 }},
  ],
}};

export default function () {{
  let res = http.get('{url}');
  check(res, {{ 'status 200': (r) => r.status === 200 }});
  sleep(1);
}}

export function handleSummary(data) {{
  return {{
    'report.html': htmlReport(data),
    'stdout': textSummary(data, {{ indent: ' ', enableColors: true }}),
  }};
}}
'''

with open("k6-script.js", "w") as f:
    f.write(k6_script)

print(f"\nĐã tạo file k6-script.js với {target} user!")
print("Bây giờ đẩy lên GitHub và chạy Actions!")
