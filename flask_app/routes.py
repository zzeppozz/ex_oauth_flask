from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template, session, url_for
# from flask_oauthlib.provider import OAuth2Provider

# ..........................
def load_app():    
    app = Flask(__name__, template_folder='templates', instance_relative_config=True)
    
    # oauth.init_app(app)
    
    app.config['SERVER_NAME'] = 'localhost:5000'
    # Preload config settings from module
    app.config.from_object('flask_app.default_settings')
    # Override default settings with file in instance folder
    app.config.from_object('flask_app.instance.local_settings')
    return app

# ..........................
app = load_app()
oauth = OAuth()
oauth.init_app(app)


# ..........................
@app.route('/')
def index():
    return render_template('index.html')

# ..........................
@app.route('/google/')
def google():   
    # Google Oauth Config
    GOOGLE_CLIENT_ID = app.config['GOOGLE_CLIENT_ID'] # os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = app.config['GOOGLE_CLIENT_SECRET'] # os.environ.get('GOOGLE_CLIENT_SECRET')
     
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
     
    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)
 
# ..........................
@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    session['user'] = user
    # session['user_id'] = user.
    print(" Google User ", user)
    return redirect('/')

# ..........................
if __name__ == "__main__":
    app = load_app()
    app.run(debug=True)


