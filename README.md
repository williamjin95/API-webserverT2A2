# API Webserver T2A2 #

## R1 ##

Problem:
Construction companies often struggle with managing multiple projects, tracking progress, allocating resources efficiently, and maintaining good communication among team members. Additionally, they face difficulties in keeping accurate records and managing client information.

Solution:
The Construction Company API addresses these issues by offering a centralized platform for managing projects, resources, and communication. It allows companies to create, update, and monitor projects, ensuring timely completion. The API helps in allocating resources like employees, equipment, and materials effectively, providing real-time availability. It improves communication by integrating with other tools, ensuring team members are always informed. The API also offers a structured way to store and access records and manage client information, ensuring all data is easily retrievable and client expectations are met.

## R2 ##

Tasks are defined based on project needs and assigned to employees according to their roles and availability. The API helps track these tasks by recording details like descriptions, deadlines, and status updates. Employees can update task statuses in real-time, which keeps everyone informed about progress. Notifications alert employees about deadlines and new assignments. Managers can generate reports to assess task completion, employee performance, and overall project progress. All actions are logged, providing a clear audit trail.

The Construction Company API ensures efficient project management, optimal resource utilization, and improved communication within the organization.

## R3 ##

Flask: This is the core framework used to build the web server, handling routing, requests, and responses.

Flask-SQLAlchemy: An extension that adds support for SQLAlchemy, used to interact with the PostgreSQL database, define models, and perform CRUD operations.

Flask-Marshmallow: An extension that integrates Marshmallow with Flask for serializing, deserializing, and validating data.

Flask-JWT-Extended: A package used for handling user authentication by creating and verifying JSON Web Tokens (JWT), and protecting routes that require authentication.

psycopg2-binary: The PostgreSQL database adapter for Python, enabling SQLAlchemy to interact with the PostgreSQL database.

Marshmallow-SQLAlchemy: An extension for Marshmallow that simplifies the serialization and deserialization of SQLAlchemy models by creating schemas based on these models.

## R4 ##

Benefits: PostgreSQL offers reliability, advanced features, scalability, and strong security, making it a robust choice for a construction company database where data integrity and advanced querying capabilities are essential.

Drawbacks: PostgreSQL's complexity, performance overhead, resource intensity, and maintenance requirements can be challenging, especially for teams without specialized knowledge. While managed services can help, they may introduce additional costs.

## R5 ##

SQLAlchemy, with Flask-SQLAlchemy, is used in this app to interact with the database using Python classes instead of SQL. It allows defining models, managing relationships, and performing CRUD operations in a readable and maintainable way. This abstraction increases productivity, improves security by preventing SQL injection, and ensures database schema is managed through Python code.

For example, you can define an Employee model, create a new employee, and manage relationships like work hours at different locations using SQLAlchemy's ORM features. This makes database operations simpler and more secure.

## R6 ##

![ERD](/docs/constructionapi.png)

## R7 ##

User:

Attributes: id, username, password
Purpose: Stores user authentication details.

Employee:

Attributes: id, name, position
Purpose: Stores employee details.
Relationship: One-to-many with Hour.

Location:

Attributes: id, address
Purpose: Stores job location details.
Relationship: One-to-many with Hour.

Hour:

Attributes: id, date, hours, employee_id, location_id
Purpose: Records hours worked by employees at specific locations.
Relationships: Many-to-one with Employee and Location.

Benefits
Data Integrity: Foreign keys ensure valid references, preventing orphan records.
Efficient Retrieval: Simplifies complex queries with JOIN operations.
Simplified Queries: Easy access to related records.
Maintainability: Clear structure for easy modifications.
Normalization: Reduces redundancy and ensures consistency.

## R8 ##

Register a New User:

POST /api/auth/register
Body: {"username": "string", "password": "string"}
Response: {"id": "integer", "username": "string"}

Login:

POST /api/auth/login
Body: {"username": "string", "password": "string"}
Response: {"access_token": "string"}

Create a New Employee:

POST /api/employees/
Headers: Authorization: Bearer <your_jwt_token>
Body: {"name": "string", "position": "string"}
Response: {"id": "integer", "name": "string", "position": "string"}

Get All Employees:

GET /api/employees/
Headers: Authorization: Bearer <your_jwt_token>
Response: [{"id": "integer", "name": "string", "position": "string"}, ...]

Update an Employee:

PUT /api/employees/<int:id>
Headers: Authorization: Bearer <your_jwt_token>
Body: {"name": "string", "position": "string"}
Response: {"id": "integer", "name": "string", "position": "string"}

Delete an Employee:

DELETE /api/employees/<int:id>
Headers: Authorization: Bearer <your_jwt_token>
Response: 204 No Content

Create a New Location:

POST /api/locations/
Headers: Authorization: Bearer <your_jwt_token>
Body: {"address": "string"}
Response: {"id": "integer", "address": "string"}

Get All Locations:

GET /api/locations/
Headers: Authorization: Bearer <your_jwt_token>
Response: [{"id": "integer", "address": "string"}, ...]

Update a Location:

PUT /api/locations/<int:id>
Headers: Authorization: Bearer <your_jwt_token>
Body: {"address": "string"}
Response: {"id": "integer", "address": "string"}

Delete a Location:

DELETE /api/locations/<int:id>
Headers: Authorization: Bearer <your_jwt_token>
Response: 204 No Content

Create a New Hour Entry:

POST /api/hours/
Headers: Authorization: Bearer <your_jwt_token>
Body: {"date": "YYYY-MM-DD", "hours": "float", "employee_id": "integer", "location_id": "integer"}
Response: {"id": "integer", "date": "YYYY-MM-DD", "hours": "float", "employee_id": "integer", "location_id": "integer"}

Get All Hour Entries:

GET /api/hours/
Headers: Authorization: Bearer <your_jwt_token>
Response: [{"id": "integer", "date": "YYYY-MM-DD", "hours": "float", "employee_id": "integer", "location_id": "integer"}, ...]

Update an Hour Entry:

PUT /api/hours/<int:id>
Headers: Authorization: Bearer <your_jwt_token>
Body: {"date": "YYYY-MM-DD", "hours": "float", "employee_id": "integer", "location_id": "integer"}
Response: {"id": "integer", "date": "YYYY-MM-DD", "hours": "float", "employee_id": "integer", "location_id": "integer"}

Delete an Hour Entry:

DELETE /api/hours/<int:id>
Headers: Authorization: Bearer <your_jwt_token>
Response: 204 No Content