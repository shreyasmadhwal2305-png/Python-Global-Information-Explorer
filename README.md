# 🌍 Python Global Information Explorer

A Python-based application that retrieves, processes, analyses, and explores country information using the **World Bank API**.

## 🚀 Features

- 🌐 Retrieve country information from the World Bank API.
- 📄 Implement API pagination to collect large datasets.
- 🔄 Automatically retry requests after temporary API failures.
- 🌎 Analyse geographical country distribution by region.
- 🏛️ Analyse countries with and without capital cities.
- 💾 Save collected country data into a JSON file.
- 📂 Load and process locally saved JSON data.
- 🔍 Search for countries by exact or partial name.
- 🔁 Perform multiple searches without restarting the program.
- 🚪 Enter `0` to exit the application.

## 🛠️ Technologies Used

- **Python 3** – Core programming language.
- **Requests** – Communicating with external APIs.
- **World Bank API** – Retrieving country information.
- **JSON** – Storing and loading country datasets.
- **Time** – Implementing delays between retry attempts.

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/shreyasmadhwal2305-png/Python-Global-Information-Explorer.git   ```

2. Navigate into the project directory:

   ```bash
   cd python-global-information-explorer
   ```

3. Install the required dependency:

   ```bash
   pip install requests
   ```

## ▶️ How to Run

Execute the following command:

```bash
python day31_api_pagination.py
```

The application will:

1. Connect to the World Bank API.
2. Retrieve country records using pagination.
3. Analyse country distribution and capital information.
4. Save the collected data to `countries_data.json`.
5. Allow you to search for countries interactively.

Enter `0` whenever you want to exit the program.

## 🌐 API Information

This project uses the [World Bank Countries API](https://api.worldbank.org/v2/country).

The API provides country-related information, including:

- Country names.
- Capital cities.
- Geographical regions.
- Income classifications.

No API key is required.

## 📚 What I Learned

Through this project, I practised:

- Advanced REST API integration.
- API pagination and automated data collection.
- Exception handling and retry mechanisms.
- Working with nested JSON structures.
- Data filtering and analysis.
- Reading and writing JSON files.
- Building interactive command-line applications.
- Using loops and conditional statements for continuous search.

## 🔮 Future Improvements

- Interactive world map with clickable countries.
- Visual dashboard with country statistics.
- Population and regional comparison charts.
- Country information portals.
- Interactive data visualizations using Python libraries.
