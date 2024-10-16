import requests
from bs4 import BeautifulSoup
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample list of URLs
urls = [
    "https://www.informa.com/privacy-policy/",
    # "https://www.nigeria-energy.com/en/home.html",
    # "https://cloudsec-sg.coriniumintelligence.com/agenda",
    # "https://ciso-bris.coriniumintelligence.com/agenda",
    # # Other URLs...
    # "https://www.coriniumintelligence.com",
    # "https://www.coriniumintelligence.com/events-calendar?hsLang=en-gb",
    # "https://ciso-syd.coriniumintelligence.com?hsLang=en-gb",
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
    #   "https://cdao-nz.coriniumintelligence.com/",
    #     "https://cdao-frankfurt.coriniumintelligence.com/",
    #     "https://cdao-eu.coriniumintelligence.com/",
    #     "https://cdao-dallas.coriniumintelligence.com/",
    #     "https://ciso-canberra.coriniumintelligence.com",
    #     "https://cdao-nordics.coriniumintelligence.com",
    #     "https://ciso-id.coriniumintelligence.com",
    #     "https://cdao-federal.coriniumintelligence.com",
    #     "https://ciso-syd.coriniumintelligence.com",
    #     "https://data-analytics-live.coriniumintelligence.com/",
    #     "https://cdao-uk.coriniumintelligence.com/",
    #     "https://cloud-sec-syd.coriniumintelligence.com",
    #     "https://cdao-canada.coriniumintelligence.com/",
    #     "https://cdao-bris.coriniumintelligence.com",
    #     "https://cdaofs.coriniumintelligence.com/",
    #     "https://ciso-my.coriniumintelligence.com/",
    #     "https://cdao-germany.coriniumintelligence.com",
    #     "https://ciso-fsi-sg.coriniumintelligence.com/",
    #     "https://cdao-spring.coriniumintelligence.com/",
    #     "https://data-architecture-sg.coriniumintelligence.com/",
    #     "https://cdao-sg.coriniumintelligence.com/",
    #     "https://cdao-syd.coriniumintelligence.com",
    #     "https://cdao-france.coriniumintelligence.com/",
    #     "https://cdao-canada-ps.coriniumintelligence.com/",
    #     "https://cdao-apex-east.coriniumintelligence.com/",
    #     "https://cdao-fs-eu.coriniumintelligence.com/2024",
    #     "https://data-architecture-uk.coriniumintelligence.com",
    #     "https://ciso-fsi-anz.coriniumintelligence.com/",
    #     "https://datainhealthcare.coriniumintelligence.com/",
    #     "https://ciso-exec.coriniumintelligence.com/",
    #     "https://cdao-my.coriniumintelligence.com",
    #     "https://cloudsec-mel.coriniumintelligence.com/",
    #     "https://cdao-mel.coriniumintelligence.com/",
    #     "https://ciso-mel.coriniumintelligence.com/",
    #     "https://data-architecture.coriniumintelligence.com/",
]

# Keywords related to event-specific pages
event_keywords = ["agenda", "schedule", "event", "conference", "summit", "calendar","home.html"]
ignore_keywords = ["privacy-policy", "terms", "about", "contact", "help", "faq"]

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
    # Lowercase text for easier matching
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)

def contains_ignore_keywords(url, ignore_keywords):
    url_lower = url.lower()
    return any(ignore_keyword.lower() in url_lower for ignore_keyword in ignore_keywords)


# NLP function to extract content relevance using TF-IDF similarity
def is_event_related(text, keywords):
    # Tokenize and process text
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    
    # Create a list of texts to compare
    all_texts = [" ".join(tokens)] + keywords
    
    # Compute TF-IDF similarity
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    cosine_similarities = (tfidf_matrix * tfidf_matrix.T).toarray()
    
    # Check similarity score between text and keywords
    similarity_with_keywords = cosine_similarities[0][1:].mean()
    
    # Threshold for relevance (can be tuned)
    return similarity_with_keywords > 0.2

# Function to filter event-related URLs using both keyword and NLP approaches
def filter_event_links_nlp(links, keywords):
    event_related_links = []
    
    for url in links:
        # Skip URLs that contain ignore keywords
        if contains_ignore_keywords(url, ignore_keywords):
            continue


        text = get_page_text(url)
        
        if contains_event_keywords(text, keywords) or is_event_related(text, keywords):
            event_related_links.append(url)
    
    return list(set(event_related_links))  # Remove duplicates

# Extract event-related URLs
event_related_links = filter_event_links_nlp(urls, event_keywords)

# Print the unique event-related URLs
for url in event_related_links:
    print(url)
