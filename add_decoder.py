from app import db
from app.models import Decoder

# Insert some decoders manually
new_decoder1 = Decoder(name='Decoder1', description='This is the first decoder.')
new_decoder2 = Decoder(name='Decoder2', description='This is the second decoder.')

# Add them to the session and commit
db.session.add(new_decoder1)
db.session.add(new_decoder2)
db.session.commit()

print('Decoders added successfully!')
