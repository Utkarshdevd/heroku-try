from flask import Flask, render_template, request, flash
from forms import ContactForm

# created new instance of Flask
app = Flask(__name__)

# preventing CSRF attacks
app.secret_key = 'development key'

# Mapped URL / function home()
@app.route('/')
def home():
	# returns rendered template
	return render_template('home.html')

# Mapped URL /about to about.html
@app.route('/about')
def about():
	return render_template('about.html')

# map form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
	# create ContactForm instance
	form = ContactForm()

	# request determines what type of request comes from browser
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form=form)
	elif request.method == 'GET':
		return render_template('contact.html', form=form)

# runs this app on a local server
if __name__ == '__main__':
	app.run(debug=True)