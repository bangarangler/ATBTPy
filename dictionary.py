# DICTIONARY

myCat = {
    "size": "fat",
    "color": "gray",
    "disposition": "loud"
}

print(myCat['size'])
print(f"My cat has {myCat['color']} fur!")

eggs = {"name":"Zophie","species":"cat","age":8}

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k,v)

print('cat' in myCat.values())
print(eggs.get('colors', 0))

print(list(eggs.keys()))
print(list(eggs.values()))

picnicItems = {'apples': 5, 'cups':2}
print(f"I am bringing {picnicItems.get("napkins",0)}, to the picnic")
