```mermaid
sequenceDiagram
    actor Admin
    participant Browser
    participant Flask as Flask App
    participant DecoderModel as Decoder Model
    participant SQLAlchemy as Flask-SQLAlchemy
    participant DB as Database

    Admin->>Browser: Navigate to /decoders
    Browser->>Flask: GET /decoders
    Flask->>DecoderModel: Fetch list of decoders
    DecoderModel->>SQLAlchemy: Query to fetch all decoders
    SQLAlchemy->>DB: Execute SELECT query
    DB-->>SQLAlchemy: Return list of decoders
    SQLAlchemy-->>DecoderModel: Return list of decoders

    Flask->>Browser: Return decoders list
    Browser->>Admin: Display list of decoders
