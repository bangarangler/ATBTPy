import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(res.raise_for_status())
print(res.status_code)
print(len(res.text))
print(res.text[:500])

playFile = open("RomeoAndJuliet.txt", 'wb')
for chunk in res.iter_content(1000000):
    playFile.write(chunk)

playFile.close()

