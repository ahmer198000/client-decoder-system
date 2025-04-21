```mermaid
sequenceDiagram
    actor Admin
    participant Browser
    participant Flask as Flask App
    participant ClientModel as Client Model
    participant SQLAlchemy as Flask-SQLAlchemy
    participant DB as Database

    Admin->>Browser: Navigate to /delete-client/<client_id>
    Browser->>Flask: GET /delete-client/<client_id>
    Flask->>ClientModel: Retrieve client with ID
    ClientModel->>SQLAlchemy: Query to fetch client by ID
    SQLAlchemy->>DB: Execute SELECT query
    DB-->>SQLAlchemy: Return client data
    SQLAlchemy-->>ClientModel: Return client data

    alt Client found
        Flask->>ClientModel: Delete client from database
        ClientModel->>SQLAlchemy: Execute DELETE query
        SQLAlchemy->>DB: Execute DELETE query
        DB-->>SQLAlchemy: Confirm successful delete
        SQLAlchemy-->>ClientModel: Return success
        ClientModel-->>Flask: Client deleted successfully

        Flask->>Browser: Redirect to /clients
        Browser->>Admin: Display client list
    else Client not found
        Flask->>Browser: Display error message
        Browser->>Admin: Show client not found message
    end
