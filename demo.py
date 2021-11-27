from flask import Flask, render_template_string

demo = Flask(__name__)

@demo.route('/')
def home():
    return '''
    <html>
        <head>
            <title>P-cap Templated Mock</title>
        </head>
        <body>
            <h1>Site is still under construction</h1>
            <p>Powered by Flask/Jinja2</p>
        </body>
    </html>'''

@demo.route("/<path_param>")
@demo.errorhandler(404)
def under_construction(path_param):
    return render_template_string('''
         <html>
            <head>
                <title>P-cap Templated Mock</title>
            </head>
            <body>
                <h1>Error 404</h1>
                <p>The page ''' + path_param + ''' could not be found</p>
            </body>
        </html>''')
  
if __name__ == "__main__":
# THe line below is great for dynamically changing code within this app
    demo.run(debug=True)
