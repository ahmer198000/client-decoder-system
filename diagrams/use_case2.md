```mermaid
sequenceDiagram
    actor Admin
    participant Browser
    participant Flask as Flask App
    participant ClientForm as ClientForm
    participant FlaskWTF as Flask-WTF
    participant ClientModel as Client Model
    participant SQLAlchemy as Flask-SQLAlchemy
    participant DB as Database

    Admin->>Browser: Navigate to /create-client
    Browser->>Flask: GET /create-client
    Flask->>ClientForm: Create client form
    Flask->>Browser: Return client creation page with form

    Admin->>Browser: Enter client details
    Admin->>Browser: Submit form
    Browser->>Flask: POST /create-client with form data

    Flask->>ClientForm: Pass form data
    ClientForm->>FlaskWTF: Validate form data
    FlaskWTF-->>ClientForm: Validation result

    alt Form is valid
        Flask->>ClientModel: Create new Client object
        ClientModel->>SQLAlchemy: Request to save client
        SQLAlchemy->>DB: Execute INSERT query
        DB-->>SQLAlchemy: Confirm successful insert
        SQLAlchemy-->>ClientModel: Return success
        ClientModel-->>Flask: Client created successfully

        Flask->>Browser: Redirect to /clients
        Browser->>Admin: Display client list
    else Form is invalid
        ClientForm-->>Flask: Return validation errors
        Flask->>Browser: Redisplay form with errors
        Browser->>Admin: Show validation errors
    end
