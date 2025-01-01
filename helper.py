import geoip2.database
from datetime import datetime
import pytz

GEOIP_DB_PATH = "GeoLite2-City.mmdb"

def get_location_data(client_ip):
    try:
        with geoip2.database.Reader(GEOIP_DB_PATH) as reader:
            # Use the 'city' method to get detailed location information
            response = reader.city(client_ip)
            
            # Extract location details
            location_data = {
                "country": response.country.name if response.country.name else "Unknown",  # Country name
                "region": response.subdivisions.most_specific.name if response.subdivisions else "Unknown",  # Region name (if available)
                "city": response.city.name if response.city else "Unknown",  # City name (if available)
                "timezone": response.location.time_zone if response.location.time_zone else "Unknown"  # Timezone (if available)
            }
            return location_data
            
    except geoip2.errors.AddressNotFoundError:
        # Handle the case where the IP address is not found in the database
        return {"error": "IP address not found in database"}
    except geoip2.errors.GeoIP2Error as e:
        # Handle other GeoIP2 errors
        return {"error": f"GeoIP2 error: {str(e)}"}
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


def get_user_time(timezone):
    try:
        if timezone:
            # Get the current time in the user's timezone
            tz = pytz.timezone(timezone)
            user_time = datetime.now(tz)

            # Convert it to a string without offset, just the timezone abbreviation
            return user_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        else:
            return "Unknown timezone"
    except pytz.UnknownTimeZoneError:
        return "Invalid timezone"


def get_server_time():
    # Get the current UTC time and convert it to a string
    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    return utc_time.strftime("%Y-%m-%d %H:%M:%S UTC")


def create_visitor_data(location_data, essay_id):
    # Get the user time as a string
    user_time = get_user_time(location_data.get("timezone"))
    
    # Get server time in UTC as a string
    server_time = get_server_time()

    data = {
        "location_data": location_data,
        "server_time": server_time,  # Server time in UTC
        "client_time": user_time,    # Client time in user's timezone
        "essay": essay_id,
    }

    return data


def add_visitor(db, client_ip, essay_id):
    try:
        location_data = get_location_data(client_ip)

        # If there is an error in location data, set it to None
        if "error" in location_data:
            location_data = None

        data = create_visitor_data(location_data, essay_id)

        data["ip_address"] = client_ip

        # Use .add() to automatically generate a document ID
        db.collection("visitors").add(data)

        return {"success": True, "message": "Visitor data added successfully"}

    except Exception as e:
        return {"success": False, "message": f"Error adding visitor data: {str(e)}"}

def check_essay_id(db, essay_id):
    doc_ref = db.collection("essays").document(essay_id)
    doc_snapshot = doc_ref.get()

    # Check if the document exists
    if doc_snapshot.exists:
        return doc_snapshot
    else:
        return False  # Document does not exist