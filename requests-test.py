import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Felis_catus-cat_on_snow.jpg/1280px-Felis_catus-cat_on_snow.jpg"

response = requests.get(url)

#print(response)

if response.status_code == 200:
    with open("image.jpg", "wb") as file:
        file.write(response.content)
