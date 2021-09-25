# Function that convert air quality index to a qualifying category
def qualify_aqi(aqi) -> str:
    if 0 <= aqi <= 50:
        return "Good"
    elif 51 <= aqi <= 100:
        return "Moderate"
    elif 101 <= aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif 151 <= aqi <= 200:
        return "Unhealthy"
    elif 201 <= aqi <= 300:
        return "Very Unhealthy"
    elif 301 <= aqi <= 500:
        return "Hazardous"


# function that gives a cautionary statement based on the current AQI
def cautionary_statement(aqi) -> str:
    if 0 <= aqi <= 50:
        return "Good AQI."
    elif 51 <= aqi <= 150:
        return "Active children and adults, and people with respiratory disease, such as asthma, should limit " \
               "prolonged outdoor exertion."
    elif 151 <= aqi <= 200:
        return "Active children and adults, and people with respiratory disease, such as asthma, should avoid " \
               "prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor " \
               "exertion."
    elif 201 <= aqi <= 300:
        return "Active children and adults, and people with respiratory disease, such as asthma, should avoid all " \
               "outdoor exertion; everyone else, especially children, should limit outdoor exertion."
    elif 301 <= aqi <= 500:
        return "Everyone should avoid all outdoor exertion."

