from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from app import app, db  # Import db here
from app.models import User, Decoder, Client
from app.forms import LoginForm, RegistrationForm
from flask_bcrypt import Bcrypt
from app import db
#from app.models import Client
from app.forms import ClientForm
from flask import render_template, redirect, url_for
from flask_login import login_required

bcrypt = Bcrypt(app)

@app.route('/create_client', methods=['GET', 'POST'])
@login_required  # Ensure only logged-in users can create clients
def create_client():
    form = ClientForm()
    if form.validate_on_submit():
        # Create a new client object
        client = Client(name=form.name.data, description=form.description.data)

        # Add client to the database
        db.session.add(client)
        db.session.commit()

        # Redirect to a page that shows all clients (or wherever you want to go)
        return redirect(url_for('list_clients'))

    return render_template('create_client.html', form=form)

@app.route('/clients')
@login_required  # Ensure only logged-in users can access this page
def list_clients():
    clients = Client.query.all()  # Query all clients from the database
    return render_template('list_clients.html', clients=clients)

@app.route('/delete_client/<int:client_id>', methods=['GET', 'POST'])
@login_required  # Ensure only logged-in users can delete clients
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)  # Get the client by id, or 404 if not found
    
    # Delete the client from the database
    db.session.delete(client)
    db.session.commit()

    # Redirect back to the clients list
    return redirect(url_for('list_clients'))

@app.route('/decoders')
@login_required  # Ensure only logged-in users can access this page
def list_decoders():
    decoders = Decoder.query.all()  # Query all decoders from the database
    return render_template('list_decoders.html', decoders=decoders)


@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # Proper password checking with bcrypt
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)  # Add the user to the session
        db.session.commit()  # Commit the session to save the user

        return redirect(url_for('login'))
    return render_template('register.html', form=form)
