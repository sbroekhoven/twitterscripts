import requests

# Making a get request
response = requests.get('https://api.twitter.com')

# print response
print(response)

# print elapsed time
print(response.elapsed)
print(response.elapsed.resolution)
