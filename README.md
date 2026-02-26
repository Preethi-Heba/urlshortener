📎 URL Shortener

A simple Flask-based URL Shortener web application that converts long URLs into short, shareable links.

🚀 Features

🔗 Convert long URLs into short links

📊 Automatically redirects to original URL

🗂 Stores URLs using SQLite database

🌐 Clean and simple user interface

⚡ Fast redirection system

🛠 Built With
. Python
. Flask
. SQLite
. HTML & CSS
. SQLAlchemy

📂 Project Structure
url_shortener/
│
├── app.py
├── templates/
│     ├── index.html
│
├── static/
│     ├── style.css
│
└── url_shortener.db

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/url-shortener.git
cd url-shortener
2️⃣ Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install flask flask_sqlalchemy
4️⃣ Run the application
python3 app.py
5️⃣ Open in browser
http://127.0.0.1:5000

🔄 How It Works

1. User enters a long URL.

2. The app generates a unique short code.

3. The short URL is saved in the database.

4. When accessed, it redirects to the original URL.

🧠 Future Improvements

📈 Click tracking

🔐 User authentication

📅 Expiry dates for links

📊 Analytics dashboard

🌍 Custom short URLs
