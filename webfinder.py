from selenium import webdriver
import argparse


def get_website_data(url):
    """A function that uses selenium to get the data from a website"""
    driver = webdriver.Firefox()
    driver.get(url)
    return driver


def main(args):
    url = args.url
    keyword = args.keyword
    driver = get_website_data(url)
    elements = driver.find_elements_by_class_name(keyword)
    next_page_button_id = args.next_page_button
    all_elements = [element.text for element in elements]
    while driver.find_element_by_id(next_page_button_id).is_enabled():
        driver.find_element_by_id(next_page_button_id).click()
        elements = driver.find_elements_by_class_name(keyword)
        all_elements += [element.text for element in elements]
    print(all_elements)
    if args.product_name in all_elements:
        print("Product found")
    driver.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default='https://google.com', help='url to scrape')
    parser.add_argument('--keyword', type=str, default='availabilityStatus', help='The element class name to search for')
    # product name argument
    parser.add_argument('--product_name', type=str, default='productName', help='The product name to search for on all pages')
    # next page button argument
    parser.add_argument('--next_page_button', type=str, default='next-page-button', help='The html id of the next page button')
    args = parser.parse_args()
    main(args)

