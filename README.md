# tjs.lightbox

A full-stack photography portfolio app where users can browse your latest works, filter by title, leave reviews, and suggest creative ideas. Built with a Flask/SQLAlchemy backend and a React frontend.

---

## 🚀 Features

- **View Photography Works**  
  Fetch and display a list of all your photos, with title, description and average rating.

- **Filter Works**  
  Live search by work title.

- **Reviews**  
  — Create, list and delete 1–5 star reviews with comments.  
  — Average rating is calculated on the fly.

- **Ideas**  
  — Users can submit “ideas” or inspirations for each work.  
  — Create, list and delete ideas.

---

##  Project Structure

```bash
tjs.lightbox/
├── backend/
│ ├── app.py # Flask application & routes
│ ├── config.py # Flask & SQLAlchemy settings
│ ├── db.py # SQLAlchemy db instance
│ ├── models.py # ORM model definitions
│ ├── seed.py # Script to create & populate the DB
│ ├── requirements.txt # Python dependencies
│ └── venv/ # Virtual environment (gitignored)
└── frontend/
├── public/
│ └── index.html # HTML template
├── src/
│ ├── components/ # Reusable React components
│ ├── App.js # Main React component
│ ├── index.js # React entry point
│ └── index.css # Global styles
├── package.json # Node dependencies & scripts
└── node_modules/ # Installed packages (gitignored)
|-frontend.old
```

---

##  Backend Setup

1. **Enter the backend folder**  
```bash
cd backend
```

2. **Create & activate a virtualenv**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

4. **Seed the database**
```bash
python seed.py
```
5. **Set environment variables & run**
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
The API will be live at http://127.0.0.1:5000.
```

6. **Test an endpoint**
```bash
curl http://127.0.0.1:5000/works
You should receive a JSON array of seeded works.
```

## Frontend Setup
1. **Enter the frontend folder**

```bash
cd ../frontend
```

2. **Install Node dependencies**
```bash
npm install
```

3. **Start the React development server**
```bash
npm start
The app will open at http://localhost:3000.
```

4. **Verify functionality**

-The page title “My Photography Works” appears.

-Your seeded works load.

-You can filter, add/delete reviews & ideas.

## API Endpoints
| Method | Path                   | Description                         |
| ------ | ---------------------- | ----------------------------------- |
| GET    | `/works`               | List all works (with reviews/ideas) |
| POST   | `/reviews`             | Create a review                     |
| DELETE | `/reviews/<review_id>` | Delete a review                     |
| POST   | `/ideas`               | Create an idea                      |
| DELETE | `/ideas/<idea_id>`     | Delete an idea                      |


## Tech Stack
Backend: Python · Flask · Flask-SQLAlchemy · Flask-CORS · SQLite

Frontend: JavaScript · React · Create React App

Styling: Custom CSS (dark neon “Codédex” theme)

