import requests

print("Hello, World!")
re =requests.get('http://www.baidu.com')
print(re.content)