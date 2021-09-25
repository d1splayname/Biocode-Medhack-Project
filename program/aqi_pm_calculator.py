
def calculate_AQI(aqiLo, aqiHi, concLo, concHi, conc):
    return int((aqiHi - aqiLo) / (concHi - concLo) * (conc - concLo) + aqiLo)


def calc_pm10(conc):         # microgram/meter-cubed
    if 0 <= conc <= 54:
        return calculate_AQI(0, 50, 0, 54, conc)
    elif 55 <= conc <= 154:
        return calculate_AQI(51, 100, 55, 154, conc)
    elif 155 <= conc <= 254:
        return calculate_AQI(101, 150, 155, 254, conc)
    elif 255 <= conc <= 354:
        return calculate_AQI(151, 200, 255, 354, conc)
    elif 355 <= conc <= 424:
        return calculate_AQI(201, 300, 355, 424, conc)
    elif 425 <= conc <= 604:
        return calculate_AQI(301, 500, 425, 604, conc)


def calc_pm25(conc):         # micrograms/meter-cubed
    if 0.0 <= conc <= 12.0:
        return calculate_AQI(0, 50, 0.0, 12.0, conc)
    elif 12.1 <= conc <= 35.4:
        return calculate_AQI(51, 100, 12.1, 35.4, conc)
    elif 35.5 <= conc <= 55.4:
        return calculate_AQI(101, 150, 155, 254, conc)
    elif 55.5 <= conc <= 150.4:
        return calculate_AQI(151, 200, 255, 354, conc)
    elif 150.5 <= conc <= 250.4:
        return calculate_AQI(201, 300, 355, 424, conc)
    elif 250.5 <= conc <= 500.5:
        return calculate_AQI(301, 500, 425, 604, conc)


