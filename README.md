# Virtual_Store_Assistant
A Virtual Store Assistant using AR for personalized product recommendations and in-store navigation.

# 🛍️ Virtual Store Assistant

Virtual Store Assistant is a web-based application leveraging Augmented Reality (AR) to offer personalized product recommendations and help customers locate products within a store. Developed for the Walmart Hackathon under the theme "Future of Retail."

## 📋 Table of Contents

- [📖 Introduction](#-introduction)
- [✨ Features](#-features)
- [💻 Tech Stack](#-tech-stack)
- [🚀 Setup](#-setup)
- [🔧 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

## 📖 Introduction

The retail landscape is transforming rapidly, blending online and offline experiences. Customers are becoming increasingly tech-savvy and enjoy exploring innovative technologies. Our Virtual Store Assistant aims to deliver a seamless shopping experience by integrating AR and providing the best aspects of both online and offline shopping.

## ✨ Features

- **Product Recommendations**: Personalized suggestions based on customer behavior and preferences.
- **Product Location**: AR navigation to help customers find products within a store.
- **Dynamic Product Display**: Fetch and display product images and details dynamically from APIs.
- **Payment Gateway**: Integrated payment page supporting multiple payment methods.

## 💻 Tech Stack

- **Frontend**: 
  - ![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS-239120?style=for-the-badge&logo=css3&logoColor=white)
  - ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  - ![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
  - ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
- **Backend**: 
  - ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
  - ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- **APIs**: Pexels, Unsplash, Pixabay for product images.
- **Database**: MySQL.

## 🚀 Setup

### Prerequisites

- Python 3.x
- Django
- Flask
- Virtual environment tools (virtualenv, pipenv, etc.)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/NakulLimbani/Virtual_Store_Assistant.git
    cd Virtual_Store_Assistant
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

## 🔧 Usage

- Navigate to the homepage to explore product categories and recommendations.
- Use the search bar to find specific products.
- Click on products to view details and add to cart.
- Proceed to checkout and select a payment method on the payment page.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
