# SnapInsta Image Download Project

This project automates the process of downloading images from the SnapInsta website using Selenium and PyAutoGUI. It is specifically designed to work with a screen resolution of 1920x1080 on a Linux Mint distribution.

## Features

- **Automated Download:** The script enables the automated download of a specified number of images from SnapInsta.

- **Firefox Interaction:** Utilizes Selenium to launch a Firefox browser, navigate the site, and trigger downloads.

- **Coordinate Management:** Coordinates of various elements on the page (links, buttons, etc.) are defined in a JSON file for easy customization.

## Requirements

- **Linux Distribution:** The script has been developed and tested on Linux Mint.

- **Screen Resolution:** The current configuration is optimized for a resolution of 1920x1080.

## Usage

1. **Install Dependencies:** Ensure you install the necessary dependencies using `pip install -r requirements.txt`.

2. **Configuration:** Modify coordinates and other settings in the `db.json` file according to your needs.

3. **Execution:** Run the script using `python main.py` and follow the instructions.

## Notes

This project is developed for educational purposes and may require adjustments to work on other configurations. Contributors are welcome to propose improvements and fixes.

## Cleanup

After running the script, the contents of the `links.txt` file are automatically cleared to maintain data privacy.

---

Feel free to customize this README based on specific features or aspects of your project.
