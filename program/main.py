import qualify_data
import aqi_pm_calculator
import readData


def main():
    print("Team BioCode+")

    columnLabels, cityDictionary = readData.readDataFromFile()


    print(columnLabels)
    for city in cityDictionary:
        print(city + ": " + str(cityDictionary[city]) + " " + str(len(cityDictionary[city])))

    pass


if __name__ == "__main__":
    main()
