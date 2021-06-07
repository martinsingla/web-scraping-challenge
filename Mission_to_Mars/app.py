### Mars scrap-store-display app

from pymongo import collection
import scrap_mars 
from flask import Flask, render_template
import pymongo

app = Flask(__name__)

#Setup MongoDB connection to db
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db
scrap_data = db.scrap_data

# Home Route that will use MongoDB data to render HTML template
@app.route("/")
def home():

    mars_info = scrap_data.find_one()

    return render_template('index.html', mars_info = mars_info)


# Route that will trigger the scraping function and store new data in MongoDB
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_info = scrap_mars.scraper()

    #update data in mongodb
    collection.drop()
    collection.insert_many(mars_info)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)