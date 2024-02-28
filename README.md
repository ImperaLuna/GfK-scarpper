### City Gross Scraper

This scraper is designed to extract data from the meat section of the City Gross website. Initially, I encountered issues related to receiving a 403 Forbidden response and retrieving encrypted data. These issues were resolved by generating headers using Postman.

#### Approach:

I found an API endpoint that serves the meat category data. This API utilizes parameters `page` and `size` to paginate the results. After testing, I determined that setting the `size` parameter to 1000 allowed me to retrieve up to 150 products in a single request.

However, one downside of this approach is the accuracy of extracted prices. It appears that the method for determining prices on the site isn't entirely clear. Through manual testing on a small sample of items (10), I achieved an accuracy of 80% in extracting prices. All other data fields extracted were accurate.

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

