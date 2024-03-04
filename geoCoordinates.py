from geopy.geocoders import Nominatim

def get_coordinates(city):
    # Create a geolocator object with a specified user agent
    geolocator = Nominatim(user_agent="user")
    # Use the geolocator to geocode the provided city
    location = geolocator.geocode(city)

    # Check if location is found
    if location:
        # Extract latitude and longitude from the location object
        latitude = location.latitude
        longitude = location.longitude
        # Return latitude and longitude
        return latitude, longitude
    else:
        # If location is not found, return None
        return None

# Example of usage
city = input("Enter the name of the city: ")
coordinates = get_coordinates(city)

# Check if coordinates are obtained
if coordinates:
    latitude, longitude = coordinates
    # Print latitude and longitude of the city
    print(f"The latitude of {city} is {latitude}")
    print(f"The longitude of {city} is {longitude}")
else:
    # If coordinates are not obtained, print a message
    print(f"Unable to find coordinates for {city}")




