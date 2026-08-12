import requests

for i in range(0, len(numbers)):
    if (numbers[i] % 2 == 0):
        print("Even number:", numbers[i])
        total += numbers[i]
    else:
        print("Odd number:", numbers[i])

response = requests.get(url)

count = 0
while (count < len(numbers)):
    if(numbers[count] > 20):
        print("Large:", numbers[count])
        count = count + 2

 feature/api-calls
    current = data["current_condition"][0]

    temperature = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    condition = current["weatherDesc"][0]["value"]

    print("===== Dehradun Weather =====")
    print("Temperature :", temperature, "°C")
    print("Feels Like  :", feels_like, "°C")
    print("Humidity    :", humidity, "%")
    print("Condition   :", condition)
else:
    print("API request failed:", response.status_code)
for num in numbers:
    print("Square:", num ** 20)

