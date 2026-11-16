# ⚡ FlowGenAI

**FlowGenAI** is an AI-powered web application that turns natural language ideas, user stories, and system workflows into structured and interactive **flowcharts** in seconds. Powered by **Django** and **Google Gemini 2.5 Flash**, it dynamically generates standards-compliant **Mermaid.js** diagrams with instant client-side rendering and high-resolution exports.

---

## 🌟 Key Features

- 🤖 **Natural Language to Diagram:** Describe any algorithm, business logic, system architecture, or process, and Gemini 2.5 Flash converts it into clean, valid Mermaid flowchart syntax (`graph TD`).
- 📊 **Real-time Live Rendering:** Client-side rendering powered by Mermaid.js v10 with instant feedback.
- 📥 **High-Resolution Exports:**
  - **PNG Export:** High-DPI rasterization via `html2canvas` (3x resolution scaling).
  - **PDF Export:** Auto aspect ratio fitting with `jspdf`.
- 🌓 **Theme Customization:** Seamless Light / Dark mode toggle with persistent state in `localStorage`.
- 🔐 **User Accounts & Authentication:** User registration, login, profile management, and account deletion with standard Django security.
- 🕒 **Saved History & Management:** Automatic history logging of generated flows with one-click reloading and deletion.

---

## 🏗️ How It Works

```text
 User Input (Topic / Prompt)
            │
            ▼
 Django View (`home`)
            │
            ▼
 Google Gemini 2.5 Flash API (`flow_generator/utils.py`)
 [Enforces strict Mermaid `graph TD` structure & formatting]
            │
            ▼
 Django ORM -> SQLite Database (`Flow` Model)
            │
            ▼
 Frontend Interface (`home.html`)
 ├── Mermaid.js (DOM Rendering)
 ├── html2canvas (PNG Download)
 └── jsPDF (PDF Download)
```

---

## 📁 Repository Structure

```text
FlowGenAI/
├── .gitignore
├── manage.py                           # Django CLI management entrypoint
├── core/                               # Django Project Settings & Routing
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                     # Project configuration & auth routing
│   ├── urls.py                         # Root URL routing
│   └── wsgi.py
└── flow_generator/                     # Main Application
    ├── __init__.py
    ├── admin.py                        # Django Admin model registrations
    ├── apps.py                         # App configuration
    ├── models.py                       # `Flow` model definition
    ├── tests.py                        # Unit and integration tests
    ├── urls.py                         # App-level endpoints
    ├── utils.py                        # Gemini 2.5 Flash API integration
    ├── views.py                        # Flow generation, history, and auth views
    ├── migrations/                     # Database schema migrations
    └── templates/                      # UI Templates (Tailwind CSS)
        ├── landing.html                # Product landing page
        ├── home.html                   # Main diagram workspace & renderer
        ├── login.html                  # User login
        ├── register.html               # User registration
        └── profile.html                # Account settings & profile management
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- A Google Gemini API Key ([Get one here](https://aistudio.google.com/))

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/Sathwik2104/FlowGenAI.git
cd FlowGenAI

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS / Linux:
source venv/bin/activate

# Install required Python packages
pip install django google-generativeai python-dotenv
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

### 4. Database Setup & Migrations
```bash
# Run migrations
python manage.py migrate

# (Optional) Create superuser for Django admin access
python manage.py createsuperuser
```

### 5. Run the Application
```bash
python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.

---

## 🎯 Usage Guide

1. **Sign Up / Log In:** Create an account or sign in to access your personal diagram workspace.
2. **Generate a Diagram:** Enter a prompt in the topic input (e.g., *"E-commerce checkout process with payment gateway failure handling"* or *"OAuth2 Authorization Code Flow"*) and click **Generate Flow**.
3. **Inspect & Interact:** View the dynamically rendered Mermaid diagram on the interactive canvas.
4. **Export:** Click **Download PNG** or **Download PDF** to export your diagram for presentations or documentation.
5. **Manage History:** Revisit previously generated flows from your sidebar or clear entries at any time.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 5
- **Generative AI:** Google Gemini 2.5 Flash (`google-generativeai`)
- **Frontend:** HTML5, Tailwind CSS, Google Fonts (Outfit)
- **Diagram Engine:** Mermaid.js v10 (ESM CDN)
- **Export Utilities:** `html2canvas`, `jspdf`
- **Database:** SQLite3

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
