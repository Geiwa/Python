import requests

response = requests.get('https://api.github.com/events')

print(response.status_code)




# response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(response.text)


# response = requests.get('https://httpbin.org/')
# print(response.text)



# response = requests.get('https://www.kivano.kg/')

# print(response.text)
