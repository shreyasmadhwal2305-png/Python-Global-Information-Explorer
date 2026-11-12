# API Pagination

import requests
import time
import json


# PART 1 - PROGRAM INTRODUCTION

print("=" * 45)
print("       GLOBAL INFORMATION EXPLORER")
print("=" * 45)


# PART 2 - API CONFIGURATION
# World Bank API provides information about countries.

url = "https://api.worldbank.org/v2/country"

# Request up to 300 records per page.
per_page = 300


# PART 3 - FETCH API PAGINATION INFORMATION

parameters = {
    "format": "json",
    "page": 1,
    "per_page": per_page
}

print("\nCONNECTING TO WORLD BANK API...")

try:

    response = requests.get(
        url,
        params=parameters,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    metadata = data[0]
    total_pages = metadata["pages"]

    print("API connection successful!")

    print("\nPAGINATION INFORMATION")
    print("----------------------")
    print("Total Pages:", total_pages)
    print("Records Per Page:", per_page)


# PART 4 - AUTOMATIC PAGINATION AND DATA COLLECTION

    all_countries = []

    for page in range(1, total_pages + 1):

        print(f"\nFetching page {page} of {total_pages}...")

        parameters = {
            "format": "json",
            "page": page,
            "per_page": per_page
        }

        # Retry temporary API failures up to three times.
        for attempt in range(1, 4):

            try:

                response = requests.get(
                    url,
                    params=parameters,
                    timeout=15
                )

                response.raise_for_status()
                data = response.json()
                break

            except requests.exceptions.Timeout:

                if attempt < 3:
                    print("Request timed out. Retrying...")
                    time.sleep(2)
                else:
                    raise

            except requests.exceptions.HTTPError:

                if response.status_code in (502, 503, 504) and attempt < 3:
                    print("Temporary server error. Retrying...")
                    time.sleep(2)
                else:
                    raise

        countries = data[1]

        # Store all records from this page.
        all_countries.extend(countries)

        print("Records received:", len(countries))


# PART 5 - DATA COLLECTION SUMMARY

    print("\nDATA COLLECTION SUMMARY")
    print("-----------------------")
    print("Total country records collected:", len(all_countries))


# PART 6 - PREPARE COUNTRY DATA

    # Aggregate records represent regions or income groups,
    # not individual geographical countries.
    geographical_countries = []

    for country in all_countries:

        if country["region"]["value"].strip() != "Aggregates":
            geographical_countries.append(country)


# PART 7 - REGION DISTRIBUTION ANALYSIS

    region_counts = {}

    for country in geographical_countries:

        region = country["region"]["value"].strip()

        if region not in region_counts:
            region_counts[region] = 0

        region_counts[region] += 1

    print("\nCOUNTRY DISTRIBUTION BY REGION")
    print("------------------------------")

    for region, count in region_counts.items():
        print(f"{region}: {count}")


# PART 8 - CAPITAL CITY ANALYSIS

    countries_with_capital = 0
    countries_without_capital = 0

    for country in geographical_countries:

        if country["capitalCity"]:
            countries_with_capital += 1
        else:
            countries_without_capital += 1

    print("\nCAPITAL CITY ANALYSIS")
    print("---------------------")
    print("Countries with a capital:", countries_with_capital)
    print("Countries without a capital:", countries_without_capital)
    print("Total geographical records:", len(geographical_countries))


# PART 9 - SAVE COUNTRY DATA TO JSON

    with open("countries_data.json", "w", encoding="utf-8") as file:

        json.dump(
            all_countries,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nDATA SAVING")
    print("-----------")
    print("Country data saved to countries_data.json")


# PART 10 - LOAD SAVED JSON DATA

    with open("countries_data.json", "r", encoding="utf-8") as file:

        saved_countries = json.load(file)

    print("\nSAVED DATA VERIFICATION")
    print("-----------------------")
    print("Total saved records:", len(saved_countries))

    for country in saved_countries[:3]:

        print("\nCountry:", country["name"])
        print("Capital:", country["capitalCity"])
        print("Region:", country["region"]["value"])


# PART 11 - CONTINUOUS COUNTRY SEARCH

    while True:

        print("\nCOUNTRY SEARCH")
        print("--------------")
        print("Enter 0 to exit the program.")

        search_name = input(
            "\nEnter a country name: "
        ).strip().lower()

        # Exit the program.
        if search_name == "0":

            print("\nThank you for using Global Information Explorer!")
            print("Exiting program...")
            break

        # Reject empty input.
        if not search_name:

            print("Please enter a country name.")
            continue

        found = False

        for country in saved_countries:

            if country["region"]["value"].strip() == "Aggregates":
                continue

            # Partial matching allows searches such as "ind".
            if search_name in country["name"].lower():

                print("\nCOUNTRY FOUND!")
                print("----------------")
                print("Name:", country["name"])
                print("Capital:", country["capitalCity"])
                print("Region:", country["region"]["value"])
                print("Income Level:", country["incomeLevel"]["value"])

                found = True

        if not found:
            print("Country not found. Please check the spelling.")


# PART 12 - ERROR HANDLING

except requests.exceptions.Timeout:

    print("\nERROR: The API request timed out.")
    print("Please check your internet connection and try again.")

except requests.exceptions.ConnectionError:

    print("\nERROR: Could not connect to the API.")
    print("Please check your internet connection.")

except requests.exceptions.HTTPError as error:

    print("\nHTTP ERROR:", error)

except (KeyError, IndexError, TypeError, ValueError) as error:

    print("\nDATA ERROR:", error)
    print("The API returned unexpected data.")

except requests.exceptions.RequestException as error:

    print("\nAPI REQUEST ERROR:", error)

except OSError as error:

    print("\nFILE ERROR:", error)