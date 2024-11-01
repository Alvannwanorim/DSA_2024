from urllib.parse import urlparse, parse_qs
from urllib.request import Request, urlopen
import urllib.error as err
# url ="hhtps://example.com/employees/name/?salary>=2500&age=30"
# parsed_url = urlparse(url)
# print(type(parsed_url))
# print(parsed_url)
# print("Scheme:",parsed_url.scheme)
# print("netloc:",parsed_url.netloc)
# print("path:",parsed_url.path)
# print("params:",parsed_url.params)
# print("Query string:",parsed_url.query)
# print("Fragment:",parsed_url.fragment)

# dct = parse_qs(parsed_url.query)
# print(dct)

obj = Request("https://www.tutorialspoint.com/")
resp = urlopen(obj)
data = resp.read()
print(data)