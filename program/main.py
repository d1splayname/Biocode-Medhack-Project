def main():
    # print("Team biocode")
    columnLables, cityDictionary = readDataFromFile()
    print(columnLables)
    print(cityDictionary)
    pass

def readDataFromFile():
    airQualityFileName = "AirQualityDataPoints.txt"

    columnLables = []
    cityDictionary = {}

    with open(airQualityFileName, "r") as file:
        # read column labels
        columnLables = file.readline().split(",")

        # read and parse in data
        dataLines = file.readlines().split("/n")
        for line in dataLines:
            cityName, dataPoint = file.readline().split(",")
            dataPoint = map(int, dataPoint)

            cityDictionary[cityName] = dataPoint

    return columnLables, cityDictionary

if __name__ == "__main__":
    main()
