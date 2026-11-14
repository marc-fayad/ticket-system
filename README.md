# TicketQueue
### A streamlined shared ticketing system for an IT team.

TicketQueue gives small IT teams one place to track helpdesk requests, identity & access management procedures, and internal project tasks. Requesters can see the status of their tickets, and staff can share queues to see what needs attention, reassign tasks, and note progress for the sake of review.

The current prototype includes a sign-in and a "My Tickets" page that shows tickets associated with the signed-in user. Ticket creation, shared queues, assignment, and status updates are planned features.

## Installation

TicketQueue requires Python 3.11 and Git. The following commands are for Windows PowerShell.

Clone the repository and open the cloned folder in your terminal.

```powershell
git clone https://github.com/marc-fayad/ticket-system.git
cd ticket-system
```

From the folder containing `manage.py`, create a virtual environment, install the dependencies, and initialize the SQLite database.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
```

## Usage

Create a local account the first time you set up TicketQueue. Follow the prompts to choose a username and password.

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

Start the development server.

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and sign in with the account you created. TicketQueue opens the **My Tickets** page. A fresh database shows an empty ticket list.

Press **Ctrl+C** in the terminal to stop the server.

## License

TicketQueue is licensed under the [MIT License](LICENSE).
