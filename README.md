# Python Automation & Scripting Lab

## Description

This project demonstrates Python scripting for automation tasks. It is designed to show how to generate dynamic log files, interact with external APIs using third-party libraries, and properly manage project dependencies.

The code follows best practices by separating concerns into distinct functions, using virtual environments for isolation, and tracking exact package versions for reproducibility.

## Features

**Log Generation**: Automatically generates a dated `.txt` file (e.g., `log_20261018.txt`) containing a list of provided log entries.

**Input Validation**: Ensures that the data passed to the log generator is a list, raising a `ValueError` if not.

**API Integration**: Uses the `requests` library to fetch data from a public API (`jsonplaceholder.typicode.com`) and parses the JSON response.

**Separation of Concerns**: Logic is encapsulated into reusable functions (`generate_log` and `fetch_data`).

**Safe Execution**: The script logic is wrapped in the `if __name__ == "__main__":` block, ensuring it only runs when executed directly, not when imported.

## Requirements & Dependencies

This project uses an isolated virtual environment. All dependencies are documented in the `requirements.txt` file to ensure consistent environments across systems.

`requests==2.32.4`
`certifi==2026.7.22`
`charset-normalizer==3.5.2`
`idna==3.15`
`urllib3==2.2.3`

## Installation & Setup

1. **Clone the repository:**

```bash
   git clone https://github.com/YourUsername/course-7-module-6-pip-pypi-scripting-lab.git
   cd course-7-module-6-pip-pypi-scripting-lab
```

## Create and activate a virtual environment:

```bash
pipenv install
pipenv shell
```

Install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```

## Usage & Testing

To run the automation script:

```bash
python generate_log.py
```

## Run the test suite

```bash
pytest -x testing/
```

## Completed Work

![Screenshot](img/Screenshot%20From%202026-10-18%2012-16-41.png)

## License

This project is open-source and available under the MIT License.
