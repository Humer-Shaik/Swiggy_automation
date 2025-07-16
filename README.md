# Swiggy Automation

**Automated end‑to‑end workflow for placing an order on Swiggy using Selenium WebDriver.**

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/selenium-4.x-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Demo](#demo)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Workflow Details](#workflow-details)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)

---

## Overview

This repository contains a Python script that automates a typical food‑ordering journey on [Swiggy](https://www.swiggy.com/). It:

1. Launches Chrome in maximised mode and navigates to Swiggy’s homepage.
2. Logs in with your phone number (OTP entry handled manually for security).
3. Searches for **Domino’s Pizza**, selects the restaurant, and adds the first menu item to the cart.
4. Prompts you to add an address (manual entry) and proceeds to the payment page.
5. Saves screenshots during key failures for easier debugging.

> **Use‑case**: Demonstrates best practices for end‑to‑end UI automation—explicit waits, graceful retries, defensive error‑handling, and clean logging—while respecting sensitive user interactions like OTP and address entry.

---

## Features

* **Headless‑ready browser setup** (toggleable via CLI flag).
* **Explicit waits** with `WebDriverWait` to handle dynamic UI states.
* **Resilient search** that retries for up to 30 seconds if elements are slow to load.
* **Screenshot capture** on locator timeouts or unexpected exceptions.
* **Console logging** summarising each major step, including page title & URL validation.
* Modular structure (`locators.py`, `swiggy.py`, `utils.py`) for easy maintenance.

---

## Demo

> Add a short GIF (optional) to `docs/demo.gif` and it will render here.
>
> ```text
> /docs
>   └── demo.gif
> ```

<p align="center">
  <img src="docs/demo.gif" width="700" alt="Automation demo"/>
</p>

---

## Prerequisites

| Tool          | Version        | Notes                                 |
| ------------- | -------------- | ------------------------------------- |
| Python        | 3.10 or newer  | Tested on 3.10 & 3.11                 |
| Google Chrome | 124 or newer   | Ensure Chrome matches driver build    |
| ChromeDriver  | Same as Chrome | Add to your system `PATH`             |
| pip           | Latest         | `python -m pip install --upgrade pip` |

---

## Installation

```bash
# 1. Clone the repository
$ git clone https://github.com/<your‑username>/Swiggy_automation.git
$ cd Swiggy_automation

# 2. (Optional) Create & activate a virtual environment
$ python -m venv .venv
$ source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt
```

---

## Configuration

Open **`config.yaml`** (or edit constants in `swiggy.py`) and set the following:

| Key                 | Description                                    |
| ------------------- | ---------------------------------------------- |
| `PHONE_NUMBER`      | 10‑digit Indian mobile number for Swiggy login |
| `CHROMEDRIVER_PATH` | Absolute path to ChromeDriver (optional)       |
| `HEADLESS`          | `true` to run browser in headless mode         |

> **Security Note**: The script pauses automatically after requesting the OTP and again when the **Add New Address** form opens. This ensures your sensitive information is never stored in plaintext.

---

## Usage

```bash
python swiggy.py               # Standard run (GUI)
python swiggy.py --headless     # Headless run (no GUI)
```

Follow the on‑screen prompts to:

1. Enter the OTP you receive on your phone.
2. Fill in your delivery address details.

The console will confirm each major milestone and print a final message when automation is complete.

---

## Workflow Details

1. **Browser Setup** – Launch Chrome, maximise window, navigate to Swiggy.
2. **Login** – Click **Sign In**, input `PHONE_NUMBER`, request OTP; script waits (`WebDriverWait`) for manual OTP entry.
3. **Post‑Login Verification** – Print page title & URL; abort if they don’t match expected values.
4. **Search "Dominos"** – Open header search, type *Dominos*, submit query; retry locator checks up to 30 seconds.
5. **Select Restaurant** – Wait until the *Domino’s Pizza* result is clickable; click to open menu page.
6. **Add Item** – Scroll to the first **ADD** button, click, then open **View Cart**.
7. **Enter Address** – Click **Add New Address**; pause for manual entry; save address.
8. **Proceed to Payment** – Click **Proceed to Payment** in cart summary.
9. **Completion** – Print final console message; automation ends with browser still open for manual review.



## Troubleshooting

| Symptom                                                   | Possible Cause                       | Remedy                                                     |
| --------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------- |
| `NoSuchElementException` when locating an element         | Swiggy UI changed                    | Update locator in `locators.py`                            |
| OTP never arrives                                         | Network congestion / DND             | Re‑run script after receiving OTP                          |
| `selenium.common.exceptions.TimeoutException` on any step | Slow internet or element locator bug | Increase wait time or verify XPath/CSS selector accuracy   |
| Black or blank browser screen in headless mode            | GPU issues on certain Linux distros  | Run with `--disable-gpu` Chrome flag or switch to GUI mode |

---

## Contributing

1. **Fork** the project and create your branch: `git checkout -b feature/AmazingFeature`.
2. Commit your changes: `git commit -m 'Add some AmazingFeature'`.
3. Push to the branch: `git push origin feature/AmazingFeature`.
4. Open a **Pull Request**.

Please open an issue first to discuss significant changes.

---

## License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

> **Disclaimer**
>
> This project is intended for **educational and personal use only**. Automating user interactions on Swiggy may violate their Terms of Service. Use responsibly and at your own risk.
