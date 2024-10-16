import requests
from bs4 import BeautifulSoup
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample list of URLs
urls = [
    "https://data-analytics-live.coriniumintelligence.com/book-a-call-spex",
    "https://www.informa.com/privacy-policy/",
    "https://www.nigeria-energy.com/en/home.html",
    "https://cloudsec-sg.coriniumintelligence.com/agenda",
    "https://ciso-bris.coriniumintelligence.com/agenda",
    "https://www.coriniumintelligence.com",
    "https://www.coriniumintelligence.com/events-calendar?hsLang=en-gb",
    "https://ciso-syd.coriniumintelligence.com?hsLang=en-gb",
    # "https://cloud-sec-syd.coriniumintelligence.com?hsLang=en-gb",
    # "https://datainhealthcare.coriniumintelligence.com/?hsLang=en-gb",
    # "https://cdao-my.coriniumintelligence.com?hsLang=en-gb",
    # "https://data-architecture-sg.coriniumintelligence.com/?hsLang=en-gb",
    # "https://cloudsec-sg.coriniumintelligence.com/agenda",
    # "https://ciso-bris.coriniumintelligence.com/agenda",
    # "https://cdao-nz.coriniumintelligence.com/agenda",
    # "https://cdao-frankfurt.coriniumintelligence.com/schedule-2024",
    # "https://cdao-dallas.coriniumintelligence.com/agenda",
    # "https://cdao-fs-eu.coriniumintelligence.com/agenda",
    # "https://cdao-gov.coriniumintelligence.com/agenda",
    # "https://cdao-germany.coriniumintelligence.com/schedule",
    # "https://cdao-nz.coriniumintelligence.com/",
    # "https://cdao-frankfurt.coriniumintelligence.com/",
    # "https://cdao-eu.coriniumintelligence.com/",
    # "https://cdao-dallas.coriniumintelligence.com/",
    # "https://ciso-canberra.coriniumintelligence.com",
    # "https://cdao-nordics.coriniumintelligence.com",
    # "https://ciso-id.coriniumintelligence.com",
    # "https://cdao-federal.coriniumintelligence.com",
    # "https://ciso-syd.coriniumintelligence.com",
    # "https://data-analytics-live.coriniumintelligence.com/",
    # "https://cdao-uk.coriniumintelligence.com/",
    # "https://cloud-sec-syd.coriniumintelligence.com",
    # "https://cdao-canada.coriniumintelligence.com/",
    # "https://cdao-bris.coriniumintelligence.com",
    # "https://cdaofs.coriniumintelligence.com/",
    # "https://ciso-my.coriniumintelligence.com/",
    # "https://cdao-germany.coriniumintelligence.com",
    # "https://ciso-fsi-sg.coriniumintelligence.com/",
    # "https://cdao-spring.coriniumintelligence.com/",
    # "https://data-architecture-sg.coriniumintelligence.com/",
    # "https://cdao-sg.coriniumintelligence.com/",
    # "https://cdao-syd.coriniumintelligence.com",
    # "https://cdao-france.coriniumintelligence.com/",
    # "https://cdao-canada-ps.coriniumintelligence.com/",
    # "https://cdao-apex-east.coriniumintelligence.com/",
    # "https://cdao-fs-eu.coriniumintelligence.com/2024",
    # "https://data-architecture-uk.coriniumintelligence.com",
    # "https://ciso-fsi-anz.coriniumintelligence.com/",
    # "https://datainhealthcare.coriniumintelligence.com/",
    # "https://ciso-exec.coriniumintelligence.com/",
    # "https://cdao-my.coriniumintelligence.com",
    # "https://cloudsec-mel.coriniumintelligence.com/",
    # "https://cdao-mel.coriniumintelligence.com/",
    # "https://ciso-mel.coriniumintelligence.com/",
    # "https://data-architecture.coriniumintelligence.com/",
    # "https://www.brazilwindpower.com.br/en/home.html",
    # "https://cdao-apex-east.coriniumintelligence.com/venue",
    # "https://cdao-eu.coriniumintelligence.com",
    # "https://cdao-apex-east.coriniumintelligence.com/suggest-a-speaker",
    # "https://cdao-apex-east.coriniumintelligence.com/agenda",
    # "https://cdao-apex-east.coriniumintelligence.com/agenda-download",
    # "https://cdao-eu.coriniumintelligence.com/agenda-download-2024",
    # "https://www.africahealthexhibition.com/en/conferences/overview.html",
    # "https://www.terrapinn.com/anti-slavery-policy",
    # "https://www.coriniumintelligence.com/privacy-policy",
    # "https://www.fastmarkets.com/privacy-notice/",
    # "https://www.fastmarkets.com/about-us/",
    # "https://www.logytalks.com/terms-conditions",
    # "https://www.informamarkets.com/en/visitor-terms-and-conditions.html",
    # vaibhav's urls
     "https://ot-security-syd.coriniumintelligence.com?hsLang=en-gb",
        "https://ciso-syd.coriniumintelligence.com?hsLang=en-gb",
        "https://ciso-exec.coriniumintelligence.com/?hsLang=en-gb",
        "https://cloud-sec-syd.coriniumintelligence.com?hsLang=en-gb",
        "https://appsec-devsecops-syd.coriniumintelligence.com?hsLang=en-gb",
        "https://ciso-fsi-anz.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-my.coriniumintelligence.com?hsLang=en-gb",
        "https://datainhealthcare.coriniumintelligence.com/?hsLang=en-gb",
        "https://ciso-canberra.coriniumintelligence.com?hsLang=en-gb",
        "https://ciso-mel.coriniumintelligence.com/?hsLang=en-gb",
        "https://cloudsec-mel.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-mel.coriniumintelligence.com/?hsLang=en-gb",
        "https://ciso-my.coriniumintelligence.com/?hsLang=en-gb",
        "https://data-architecture.coriniumintelligence.com/?hsLang=en-gb",
        "https://cloudsec-sg.coriniumintelligence.com/?hsLang=en-gb",
        "https://ciso-fsi-sg.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-perth.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-id.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-sg.coriniumintelligence.com/?hsLang=en-gb",
        "https://data-architecture-sg.coriniumintelligence.com/?hsLang=en-gb",
        "https://ciso-bris.coriniumintelligence.com/?hsLang=en-gb",
        "https://data-architecture-syd.coriniumintelligence.com?hsLang=en-gb",
        "https://devops-syd.coriniumintelligence.com/?hsLang=en-gb",
        "https://ciso-id.coriniumintelligence.com?hsLang=en-gb",
        "https://cdao-bris.coriniumintelligence.com?hsLang=en-gb",
        "https://cdao-nz.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-syd.coriniumintelligence.com?hsLang=en-gb",
        "https://devops-mel.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-germany.coriniumintelligence.com?hsLang=en-gb",
        "https://data-architecture-nz.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-spring.coriniumintelligence.com/?hsLang=en-gb",
        "https://da-metro-chicago.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-uk.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-dallas.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-federal.coriniumintelligence.com?hsLang=en-gb",
        "https://data-analytics-live.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-france.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-canada.coriniumintelligence.com/?hsLang=en-gb",
        "https://ciso-ps.coriniumintelligence.com?hsLang=en-gb",
        "https://cdao-apex-east.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-eu.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-nordics.coriniumintelligence.com?hsLang=en-gb",
        "https://data-architecture-uk.coriniumintelligence.com?hsLang=en-gb",
        "https://cdao-fall.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-frankfurt.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-fs-eu.coriniumintelligence.com/2024?hsLang=en-gb",
        "https://cdao-gov.coriniumintelligence.com/?hsLang=en-gb",
        "https://cdao-perth.coriniumintelligence.com/",
        "https://cdao-frankfurt.coriniumintelligence.com/",
        "https://cdao-fall.coriniumintelligence.com/",
        "https://cdao-nz.coriniumintelligence.com/",
        "https://cdao-eu.coriniumintelligence.com/",
        "https://ciso-canberra.coriniumintelligence.com",
        "https://cdao-nordics.coriniumintelligence.com",
        "https://cdao-dallas.coriniumintelligence.com/",
        "https://ciso-id.coriniumintelligence.com",
        "https://cdao-federal.coriniumintelligence.com",
        "https://ciso-syd.coriniumintelligence.com",
        "https://ot-security-syd.coriniumintelligence.com",
        "https://data-analytics-live.coriniumintelligence.com/",
        "https://cdao-uk.coriniumintelligence.com/",
        "https://appsec-devsecops-syd.coriniumintelligence.com",
        "https://cloud-sec-syd.coriniumintelligence.com",
        "https://ciso-my.coriniumintelligence.com/",
        "https://cdao-bris.coriniumintelligence.com",
        "https://cdao-canada.coriniumintelligence.com/",
        "https://cdao-spring.coriniumintelligence.com/",
        "https://cdao-germany.coriniumintelligence.com",
        "https://ciso-fsi-sg.coriniumintelligence.com/",
        "https://cdao-sg.coriniumintelligence.com/",
        "https://cdao-apex-east.coriniumintelligence.com/",
        "https://cdao-france.coriniumintelligence.com/",
        "https://cdao-syd.coriniumintelligence.com",
        "https://data-architecture-sg.coriniumintelligence.com/",
        "https://ciso-exec.coriniumintelligence.com/",
        "https://data-architecture-uk.coriniumintelligence.com",
        "https://cdao-fs-eu.coriniumintelligence.com/2024",
        "https://datainhealthcare.coriniumintelligence.com/",
        "https://ciso-fsi-anz.coriniumintelligence.com/",
        "https://cdao-my.coriniumintelligence.com",
        "https://ciso-mel.coriniumintelligence.com/",
        "https://cloudsec-mel.coriniumintelligence.com/",
        "https://data-architecture.coriniumintelligence.com/",
        "https://cdao-mel.coriniumintelligence.com/",
        "https://cloudsec-sg.coriniumintelligence.com/",
        "https://cdao-id.coriniumintelligence.com/",
        "https://ciso-bris.coriniumintelligence.com/",
        "https://data-architecture-syd.coriniumintelligence.com",
        "https://devops-syd.coriniumintelligence.com/",
        "https://devops-mel.coriniumintelligence.com/",
        "https://da-metro-chicago.coriniumintelligence.com/",
        "https://data-architecture-nz.coriniumintelligence.com/",
        "https://ciso-ps.coriniumintelligence.com",
        "https://cdao-gov.coriniumintelligence.com/",
        "https://www.coriniumintelligence.com/content/page/2",
        "https://ot-security-syd.coriniumintelligence.com/exclusive-content",
        "https://ciso-syd.coriniumintelligence.com/request-to-speak",
        "https://ciso-syd.coriniumintelligence.com/exclusive-content",
        "https://ciso-exec.coriniumintelligence.com",
        "https://cloud-sec-syd.coriniumintelligence.com/",
        "https://ciso-syd.coriniumintelligence.com/",
        "https://ciso-exec.coriniumintelligence.com/partners",
        "https://ciso-exec.coriniumintelligence.com/content",
        "https://appsec-devsecops-syd.coriniumintelligence.com/request-to-speak",
        "https://cloud-sec-syd.coriniumintelligence.com/exclusive-content",
        "https://appsec-devsecops-syd.coriniumintelligence.com/exclusive-content",
        "https://ciso-fsi-anz.coriniumintelligence.com",
        "https://datainhealthcare.coriniumintelligence.com",
        "https://datainhealthcare.coriniumintelligence.com/request-to-speak",
        "https://ciso-fsi-anz.coriniumintelligence.com/exclusive-content",
        "https://datainhealthcare.coriniumintelligence.com/partners",
        "https://ciso-canberra.coriniumintelligence.com/request-to-speak",
        "https://datainhealthcare.coriniumintelligence.com/content",
        "https://ciso-canberra.coriniumintelligence.com/exclusive-content",
        "https://ciso-canberra.coriniumintelligence.com/partners",
        "https://ciso-bris.coriniumintelligence.com",
        "https://devops-mel.coriniumintelligence.com",
        "https://ciso-nz.coriniumintelligence.com",
        "https://cdao-my.coriniumintelligence.com/request-to-speak",
        "https://cdao-my.coriniumintelligence.com/partners",
        "https://cdao-my.coriniumintelligence.com/content-2024",
        "https://cdao-id.coriniumintelligence.com",
        "https://ciso-mel.coriniumintelligence.com",
        "https://ciso-mel.coriniumintelligence.com/content-new",
        "https://ciso-mel.coriniumintelligence.com/partners",
        "https://cloudsec-mel.coriniumintelligence.com",
        "https://cloudsec-mel.coriniumintelligence.com/content",
        "https://cloudsec-mel.coriniumintelligence.com/partners",
        "https://cdao-mel.coriniumintelligence.com",
        "https://cdao-mel.coriniumintelligence.com/content",
        "https://cdao-perth.coriniumintelligence.com",
        "https://cdao-nz.coriniumintelligence.com",
        "https://cdao-mel.coriniumintelligence.com/partners",
        "https://data-architecture.coriniumintelligence.com",
        "https://ciso-my.coriniumintelligence.com",
        "https://cdao-syd.coriniumintelligence.com/2024",
        "https://ciso-my.coriniumintelligence.com/request-to-speak",
        "https://data-architecture.coriniumintelligence.com/content",
        "https://data-architecture.coriniumintelligence.com/partners",
        "https://cloudsec-sg.coriniumintelligence.com/request-to-speak",
        "https://cloudsec-sg.coriniumintelligence.com",
        "https://cloudsec-sg.coriniumintelligence.com/partners",
        "https://cloudsec-sg.coriniumintelligence.com/content",
        "https://ciso-fsi-sg.coriniumintelligence.com",
        "https://ciso-sing.coriniumintelligence.com/",
        "https://cdao-perth.coriniumintelligence.com/content",
        "https://cdao-perth.coriniumintelligence.com/partners",
        "https://cdao-id.coriniumintelligence.com/request-to-speak",
        "https://cdao-id.coriniumintelligence.com/book-a-call",
        "https://cdao-id.coriniumintelligence.com/partners",
        "https://cdao-id.coriniumintelligence.com/content",
        "https://data-architecture-sg.coriniumintelligence.com",
        "https://cdao-sg.coriniumintelligence.com/old-home",
        "https://ciso-bris.coriniumintelligence.com/exclusive-content",
        "https://data-architecture-syd.coriniumintelligence.com/exclusive-content",
        "https://data-architecture-syd.coriniumintelligence.com/partners",
        "https://devops-syd.coriniumintelligence.com",
        "https://devops-syd.coriniumintelligence.com/request-to-speak",
        "https://devops-syd.coriniumintelligence.com/partners",
        "https://devops-syd.coriniumintelligence.com/book-a-call-with-rhys",
        "https://ciso-id.coriniumintelligence.com/request-to-speak",
        "https://devops-syd.coriniumintelligence.com/content",
        "https://ciso-id.coriniumintelligence.com/partners",
        "https://ciso-id.coriniumintelligence.com/content",
        "https://cdao-bris.coriniumintelligence.com/",
        "https://cdao-bris.coriniumintelligence.com/exclusive-content",
        "https://cdao-syd.coriniumintelligence.com/",
        "https://data-architecture-syd.coriniumintelligence.com/",
        "https://cdao-nz.coriniumintelligence.com/request-to-speak",
        "https://cdao-nz.coriniumintelligence.com/content",
        "https://cdao-nz.coriniumintelligence.com/partners",
        "https://devops-mel.coriniumintelligence.com/request-to-speak",
        "https://data-architecture-nz.coriniumintelligence.com",
        "https://devops-mel.coriniumintelligence.com/exclusive-content",
        "https://data-architecture-nz.coriniumintelligence.com/content",
        "https://data-architecture-nz.coriniumintelligence.com/partners",
        "https://cdao-germany.coriniumintelligence.com/schedule",
        "https://cdao-spring.coriniumintelligence.com",
        "https://da-metro-chicago.coriniumintelligence.com",
        "https://da-metro-chicago.coriniumintelligence.com/book-a-call-spex",
        "https://cdao-dallas.coriniumintelligence.com",
        "https://cdao-dallas.coriniumintelligence.com/book-a-call-spex",
        "https://cdao-uk.coriniumintelligence.com",
        "https://cdao-uk.coriniumintelligence.com/event-videos-2024",
        "https://data-analytics-live.coriniumintelligence.com",
        "https://cdao-france.coriniumintelligence.com",
        "https://cdao-canada.coriniumintelligence.com/team",
        "https://cdao-canada.coriniumintelligence.com/book-a-call-spex",
        "https://ciso-ps.coriniumintelligence.com/partners",
        "https://ciso-ps.coriniumintelligence.com/content",
        "https://aicyber.coriniumintelligence.com",
        "https://cdao-apex-east.coriniumintelligence.com/apex",
        "https://cdao-eu.coriniumintelligence.com",
        "https://cdao-fall.coriniumintelligence.com/corinium-gala",
        "https://cdao-fall.coriniumintelligence.com/corinium-awards-ticket",
        "https://cdao-frankfurt.coriniumintelligence.com",
        "https://cdao-frankfurt.coriniumintelligence.com/schedule-2024",
        "https://cdao-fs-eu.coriniumintelligence.com",
        "https://cdao-gov.coriniumintelligence.com",
        "https://cdao-gov.coriniumintelligence.com/team",
]

# Keywords related to event-specific pages
event_keywords = ["agenda", "schedule", "event", "conference", "summit", "calendar","home.html"]
ignore_keywords = ["privacy-policy", "terms", "about", "contact", "help", "faq", "cookie", "policy", "notice", "visitor", "terms-and-conditions","anti-slavery-policy", "logytalks", "informamarkets", "fastmarkets","book-a-call-spex"] 
# add more keywords here
# Function to get the text from a webpage
def get_page_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract all text from the page
        text = soup.get_text(separator=" ").strip()
        return text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Function to check if the text contains any event-related keywords
def contains_event_keywords(text, keywords):
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)

def contains_ignore_keywords(url, ignore_keywords):
    url_lower = url.lower()
    return any(ignore_keyword.lower() in url_lower for ignore_keyword in ignore_keywords)

# NLP function to extract content relevance using TF-IDF similarity
def is_event_related(text, keywords):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    
    all_texts = [" ".join(tokens)] + keywords
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    cosine_similarities = (tfidf_matrix * tfidf_matrix.T).toarray()
    
    similarity_with_keywords = cosine_similarities[0][1:].mean()
    
    return similarity_with_keywords > 0.2

# Function to filter event-related URLs using both keyword and NLP approaches
def filter_event_links_nlp(links, keywords):
    results = {}
    
    for url in links:
        # Skip URLs that contain ignore keywords
        if contains_ignore_keywords(url, ignore_keywords):
            results[url] = False
            continue

        text = get_page_text(url)
        
        if contains_event_keywords(text, keywords) or is_event_related(text, keywords):
            results[url] = True
        else:
            results[url] = False

    return results  # Return results dictionary

# Extract event-related URLs
event_related_results = filter_event_links_nlp(urls, event_keywords)

# Print the results
for url, is_event in event_related_results.items():
    print(f"{url} - {is_event}")