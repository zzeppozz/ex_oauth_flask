# oAuth test application with Flask

## Get Google credentials

https://developers.google.com/identity/gsi/web
https://developers.google.com/identity/gsi/web/guides/overview

## Debugging


To run flask in debug mode, first setup virtual environment for python at the 
top level of the repo, activate, then add dependencies from requirements.txt:

```zsh
cd ~/git/ex_oauth_flask
python3 -m venv venv
. venv/bin/activate
pip3 install Flask Authlib requests
```

then start the flask application

```zsh
cd ~/git/ex_oauth_flask
export FLASK_ENV=development
export FLASK_APP=flask_app/routes
flask run
```

test through flask (no SSL):
http://localhost:5000/api/v1/name?namestr=Notemigonus%20crysoleucas%20(Mitchill,%201814)
http://localhost:5000/api/v1/occ?occid=01493b05-4310-4f28-9d81-ad20860311f3
