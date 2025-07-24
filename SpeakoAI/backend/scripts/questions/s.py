import json

with open("q2.json") as f:
    content = f.read()

# Remove last comma before ]
import re

fixed = re.sub(r',\s*]', ']', content)

# Validate JSON
try:
    data = json.loads(fixed)
    print("✅ JSON is valid now.")
    # Optionally write back to a clean file
    with open("cleaned.json", "w") as out:
        json.dump(data, out, indent=2)
except json.JSONDecodeError as e:
    print("❌ Still broken:", e)
# import json
#
# with open("q2.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#
# print(data[0])  # sanity check
