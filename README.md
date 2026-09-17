# Blood Donate & Request System

A full-featured Django web application where users can register as blood donors, request blood for medical emergencies, and search/filter suitable donors based on location and blood group.

---

## Features

* **User Authentication:** Registration, Login, and Logout functionality.
* **Donor Profile Management:** Users can create and update their donor status, location, last donation date, and availability.
* **Blood Requests (CRUD):**
  * **Create:** Request blood with patient details, hospital, required date, and urgency.
  * **Read:** View active blood requests with detailed views.
  * **Update & Delete:** Requesters can edit or remove their own requests.
* **Search & Filtering:**
  * Filter donors by Blood Group, Location, and Availability.
  * Filter blood requests by Blood Group, Location, and Status (Pending, Fulfilled, Cancelled).
* **Responsive UI:** Built with Bootstrap 5 for clean and mobile-friendly navigation.

---

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, Bootstrap 5, CSS3
* **Database:** SQLite3 (Default Django DB)

---

## Installation & Setup Instructions

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd blood_donation_project