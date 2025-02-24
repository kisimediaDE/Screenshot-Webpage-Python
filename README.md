# Webpage Screenshot Tool

## 📌 Overview

This Python script captures a screenshot of a given webpage at a specified resolution and aspect ratio. It utilizes **Selenium** to automate Chrome and take a screenshot at the desired dimensions without cropping or resizing.

## 🚀 Features

- Capture a **full-page screenshot** at a specified resolution (e.g., **1920x1080 for 16:9**).
- Uses **headless Chrome** for efficient rendering.
- Supports **custom resolution input**.
- Fully automated with **Selenium WebDriver**.

## 📦 Requirements

### 1. Install Dependencies

You need to install **Selenium**:

```bash
pip install selenium
```

### 2. Install Google Chrome

Ensure that **Google Chrome** is installed on your system.

### 3. Download ChromeDriver

Download the **Chrome WebDriver** that matches your Chrome version from:
[ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

Extract and place `chromedriver` in the project directory or add it to your system `PATH`.

## 💻 Usage

### Run the script:

```bash
python screenshot.py
```

### Provide the inputs:

- **Enter the URL** of the webpage.
- **Specify width** (e.g., 1920 for Full HD resolution).
- **Specify height** (e.g., 1080 for a 16:9 ratio).

### Example Input:

```
Enter URL: https://example.com
Enter width: 1920
Enter height: 1080
```

The script will generate a **screenshot.png** file in the current directory.

## ⚙️ How It Works

1. **Launches headless Chrome** with the specified window size.
2. **Loads the webpage** and waits for full rendering.
3. **Takes a screenshot** at the exact resolution specified.
4. **Saves the screenshot** without resizing or cropping.

## 🛠 Troubleshooting

### ChromeDriver version mismatch

If you get an error related to ChromeDriver, make sure you have:

- The latest version of **Google Chrome** installed.
- The correct version of **ChromeDriver** matching your Chrome version.

### Webpage not fully loaded in screenshot

Increase the `time.sleep(3)` value in the script to allow more time for the webpage to load.

## 📜 License

This project is licensed under the MIT License.

---

Enjoy capturing high-quality webpage screenshots! 🚀
