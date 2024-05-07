from web_app.routes.auth_routes import auth_routes


@auth_routes.route("/auth/google/login")
def google_login():
    print("GOOGLE OAUTH LOGIN...")
    oauth = current_app.config["OAUTH"]
    redirect_uri = url_for("auth_routes.google_oauth_callback", _external=True) # see corresponding route below
    return oauth.google.authorize_redirect(redirect_uri) # send the user to login with google, then hit the callback route