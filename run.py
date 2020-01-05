import os

from contact_app import create_app_contact_app

config_name = os.environ.get('FLASK_CONFIG', 'development')
app = create_app_contact_app(config_name)

if __name__ == '__main__':
    app.run()
