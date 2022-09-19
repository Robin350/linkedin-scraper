import logging

logger = logging.getLogger(__name__)

def parse_entity_results(entities):
    company_list = []
    for entity in entities:
        name = entity.find_element("class name", "app-aware-link").text
        subtitle = entity.find_element("class name", "entity-result__primary-subtitle").text
        location = subtitle.split(" • ")[1]
        followers_str = entity.find_element("class name", "entity-result__secondary-subtitle").text
        followers = followers_str.replace(" followers", "")
        multiply_by_1000 = "K" in followers
        followers = float(followers.replace("K", "")) * (1000 if multiply_by_1000 else 1)

        company_list.append({
            "name": name,
            "location": location,
            "followers": followers
        })
    return company_list

