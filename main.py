import phonenumbers
import opencage
import folium
from phonenumbers import geocoder, carrier

from opencage.geocoder import OpenCageGeocode

number = input("Enter phone number with country code (+91): ")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
service_provider = phonenumbers.parse(number)

print(location)
print(carrier.name_for_number(service_provider, "en"))

key = '4a6b05cf15e84f329aa8f5f16aea87b3'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save('mylocation.html')
