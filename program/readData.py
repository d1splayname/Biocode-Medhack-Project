def readDataFromFile():
    airQualityFileName = "AirQualityDataPoints.csv"

    columnLabels = []
    cityDictionary = {}

    with open(airQualityFileName, "r") as file:
        # read column labels
        columnLabels = file.readline().rstrip().split(",")

        # read and parse in data
        dataLines = file.readlines()
        for line in dataLines:
            splitLine = line.split(",")

            cityName, dataPoint = splitLine[0], splitLine[1:]
            dataPoint = list(map(float, dataPoint))

            cityDictionary[cityName] = dataPoint

    return columnLabels, cityDictionary


def getLatLon():
    _, cityDict = readDataFromFile()
    cities = [i for i in cityDict]
    lat = [cityDict[i][7] for i in cityDict]
    lon = [cityDict[i][8] for i in cityDict]
    return cities, lat, lon


def getAQIs():
    columns, cityDict = readDataFromFile()
    cities = [i for i in cityDict]
    aqi = [cityDict[i][0] for i in cityDict]
    pm10 = [cityDict[i][1] for i in cityDict]
    pm25 = [cityDict[i][2] for i in cityDict]
    o3 = [cityDict[i][3] for i in cityDict]
    so2 = [cityDict[i][4] for i in cityDict]
    no2 = [cityDict[i][5] for i in cityDict]
    co = [cityDict[i][6] for i in cityDict]
    return cities, aqi, pm10, pm25, o3, so2, no2, co