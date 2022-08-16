from selenium import webdriver
import argparse


def get_website_data(url):
    """A function that uses selenium to get the data from a website"""
    driver = webdriver.Firefox()
    driver.get(url)
    data = driver.find_element_by_tag_name('body')
    return data, driver


def main(args):
    url = args.url
    keyword = args.keyword
    data, driver = get_website_data(url)
    print(driver.find_element_by_id(keyword).text)
    driver.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default='https://google.com', help='url to scrape')
    parser.add_argument('--keyword', type=str, default='availabilityStatus', help='keyword to search for')
    args = parser.parse_args()
    main(args)

