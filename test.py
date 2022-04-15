from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/5').json())
print(get('http://localhost:5000/api/v2/users/52').json())  # нет пользователя
print(get('http://localhost:5000/api/v2/users/g').json())  # не число

print(post('http://localhost:5000/api/v2/users').json())  # нет словаря
print(post('http://localhost:5000/api/v2/users', json={"name": "Sanya"}).json())
print(post("http://localhost:5000/api/v2/users", json={"name": "Sanya",
                                                       "surname": "Wolf", "age": 17, 'contacts': '2343',
                                                       "hashed_password": "wolf", "email": "wolf@mars.org"}).json())

print(delete('http://localhost:5000/api/v2/goods/999').json())
print(delete('http://localhost:5000/api/v2/goods/10').json())

print(get('http://localhost:5000/api/v2/goods').json())
print(get('http://localhost:5000/api/v2/goods/5').json())
print(get('http://localhost:5000/api/v2/goods/52').json())  # нет пользователя
print(get('http://localhost:5000/api/v2/goods/g').json())  # не число

print(post('http://localhost:5000/api/v2/goods').json())  # нет словаря
print(post('http://localhost:5000/api/v2/goods', json={"good": "Good1"}).json())
print(post("http://localhost:5000/api/v2/goods", json={"good": "Good1", "price": 1,
                                                       "description": "computer", 'contacts': '34356'}).json())

print(delete('http://localhost:5000/api/v2/goods/999').json())
print(delete('http://localhost:5000/api/v2/goods/10').json())
