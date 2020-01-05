from config import app_config
from flask import Flask, render_template, request, redirect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app_contact_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    from contact_app.models import Contact
    from contact_app.forms import ContactCreateForm

    @app.route('/')
    def contact_list_view():
        all_contacts = Contact.query.all()
        return render_template('contact_list.html', all_contacts=all_contacts)

    @app.route('/<int:contact_id>')
    def contact_detail_view(contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        return render_template('contact_details.html', contact=contact)

    @app.route('/add/<int:contact_id>', methods=['GET', 'POST'])
    def contact_create_view(contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()  # checks already exists entry
        if contact:
            return "Contact with id {} already existing".format(contact_id)
        else:
            form = ContactCreateForm()
            form.id.default = contact_id
            if form.validate_on_submit():
                contact = Contact(
                    id=contact_id, email=form.data['email'],
                    first_name=form.data['first_name'], last_name=form.data['last_name'],
                    phone_number=form.data['phone_number'])
                db.session.add(contact)
                db.session.commit()
                return redirect('/')
            return render_template('contact_add.html', form=form, contact_id=contact_id)

    @app.route('/delete/<int:contact_id>', methods=['POST'])
    def contact_delete_view(contact_id):
        Contact.query.filter_by(id=contact_id).delete()
        db.session.commit()
        return redirect('/')

    @app.route('/search/<string:contact_name>')
    def contact_search_view(contact_name):
        contacts = Contact.query.filter(Contact.first_name.contains(contact_name))
        return render_template('contact_search.html', all_contacts=contacts)

    return app
