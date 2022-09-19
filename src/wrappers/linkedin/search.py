from src.wrappers.linkedin.connect import linkedin_connection
from src.wrappers.linkedin.parser import parse_entity_results
from time import sleep


def search_learning_companies(technology):
    driver = linkedin_connection.driver
    driver.get(
        f"https://www.linkedin.com/search/results/all/"
        f"?keywords={technology}"
        f"&origin=GLOBAL_SEARCH_HEADER"
    )
    sleep(5)
    companies_button = driver.find_element("xpath", "//button[text()='Companies']")
    companies_button.click()
    sleep(2)
    industry_button = driver.find_element("xpath", "//button[text()='Industry']")
    industry_button.click()
    sleep(1)
    filter_button = driver.find_element("placeholder", "Add an industry")
    filter_button.send_keys("E-learning providers")
    sleep(1)
    industry_button.click()
    sleep(1)
    companies = []
    for page in range(2, 25):
        try:
            driver.find_element("xpath", "//h2[text()='No results found']")
            break
        except Exception as e:
            pass
        breakpoint()
        companies.extend(parse_entity_results(
            driver.find_elements("class name", "entity-result__content")
        ))
        page += 1
        driver.get(
            f"https://www.linkedin.com/search/results/companies/"
            f"?industry=['132']"
            f"&keywords={technology}"
            f"&origin=FACETED_SEARCH"
            f"&page={page}"
        )
    return companies



