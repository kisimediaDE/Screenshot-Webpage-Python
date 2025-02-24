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

You need to install **Selenium** and **Validators**:

```bash
pip install selenium validators
```

### 2. Install Google Chrome

Ensure that **Google Chrome** is installed on your system.

### 3. Install ChromeDriver

To install ChromeDriver:

1. Find your Chrome version:

   - Open Chrome and go to `chrome://settings/help`
   - Note down the version number (e.g., 120.0.0.1)

2. Download the corresponding **ChromeDriver** version from:

   - [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

3. Extract and place `chromedriver` in the project directory or add it to your system `PATH`.

### 4. Add ChromeDriver to PATH

#### macOS

```bash
echo 'export PATH="$PATH:~/path-to-chromedriver"' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

1. Move `chromedriver.exe` to a folder (e.g., `C:\chromedriver`)
2. Open **System Properties** → **Advanced** → **Environment Variables**
3. Under **System Variables**, find `Path` and click **Edit**
4. Click **New** and add `C:\chromedriver`
5. Click **OK**, restart the terminal, and verify with:

```powershell
chromedriver --version
```

#### Linux

```bash
echo 'export PATH="$PATH:/path-to-chromedriver"' >> ~/.bashrc
source ~/.bashrc
```

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
