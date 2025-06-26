# import the Flask library so we can create a server side application
from flask import Flask
from datetime import datetime

# Here we create an instance of the Flask class, think of this as creating an object.
# This object will act as a web server and we will give our application a name of app.
# The __name__ is a special variable in Python that is set to the name of the module.
# Don't worry about this for now.
app = Flask(__name__)

# Now let's create a route for our application.
# A route is a path on the web server that our application will respond to.
# / is the root route, it is the default route that our application will respond to.
@app.route('/')

# now let create a function that will be called when the user navigates to the root route.
def index():
    # Create a variable to hold the date and time to display on the webpage.
    date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create a variable called webpage_content
    webpage_content = '''
<!DOCTYPE html>
<html lang="en">
<!-- This is the head section of the HTML document. -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Racing Cars</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background-color: #222;
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        .car {
            margin-bottom: 20px;
        }
        .car img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Racing Cars World</h1>
        <p>The current date and time is: ''' + date_and_time + '''</p>
    </header>
    <main>
        <section class="car">
            <h2>Formula 1</h2>

            <p>Formula 1 cars are the pinnacle of racing technology, reaching speeds over 200 mph with cutting-edge aerodynamics and engineering.</p>
        </section>
        <section class="car">
            <h2>Le Mans Prototypes</h2>
            
            <p>Designed for endurance racing, Le Mans prototypes are built to last 24-hour races while maintaining high speed and performance.</p>
        </section>
        <section class="car">
            <h2>Rally Cars</h2>
  
            <p>Rally cars compete on various surfaces and weather conditions, emphasizing driver skill and vehicle durability.</p>
        </section>
    </main>
</body>
</html>
'''
    # This is the response that will be sent to the user's browser aka the client.
    return webpage_content

# Now let's create a route for the about page.
@app.route('/about')
def about():
    # Create a variable called webpage_content
    webpage_content = '''
    <h2>This is the future home of the about page.</h2>
    '''
    # This is the response that will be sent to the user's browser aka the client.
    return webpage_content


# This is a special command that will run the application.
# It will start the web server and listen for requests.
if __name__ == '__main__':
    # This will start the webserver on port 5000.
    # if your port is already in use, you can change the port number.
    # Keep this number in mind, you will need it to access the application.
    # debug=True will give you more information about the server.
    # very useful for debugging and troubleshooting.
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0')



