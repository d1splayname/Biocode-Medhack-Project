def main():
    print("Team biocode")

    columnLables, cityDictionary = readDataFromFile()
    # print(columnLables)
    # print(cityDictionary)
    pass

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
            dataPoint = list(map(int, dataPoint))

            cityDictionary[cityName] = dataPoint

    return columnLables, cityDictionary


if __name__ == "__main__":
    main()
