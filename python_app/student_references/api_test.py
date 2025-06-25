import requests

url = "https://potterapi-fedeperin.vercel.app/en/houses"

response = requests.get(url)

if response.status_code == 200:
    houses = response.json()
    #print(response.content)
    for house in houses:
        print(f"House: {house["house"]}, Founder: {house["founder"]}")
else: 
    print(f"Failed to retrieve data:{response.status_code}")