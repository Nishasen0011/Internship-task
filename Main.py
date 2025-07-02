import json, datetime, unittest

with open("data-1.json") as f:
    data1 = json.load(f)
with open("data-2.json") as f:
    data2 = json.load(f)
with open("data-result.json") as f:
    expected = json.load(f)

def convert1(d):
    dt = datetime.datetime.fromisoformat(d["time"].replace("Z","+00:00"))
    return {"deviceId": d["device-id"], "temperature": d["temperature"], "humidity": d["humidity"], "timestamp": int(dt.timestamp()*1000)}

def convert2(d):
    return {"deviceId": d["device"], "temperature": d["air"]["temperature"], "humidity": d["air"]["humidity"], "timestamp": d["timestamp"]}

def main(d):
    return convert2(d) if d.get("air") else convert1(d)

class Test(unittest.TestCase):
    def test1(self): self.assertEqual(main(data1), expected)
    def test2(self): self.assertEqual(main(data2), expected)

if __name__ == "__main__":
    unittest.main()
