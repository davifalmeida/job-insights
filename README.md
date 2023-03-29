# Job Analysis Web App

## Overview

This project is a web application that provides data analysis on job listings. The app is built using Flask, a popular Python web framework. Users can explore various insights on job data, extracted from Glassdoor and obtained through Kaggle. The project also includes testing using Pytest and demonstrates various key Python programming concepts.

Created by [davifalmeida](https://github.com/davifalmeida).

## Features

- Interactive data analysis on job listings.
- Web application built using Flask.
- Exception handling and data manipulation.
- Custom modules and code organization.
- Unit testing with Pytest.

## Installation and Setup

1. Clone this repository or download the project files to your local machine.
2. Set up a virtual environment (optional, but recommended):
```
python -m venv venv
```
3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Linux/macOS:
  ```
  source venv/bin/activate
  ```
4. Install the required dependencies listed in the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ```
5. Run the Flask application:

```
flask run
```
6. Access the web app in your browser at `http://localhost:5000/`.

## Usage

- Navigate to the app's homepage to view various job data insights.
- Interact with the data by selecting filters or options as needed.
- Explore the source code to understand the implementation and organization of the project.

## Contributing

Feel free to submit pull requests or open issues if you have suggestions for improvements or encounter any bugs.

## License

This project is released under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- Data sourced from [Glassdoor](https://www.glassdoor.com/index.htm) and obtained through [Kaggle](https://www.kaggle.com/).
- Flask web framework: [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- Testing framework: [Pytest](https://docs.pytest.org/en/latest/)
