```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant Flask as Flask App
    participant RegForm as RegistrationForm
    participant FlaskWTF as Flask-WTF
    participant Bcrypt as Flask-Bcrypt
    participant UserModel as User Model
    participant SQLAlchemy as Flask-SQLAlchemy
    participant DB as Database

    User->>Browser: Navigate to /register
    Browser->>Flask: GET /register
    Flask->>RegForm: Create registration form
    Flask->>Browser: Return registration page with form
    
    User->>Browser: Enter username, password
    User->>Browser: Submit form
    Browser->>Flask: POST /register with form data
    
    Flask->>RegForm: Pass form data
    RegForm->>FlaskWTF: Validate form data
    FlaskWTF-->>RegForm: Validation result
    
    alt Form is valid
        Flask->>Bcrypt: Hash password
        Bcrypt-->>Flask: Return hashed password
        
        Flask->>UserModel: Create new User object
        UserModel->>SQLAlchemy: Request to save user
        SQLAlchemy->>DB: Execute INSERT query
        DB-->>SQLAlchemy: Confirm successful insert
        SQLAlchemy-->>UserModel: Return success
        UserModel-->>Flask: User created successfully
        
        Flask->>Browser: Redirect to /login
        Browser->>User: Display login page
    else Form is invalid
        RegForm-->>Flask: Return validation errors
        Flask->>Browser: Redisplay form with errors
        Browser->>User: Show validation errors
    end