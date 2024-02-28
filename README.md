### City Gross Scraper

This scraper is designed to extract data from the meat section of the City Gross website. Initially, I encountered issues related to receiving a 403 Forbidden response and retrieving encrypted data. This issues were resolved by generating headers using Postman.

#### Approach:

Specifically for the meat category (would imagine rest of the categories are similar) i've found an api that uses parameter `page` and `size` to paginate the results. Figure out this would be the best aproach to retrieve a large amount of data in a single request. After testing, I determined that setting the `size` parameter to 1000 would allow to retrieve all the producs (total number of products is 150).

Downside of this aporach seems to be the acuracy at wich the prices are extracted, didn't figure out excatly what sets the price in the site , with manual testing on a small amount of items (10) managed to get an acrruacy of 80%
Every other data field extracted is accurate.

#### How I organized the code.

Split the code into 3 functions: 
main function takes care or the request part and printing the dictionary for the purpose of manual testing.

get_price function is a helper function for parse_data

parse_json creates and returns a dictionary with the following structure: 

```
parsed_data[key: index] = {
        'Product ID': str,      # Unique identifier for the product (string)
        'Product URL': str,     # URL of the product (string)
        'Product Name': str,    # Name of the product (string)
        'Brand': str,           # Brand of the product (string)
        'Price': float,         # Price of the product (float)
        'GTIN': str             # Global Trade Item Number of the product (string) 
```

## Running the Script:
Clone the repository:
`git clone https://github.com/ImperaLuna/GfK-scarpper.git`

Navigate to the project directory:
`cd GfK-scarpper`

Install the required dependencies:
`pip install -r requirements.txt`

Run the script:
`python main.py`

