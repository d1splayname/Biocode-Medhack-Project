def readDataFromFile():
    airQualityFileName = "AirQualityDataPoints.csv"

    columnLables = []
    cityDictionary = {}

    with open(airQualityFileName, "r") as file:
        # read column labels
        columnLables = file.readline().rstrip().split(",")

        # read and parse in data
        dataLines = file.readlines()
        for line in dataLines:
            splitLine = line.split(",")

            cityName, dataPoint = splitLine[0], splitLine[1:]
            dataPoint = list(map(float, dataPoint))

            cityDictionary[cityName] = dataPoint

    return columnLables, cityDictionary


def getLatLon():
    _, cityDict = readDataFromFile()
    cities = [i for i in cityDict]
    lat = [cityDict[i][7] for i in cityDict]
    lon = [cityDict[i][8] for i in cityDict]
    return cities, lat, lon
