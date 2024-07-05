
# Insurance Platform

This repository contains the code for an insurance platform developed using HTML, CSS, Django, and MySQL. The platform facilitates policy management, claims processing, and provides user-friendly interfaces for effortless interaction.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Features
- **Policy Management:** Allows users to manage their insurance policies effectively.
- **Claims Processing:** Facilitates the processing of insurance claims.
- **User-Friendly Interfaces:** Designed to ensure effortless interaction for users.
- **Payment Automation:** Integrated with Razorpay for seamless payment automation using ngrok and webhooks.
- **Security:** Utilized CSRF tokens for robust form validation and incorporated CORS middleware to secure cross-origin requests and enhance security against unauthorized access attempts.

## Tech Stack
- **Frontend:** HTML, CSS
- **Backend:** Django
- **Database:** MySQL
- **Payment Gateway:** Razorpay
- **Security:** CSRF tokens, CORS middleware

## Installation

### Prerequisites
- Python 3.x
- Django
- MySQL
- ngrok (for webhook testing)
- Razorpay account

### Steps
1. **Clone the repository:**
    ```sh
    git clone https://github.com/harshini-20-05/INSURANCE.IN.git
    cd INSURANCE.IN
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install Django mysqlclient djangorestframework razorpay ngrok corsheaders
    ```

4. **Set up MySQL database:**
    - Create a MySQL database.
    - Update `settings.py` with your database credentials.

5. **Run migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Run ngrok for webhooks:**
    ```sh
    ngrok http 8000
    ```

## Usage
1. **Access the platform:**
    Open your web browser and go to `http://127.0.0.1:8000`.

2. **Admin Panel:**
    Access the Django admin panel at `http://127.0.0.1:8000/admin` to manage users, policies, and claims.

3. **User Login:**
    Use the login system to access the platform as an agent or customer.

4. **Payments:**
    Process payments using Razorpay through the integrated payment system.



## Contact
For any questions or suggestions, feel free to reach out:
- Email: harshini.v218@gmail.com
- GitHub: [harshini-20-05](https://github.com/harshini-20-05)


