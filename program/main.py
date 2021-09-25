import readData


def main():
    print("Team BioCode+")

    columnLabels, cityDictionary = readData.readDataFromFile()

    # pretty print data
    print(columnLabels)
    for city in cityDictionary:
        print(city + ": " + str(cityDictionary[city]) + " " + str(len(cityDictionary[city])))


if __name__ == "__main__":
    main()
