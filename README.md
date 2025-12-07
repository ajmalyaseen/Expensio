# 💰 Expensio - Minimal Expense Tracker

Expensio is a clean, dark-themed expense tracking application built with **Django** and **Tailwind CSS**. It helps users track their daily income and expenses, categorize them, and analyze their financial habits with a modern dashboard.

## ✨ Features

* 🔐 **Secure Authentication:** User Login, Registration, and Profile management.
* 📊 **Interactive Dashboard:** View Total Income, Expense, and Current Balance at a glance.
* 📅 **Smart Filtering:** Filter transactions by Month and Date.
* 📂 **Category Management:** Add custom categories for Income and Expenses with icons.
* 🎨 **Modern UI:** Fully responsive Dark Mode interface designed with Tailwind CSS.
* 📝 **Transaction History:** View recent transactions with color-coded indicators (Green for Income, Red for Expense).

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, Tailwind CSS, JavaScript
* **Database:** SQLite (Default)

## 🚀 How to Run Locally

Follow these steps to set up the project on your machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/ajmalyaseen/Expensio.git](https://github.com/ajmalyaseen/Expensio.git)
    cd Expensio
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

Open your browser and visit: `http://127.0.0.1:8000/`

## 👤 Author

**Ajmal Yaseen**
* [GitHub Profile](https://github.com/ajmalyaseen),
* [Linkdn Profile](www.linkedin.com/in/ajmal-yaseen-bb2374272)


---
*Built with ❤️ using Django*