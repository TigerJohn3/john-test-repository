import json
import requests

dictionary = {
    'happy': 'contentment with all',
    'mad': 'not accepting what is happening',
}

#print(dictionary['mad'])

dictionary['ecstacy'] = 'pure enlightment and bliss'

#print(dictionary)

dictionary.update({})

#for-loops

names = ['john', 'tyler', 'ryan', 'kurt']

for name in names:
    print(name)


# Functions

def full_name(first_name, last_name):
    return first_name + " " + last_name

result = full_name('john', 'hrabovsky')

print('The persons full name is:', result)


#######################################################
# ***CLASSES*** #
#######################################################


class House:
    rooms = None
    has_sauna = None

    def __init__(self, num_rooms, num_bathrooms, has_sauna):
        self.rooms = num_rooms
        self.bathrooms = num_bathrooms
        self.has_sauna = has_sauna

    def total_num_of_rooms(self):
        return self.rooms + self.bathrooms


# How you pass information into your class when you create it
# use the def __init__ method
john_house = House(num_rooms=12, num_bathrooms=4,has_sauna=True)
print('Rooms mentioned:', john_house.rooms)
print('Bathrooms mentioned:', john_house.bathrooms)
print('Is there a sauna?', john_house.has_sauna)
print('Total rooms and bathrooms:', john_house.total_num_of_rooms())

peter_house = House(num_rooms=3, num_bathrooms=2, has_sauna=False)
print("Peter's house has:", peter_house.rooms, "rooms.")


# This allows all properties that already exist for house to exist in hotel as well
class Hotel(House):
    pass


dudes_hotel = Hotel(num_rooms=56, num_bathrooms=60,has_sauna=True)
print("At Dude's Hotel, there are:", dudes_hotel.total_num_of_rooms(), "rooms and bathrooms.")

person = {
    "firstName": "John",
    "lastName": "Hrabovsky",
}

# Converts the person dictionary into a string format
string_person = json.dumps(person)
print(string_person)
print(type(string_person))

# Converts from json string back to dictionary format
dictonary_person = json.loads(string_person)
print(dictonary_person)
print(type(dictonary_person))
print('The first name of the person is:', dictonary_person['firstName'])

# Requests
response = requests.get('https://jsonplaceholder.typicode.com/todos')
print('\n \n')
print(response)
# Because we know todos returns json, we can run json on response
todos = response.json()

#API allows you to integrate with API and then pull data
for todo in todos:
    print(todo['title'])
