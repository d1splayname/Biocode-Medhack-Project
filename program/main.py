import qualify_data
import aqi_pm_calculator
import readData


def main():
    print("Team BioCode+")

    columnLables, cityDictionary = readData.readDataFromFile()

    """
    print(columnLables)
    for city in cityDictionary:
        print(city + ": " + str(cityDictionary[city]) + " " + str(len(cityDictionary[city])))
    """
    pass


if __name__ == "__main__":
    main()
