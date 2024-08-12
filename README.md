# Instagram Auto-Follow Bot

This Python script automates the process of logging into Instagram and following a list of specified profiles using Selenium WebDriver.

## Features

- **Automated Login**: Logs into Instagram using your credentials.
- **Profile Following**: Automatically follows a list of specified Instagram profiles.

## Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Google Chrome**: This script uses Chrome for automation. Install Chrome from [here](https://www.google.com/chrome/).
- **ChromeDriver**: Download the appropriate version of ChromeDriver for your Chrome version from [here](https://sites.google.com/chromium.org/driver/). Ensure it's added to your system's PATH or specify the path in the script.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/KunshArora912/instagram-auto-follow-bot.git
    cd instagram-auto-follow-bot
    ```

2. Install the required Python packages:

    ```bash
    pip install selenium
    ```

## Setup

1. **Configure Instagram Credentials**: Open the script and enter your Instagram `USERNAME` and `PASSWORD` in the designated variables.

    ```python
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    ```

2. **Add Profiles to Follow**: Add the URLs of the Instagram profiles you want to follow in the `profiles_to_follow` list.

    ```python
    profiles_to_follow = [
        "https://www.instagram.com/username1/",
        "https://www.instagram.com/username2/"
    ]
    ```

3. **Specify ChromeDriver Path**: Update the `driver_path` variable with the path to your `chromedriver` executable.

    ```python
    driver_path = 'path/to/chromedriver'
    ```

4. **Optional**: If Chrome is installed in a non-standard location, update the `binary_location` in the script:

    ```python
    options.binary_location = "C:\\Path\\To\\Chrome\\Application\\chrome.exe"
    ```

## Usage

To run the script, execute the following command in your terminal or command prompt:

```bash
python instagram_follow_bot.py
