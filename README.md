# Password Manager

## Overview

Welcome to my Password Manager project! This application provides a secure and user-friendly solution for managing
passwords. It includes features for account creation, login, password generation, and storage in a local file.

## Features

- **User Authentication:** Users can create an account with a secure passcode or log in to an existing account.
- **Password Generation:** The application generates strong passwords with a mix of letters, numbers, and symbols.
- **Data Encryption:** User passcodes and passwords are encrypted to enhance security.
- **Graphical User Interface (GUI):** The program offers an intuitive GUI for a seamless user experience.
- **Data Persistence:** User data is stored locally, allowing for easy retrieval across sessions.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Required Python packages: `tkinter`, `pandas`

## Getting Started

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/NEjim2001/Password-Manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Password-Manager
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```

## Usage

- **First-Time Users:** If you're a first-time user, you'll be prompted to set up a passcode.
- **Returning Users:** Enter your passcode to log in and access the main application.

## File Structure

- `main.py`: Main script to run the application.
- `user.py`: Module handling user authentication and passcode management.
- `passgen.py`: Module for generating strong passwords.
- `encryption.py`: Module providing encryption and decryption functionality.
- `assets/`: Directory containing logo and other assets.
- `application_data/`: Directory for storing user data.

##  

Happy password managing!
