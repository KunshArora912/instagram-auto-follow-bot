# Instagram-auto-follow-bot
Instagram Auto-Follow Bot
This Python script automates the process of logging into Instagram and following a list of specified profiles using Selenium WebDriver.

Features
Automated Login: Logs into Instagram using your credentials.
Profile Following: Automatically follows a list of specified Instagram profiles.
Prerequisites
Python 3.x: Ensure that Python is installed on your system. You can download it from python.org.
Google Chrome: This script uses Chrome for automation. Install Chrome from here.
ChromeDriver: Download the appropriate version of ChromeDriver for your Chrome version from here. Ensure it's added to your system's PATH or specify the path in the script.
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/KunshArora912/instagram-auto-follow-bot.git
cd instagram-auto-follow-bot
Install the required Python packages:

bash
Copy code
pip install selenium
Setup
Configure Instagram Credentials: Open the script and enter your Instagram USERNAME and PASSWORD in the designated variables.

python
Copy code
USERNAME = 'your_username'
PASSWORD = 'your_password'
Add Profiles to Follow: Add the URLs of the Instagram profiles you want to follow in the profiles_to_follow list.

python
Copy code
profiles_to_follow = [
    "https://www.instagram.com/username1/",
    "https://www.instagram.com/username2/"
]
Specify ChromeDriver Path: Update the driver_path variable with the path to your chromedriver executable.

python
Copy code
driver_path = 'path/to/chromedriver'
Optional: If Chrome is installed in a non-standard location, update the binary_location in the script:

python
Copy code
options.binary_location = "C:\\Path\\To\\Chrome\\Application\\chrome.exe"
Usage
To run the script, execute the following command in your terminal or command prompt:

bash
Copy code
python instagram_follow_bot.py
The script will log in to Instagram, visit each profile in the profiles_to_follow list, and attempt to follow them.

Notes
Headless Mode: The script runs in headless mode by default, meaning it doesn't open a visible browser window. If you want to see the browser actions, you can remove or comment out the options.add_argument('--headless') line in the script.

Timeouts: The script includes sleep times to account for page loading. Adjust these values if you encounter issues related to slow or fast loading times.

Disclaimer
This script is for educational purposes only. Automating interactions with social media platforms can violate their terms of service. Use it responsibly and at your own risk.
