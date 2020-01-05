from contact_app import db


class Contact(db.Model):
    """
    Create an Employee table
    """

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    phone_number = db.Column(db.String(10), unique=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
