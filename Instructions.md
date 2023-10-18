To run the Django project repository "book-recommender-app," please follow these installation instructions:
After step 6, you can skip to the end of file.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kallol7/book-recommender-app
   cd book-recommender-app
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use: .\env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   ```bash
   cd config
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Admin):**
   I have provided the database (db.sqlite3 inside config folder), you can 
   skip the step below and use the superuser I already created:
      Username: admin
      Password: admin
   
   Run this if you don't want to use the superuser I provided above.
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The development server will start, 
   and you can access the application in your web browser at `http://localhost:8000/`.

7. **Access the Admin Interface:**
   To access the admin interface, go to `http://localhost:8000/admin/` and log in using the superuser credentials you created in step 5.

8. **Using the Application:**
   You can now use the book-recommender app by navigating to `http://localhost:8000/` and explore its features.

These instructions should help you set up and run the "book-recommender-app" Django project successfully.

Now follow the instructions in "README.md" file.
