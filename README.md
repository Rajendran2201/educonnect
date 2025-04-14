# EduConnect

EduConnect is an educational platform designed to improve the quality of education for students in government schools. It includes various features such as a virtual lab assistant, career guidance, event/workshop booking, resource sharing, a discussion forum, attendance management, events tracker, and a donation module. The platform aims to provide students with valuable resources, mentorship, and a personalized learning experience.

## Features

### 1. Virtual Lab Assistant
- A subject-specific lab assistant focusing on biology, chemistry, and physics.
- Provides virtual assistance with lab experiments, explanations, and resources.

### 2. Career Guidance
- Professional mentorship and career advice from alumni and industry professionals.
- Includes workshops, webinars, and career path recommendations for students.

### 3. Event & Workshop Booking
- Students can book and register for educational events and workshops.
- Provides an easy way for students to stay updated with upcoming events.

### 4. Resource Sharing
- A platform to share study materials, educational resources, and notes.
- Students and teachers can upload, download, and access resources for better learning.

### 5. Discussion Forum
- A community-based forum for students and teachers to ask questions and engage in discussions.
- Encourages knowledge sharing and peer-to-peer learning.

### 6. Attendance Management
- A system for tracking student attendance and providing insights through visualizations.
- Similar to GitHub's contribution graph, it shows trends and patterns in attendance.

### 7. Events Tracker
- A tool to track and manage school events, both educational and extracurricular.
- Helps keep students and teachers informed about important events.

### 8. Donation Module
- Allows users to contribute financially to support educational initiatives.
- Provides transparency by tracking donations and their usage.

## Installation

To run the EduConnect platform locally, follow these steps:

### Prerequisites
- Python 3.10 or higher
- Django 4.0 or higher
- A MySQL or PostgreSQL database (ensure your settings are configured correctly)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Rajendran2201/educonnect.git
   cd educonnect
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database by modifying the `DATABASES` settings in `settings.py` to match your database configuration.

5. Run migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

The application should now be running at `http://localhost:8000/`.

## Technologies Used

- **Django**: Web framework for Python.
- **SQLite** (default database, but can be replaced with MySQL/PostgreSQL).
- **Bootstrap**: Frontend framework for responsive design.
- **JavaScript** (Vanilla JS and jQuery): To handle interactivity.

## Contributing

If you'd like to contribute to EduConnect, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to your forked repository (`git push origin feature/your-feature`).
5. Open a pull request.

## License

EduConnect is open-source and released under the MIT License.

## Contact

For more information, feel free to contact the project maintainers:

- Email: rajendran.stech@gmail.com

