import requests


def parse_data_to_dict(data):
    """
    Parse JSON response into a dictionary with specified keys.

    Args:
        - data (dict): JSON response data.

    Returns:
        - dict: Dictionary with the structure:

        parsed_data[key: index] = {
        'Product ID': str,      # Unique identifier for the product (string)
        'Product URL': str,     # URL of the product (string)
        'Product Name': str,    # Name of the product (string)
        'Brand': str,           # Brand of the product (string)
        'Price': float,         # Price of the product (float)
        'GTIN': str             # Global Trade Item Number of the product (string)
        }


    """
    parsed_data = {}
    # base url is used in generating the product page for manual testing
    base_url = "www.citygross.se/matvaror"

    for index, item in enumerate(data['data'], start=1):
        product_info = {
            # took the liberty to add url and product id for the purpose of manual testing
            'Product ID': item['id'],
            'Product URL': f"{base_url}{item['url']}",
            'Product Name': item['name'],
            'Brand': item['brand'],
            'Price': get_price(item),
            'GTIN': item['gtin']
        }
        parsed_data[index] = product_info
    return parsed_data


def get_price(item: dict) -> float:
    """
    Retrieve price information from the item.

    Args:
       - item (dict): Dictionary containing product information

    Returns:
       - float (or int) representing the price of the product
    """

    # Todo: The function is not working entirely correct (upon testing it seems to generate 8/10 correct prices)
    # we are checking if the has promotion is set to true and than try to retrieve the promotion price
    # if it doesn't exist we retrieve the current price instead (not always the actual price in the website)
    if item['prices'][0]['hasPromotion']:
        try:
            return item['prices'][0]['promotions'][0]['value']
        except (KeyError, IndexError):
            return item['prices'][0]['currentPrice']['price']
    else:
        return item['prices'][0]['currentPrice']['price']


def main():
    # the parameter size=10 can be change to lower the amount of requests done
    # it's set to 10 in order to allow for a fast execution of the script
    # tested up to 1000 generating a total of 150 products
    # the url is specific for the meat category
    url = "https://www.citygross.se/api/v1/esales/products?categoryId=1493&size=100"

    # <--------------------------Automatically generated via Postman--------------------------------->
    # used to bypass the return of encrypted data from the url

    payload = {}
    headers = {
        'authority': 'www.citygross.se',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.8',
        'cookie': 'e_sk=da9a3674-a6fd-46c4-9fdd-3b083afd96d0',
        'referer': 'https://www.citygross.se/matvaror/kott-och-fagel?page=2',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    # <--------------------------Automatically generated via Postman--------------------------------->

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        parsed_data = parse_data_to_dict(data)
        for index, product_info in parsed_data.items():
            print(f"Key: {index}")
            for key, value in product_info.items():
                print(f"{key}: {value}")
            print()
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()