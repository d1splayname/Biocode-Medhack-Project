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
def cautionary_statement(aqi_level) -> str:
    if aqi_level == "Good":
        return "None"
    elif aqi_level == "Moderate":
        return "Active children and adults, and people with respiratory disease, such as asthma, should limit " \
               "prolonged outdoor exertion."
    elif aqi_level == "Unhealthy for Sensitive Groups":
        return "Active children and adults, and people with respiratory disease, such as asthma, should avoid " \
               "prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor " \
               "exertion."
    elif aqi_level == "Unhealthy" or aqi_level == "Very Unhealthy":
        return "Active children and adults, and people with respiratory disease, such as asthma, should avoid all " \
               "outdoor exertion; everyone else, especially children, should limit outdoor exertion."
    elif aqi_level == "Hazardous":
        return "Everyone should avoid all outdoor exertion."

