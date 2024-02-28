### City Gross Scraper

This scraper is designed to extract data from the meat section of the City Gross website. Initially, I encountered issues related to receiving a 403 Forbidden response and retrieving encrypted data. These issues were resolved by generating headers using Postman.

#### Approach:

I found an API endpoint that serves the meat category data. This API utilizes parameters `page` and `size` to paginate the results. After testing, I determined that setting the `size` parameter to 1000 allowed me to retrieve up to 150 products in a single request.

Downside of this aporach seems to be the acuracy at wich the prices are extracted, didn't figure out excatly what sets the price in the site , with manual testing on a small amount of items (10) managed to get an acrruacy of 80%
Every other data field extracted is accurate.

#### Running the Script:

```bash
# Clone the repository:
git clone https://github.com/ImperaLuna/GfK-scarpper.git

# Navigate to the project directory:
cd GfK-scarpper

# Install the required dependencies:
pip install -r requirements.txt

# Run the script:
python main.py

