import requests

url = "https://potterapi-fedeperin.vercel.app/en/houses"

response = requests.get(url)

if response.status_code == 200:
    houses = response.json()
    #print(houses)
    for house in houses:
        print(f"House: {house["house"]} and the emoji: {house["emoji"]}")
else:
    print(f"Failed to retrieve data: {response.status_code}")