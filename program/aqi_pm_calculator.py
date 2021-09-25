
def calculate_AQI(aqiLo, aqiHi, concLo, concHi, conc) -> int:
    return int((aqiHi - aqiLo) / (concHi - concLo) * (conc - concLo) + aqiLo)


def calc_pm10(conc) -> int:         # microgram/meter-cubed
    if 0 <= conc <= 50:
        calculate_AQI(0, 50, 0, 54, conc)
    elif 51 <= conc <= 100:
        calculate_AQI(51, 100, 55, 154, conc)
    elif 101 <= conc <= 150:
        calculate_AQI(101, 150, 155, 254, conc)
    elif 151 <= conc <= 200:
        calculate_AQI(151, 200, 255, 354, conc)
    elif 201 <= conc <= 300:
        calculate_AQI(201, 300, 355, 424, conc)
    elif 301 <= conc <= 500:
        calculate_AQI(301, 500, 425, 604, conc)


def calc_pm25(conc) -> int:         # micrograms/meter-cubed
    if 0 <= conc <= 50:
        calculate_AQI(0, 50, 0.0, 12.0, conc)
    elif 51 <= conc <= 100:
        calculate_AQI(51, 100, 12.1, 35.4, conc)
    elif 101 <= conc <= 150:
        calculate_AQI(101, 150, 155, 254, conc)
    elif 151 <= conc <= 200:
        calculate_AQI(151, 200, 255, 354, conc)
    elif 201 <= conc <= 300:
        calculate_AQI(201, 300, 355, 424, conc)
    elif 301 <= conc <= 500:
        calculate_AQI(301, 500, 425, 604, conc)
