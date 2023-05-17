# Gelsenkirchen Ratsinfo Scraper

This project scrapes the Gelsenkirchen city council's website for information about its councilors.

## Installation

This project is built with Python and uses Poetry for dependency management. To install the project, follow these steps:

1. Install [Python](https://www.python.org/downloads/).
2. Install Poetry by following the [official guide](https://python-poetry.org/docs/#installation).
3. Clone this repository:
    ```bash
    git clone https://github.com/vschwaberow/ratsinfo-scraper.git
    cd ratsinfo-scraper
    ```
4. Install dependencies with Poetry:
    ```bash
    poetry install
    ```

## Usage

After you've installed the project, you can run the scraper with this command:

```bash
poetry run python main.py
```

This command will scrape the councilor information from the Gelsenkirchen city council website and save it in a CSV file named `person_details.csv`.

The CSV file will contain the following columns:

- `Name`: The name of the councilor.
- `Party`: The party of the councilor.
- `Memberships`: The committees that the councilor is a member of, their roles in those committees, and the dates they joined.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the Apache 2.0 and MIT license.

## Disclaimer

This project is for educational purposes only. Please make sure to comply with the terms of service of the website before running the scraper. The authors of this project are not responsible for any misuse of the software.
