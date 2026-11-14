# Design

## User Stories

### US-01 - Submitting a ticket
User Story: As a requester, I want to submit a ticket that has a category and description so I can send my request to the team that handles it.

Acceptance Criterion: When I submit a ticket with a title, category, and subscription, it appears in "My Tickets" with the 'Open' status. 

### US-02 - Checking ticket status
User Story: As a requester, I want to see the current status of my submitted tickets so I can tell whether my requests are open, in progress, or closed.

Acceptance Criterion: After a team member changes my ticket from 'Open' to 'In Progress', I see the updated status next time I look at the ticket.

### US-03 - Filtering tickets
User Story: As a team member, I want to filter tickets by category, status, and assignee, so I can find the work I need to handle or what somebody else is assigned.

Acceptance Criterion: When I select a category like 'IAM' and a status like 'Open', the queue displays only open IAM tickets I can see.

## Misuse Stories

### MS-01 - Edit someone else's ticket
Misuse Story: As a requester, I want to modify the ticket someone else opened that I have not been given permission to.

Mitigation Criterion: When I modify a field in someone else's assigned ticket,  the server denies the change and shows a denial message.

### MS-02 - Submit a ticket in someone else's name
Misuse Story: As a requester, I want to submit a ticket under another employee's name so I can make it appear that they requested work or access.

Mitigation Criterion: When a user submits a ticket while singed in, the Ticket Queue records the user as the requester.

## UI Mockups

### Ticket Creation
Filling out a form to submit a ticket.
![New Ticket form](images/TicketCreation.png)
Supports US-01


### My Ticket Queue
Checking the status of tickets the user submitted or is assigned.
![My Tickets list](images/MyTickets.png)
Supports US-02


### Followed Queues
Filter tickets by category, status, or assignee.
![Staff Queue](images/TicketQueues.png)
Supports US-03

## C4 Diagrams

### System Context Diagram
![System Context Diagram](images/TicketQueue-C4-Diagram-System-Context.drawio.png)

### Container Diagram
![System Context Diagram](images/TicketQueue-C4-Diagram-Container.drawio.png)

### Component Diagram
![System Context Diagram](images/TicketQueue-C4-Diagram-Component.drawio.png)
