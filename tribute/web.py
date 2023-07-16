from flask import Flask

app = Flask(__name__)

@app.route("/")
def new():
    return '''<html>
    <head>
        <title>Hello</title>
        <link href="hello.css" rel="stylesheet" type="text/css" >
    </head>
    <body><center><button class="button"><a href="new.html">Click To See Tribute For TechnoBlade</a></button>
    </center>
        
    </body>
</html>'''

if __name__ == "__main__":
    app.run()
