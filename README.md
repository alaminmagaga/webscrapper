<h1 align="center">Web Scraper with Python and Django</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python 3.8+">
</p>

<p align="center">
  <img src="https://github.com/alaminmagaga/webscrapper/blob/master/Untitled.gif" alt="App">
</p>

<h2>Description</h2>

This web scraper application is built using Python and Django. It allows users to enter a URL and scrape the content of the page. The scraped data is then displayed in a user-friendly format. Additionally, users have the option to download the scraped data in PDF, CSV, or JSON format.

## Features

- **URL Input**: Users can enter the URL of a web page they want to scrape.
- **Content Scraping**: The web scraper retrieves the content of the provided URL and extracts the relevant data.
- **User-Friendly Display**: The scraped data is displayed in a user-friendly format, making it easy for users to view and analyze.
- **Data Download**: Users have the option to download the scraped data in PDF, CSV, or JSON format for further analysis or storage.

## Installation

To run the web scraper locally, follow these steps:

1. Clone this repository to your local machine using the following command:
<br>git clone git clone https://github.com/alaminmagaga/webscrapper.git

2. Change to the project directory:
```
cd web-scraper
```

3. Create a virtual environment to install the required dependencies:
```
python3 -m venv venv
```

4. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. Install the dependencies:
 ```
 pip install -r requirements.txt
  ```

6. Run the Django development server:
Open your web browser and navigate to `http://localhost:8000` to access the web scraper.

## Usage

1. Once you access the web scraper in your web browser, you will see an input field to enter the URL of the web page you want to scrape.

2. Enter the URL and click the "Scrape" button to initiate the scraping process.

3. The web scraper will retrieve the content of the provided URL and extract the relevant data.

4. The scraped data will be displayed in a user-friendly format on the web page.

5. To download the scraped data, click on the desired format (PDF, CSV, or JSON) link provided on the web page.

6. The downloaded file can be further analyzed or stored for future reference.

## Contributing

Contributions are welcome! If you encounter any issues with the web scraper or would like to contribute improvements, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch from the main branch.
 ```
 git checkout -b my-branch
  ```
  
3. Make the desired changes and commit them with descriptive commit messages.
```
git commit -m "Add feature or fix issue"
```

4. Push the branch to your forked repository.
```
git push origin my-branch
```

5. Open a pull request on the original repository, describing the changes you made.



