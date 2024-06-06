import requests
from ipinfo import getHandler

# Function to automatically detect the user's IP address
def get_my_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

# Function to get the country from IP address using ipinfo
def get_country_from_ip(ip_address):
    handler = getHandler('443dea1a32ed7b') # access token from the ipinfo website
    details = handler.getDetails(ip_address)
    return details.country_name

# Main execution logic
if __name__ == '__main__':
    my_ip = get_my_ip()
    country = get_country_from_ip(my_ip)
    print(f"The country of IP address {my_ip} is {country}")


# Automatic IP Detection: The function get_my_ip() makes a request to api.ipify.org,
# which returns the public IP address of the device running the script.
# Country Lookup: The function get_country_from_ip() uses the ipinfo handler 
# to fetch geolocation details for a given IP address and extract the country name.