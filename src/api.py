# @app.route('/user/<user>')
def show_user_profile(user):
  return 'Hello {user}'.format(user=user)
