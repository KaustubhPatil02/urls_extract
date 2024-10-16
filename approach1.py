# Sample list of URLs
urls = [
    "https://www.coriniumintelligence.com",
    "https://www.coriniumintelligence.com/events-calendar?hsLang=en-gb",
    "https://ciso-syd.coriniumintelligence.com?hsLang=en-gb",
    "https://cloud-sec-syd.coriniumintelligence.com?hsLang=en-gb",
    "https://datainhealthcare.coriniumintelligence.com/?hsLang=en-gb",
    "https://cdao-my.coriniumintelligence.com?hsLang=en-gb",
    "https://data-architecture-sg.coriniumintelligence.com/?hsLang=en-gb",
    "https://cloudsec-sg.coriniumintelligence.com/agenda",
    "https://ciso-bris.coriniumintelligence.com/agenda",
    "https://cdao-nz.coriniumintelligence.com/agenda",
    "https://cdao-frankfurt.coriniumintelligence.com/schedule-2024",
    "https://cdao-dallas.coriniumintelligence.com/agenda",
    "https://cdao-fs-eu.coriniumintelligence.com/agenda",
    "https://cdao-gov.coriniumintelligence.com/agenda",
    "https://cdao-germany.coriniumintelligence.com/schedule",
      "https://cdao-nz.coriniumintelligence.com/",
        "https://cdao-frankfurt.coriniumintelligence.com/",
        "https://cdao-eu.coriniumintelligence.com/",
        "https://cdao-dallas.coriniumintelligence.com/",
        "https://ciso-canberra.coriniumintelligence.com",
        "https://cdao-nordics.coriniumintelligence.com",
        "https://ciso-id.coriniumintelligence.com",
        "https://cdao-federal.coriniumintelligence.com",
        "https://ciso-syd.coriniumintelligence.com",
        "https://data-analytics-live.coriniumintelligence.com/",
        "https://cdao-uk.coriniumintelligence.com/",
        "https://cloud-sec-syd.coriniumintelligence.com",
        "https://cdao-canada.coriniumintelligence.com/",
        "https://cdao-bris.coriniumintelligence.com",
        "https://cdaofs.coriniumintelligence.com/",
        "https://ciso-my.coriniumintelligence.com/",
        "https://cdao-germany.coriniumintelligence.com",
        "https://ciso-fsi-sg.coriniumintelligence.com/",
        "https://cdao-spring.coriniumintelligence.com/",
        "https://data-architecture-sg.coriniumintelligence.com/",
        "https://cdao-sg.coriniumintelligence.com/",
        "https://cdao-syd.coriniumintelligence.com",
        "https://cdao-france.coriniumintelligence.com/",
        "https://cdao-canada-ps.coriniumintelligence.com/",
        "https://cdao-apex-east.coriniumintelligence.com/",
        "https://cdao-fs-eu.coriniumintelligence.com/2024",
        "https://data-architecture-uk.coriniumintelligence.com",
        "https://ciso-fsi-anz.coriniumintelligence.com/",
        "https://datainhealthcare.coriniumintelligence.com/",
        "https://ciso-exec.coriniumintelligence.com/",
        "https://cdao-my.coriniumintelligence.com",
        "https://cloudsec-mel.coriniumintelligence.com/",
        "https://cdao-mel.coriniumintelligence.com/",
        "https://ciso-mel.coriniumintelligence.com/",
        "https://data-architecture.coriniumintelligence.com/",
        # "https://cloudsec-sg.coriniumint
]

# Keywords related to event-specific URLs
event_keywords = ["agenda", "schedule", "event", "calendar"]

#just a func
def filter_event_links(links, keywords):
    return [url for url in links if any(keyword in url for keyword in keywords)]

#extract the urls
event_related_links = filter_event_links(urls, event_keywords)

# Printing 
for url in event_related_links:
    print(url)
