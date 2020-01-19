from libs.api_lib import ApiClient
print('from .libs.api_lib import ApiClient')

client = ApiClient(base_url='http://localhost:8000/api')
print("client = ApiClient(base_url='http://localhost:8000/api')")

response = client.login(login='admin', password='1111')
print("client.login(login='admin', password='1111')")
print(response)

assert(client.token)
print('assert(client.token)')

publications = client.get_publications()
print('publications = client.get_publications()')
print(publications)

categories = client.get_categories()
print('categories = client.get_categories()')
print(categories)

publication = client.get_publication(id=1)
print('publication = client.get_publication(id=1)')
print(publication)

category = client.get_category(id=1)
print('category = client.get_category(id=1)')
print(category)

response = client.update_category(data=category)
print('client.update_category(data=category)')
print(response)

response = client.update_publication(data=publication)
print('client.update_publication(data=publication)')
print(response)

response = client.create_category(data=category)
print('client.create_category(data=category)')
print(response)

response = client.create_publication(data=publication)
print('client.create_publication(data=publication)')
print(response)

client.token = ''
print('client.token = ''')

response = client.get_publications()
print('response = client.get_publications()')
print(response)

assert(response=='401 Unauthorized')
print("assert(response=='401 Unauthorized')")

print('SUCCESS! ALL TESTS PASSES')