# Script to scrape a Youtube channel for all locations mentioned in the video and its title/description
# R. Devine 25.05.2025

import nltk
import lxml
import locationtagger
import spacy
from pytubefix import Channel

# essential entity model downloads
nltk.downloader.download('maxent_ne_chunker_tab')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')



# youtube page to be scanned [Modify this]
channel = Channel("https://www.youtube.com/@TomScottGo")

# load natural language python model
nlp = spacy.load('en_core_web_sm')

# itterate through videos on the channel
for video in channel.videos:
    desc = video.description

    # try load manually entered english captions, then auto generated captions
    try :
        subs = video.captions['en']
    except:
        subs = video.captions['a.en']
        
    print("Video Title: "+video.title)
    # use locationtagger NLP to do initial sweep through text for locations
    place_entity = locationtagger.find_locations(text = desc)
    places_spoken = locationtagger.find_locations(text = subs.generate_srt_captions())

    # use basic python NLP to filter returned values to countries, regions and cities.
    doc = nlp(str(place_entity.countries)+" "+str(place_entity.regions)+" "+str(place_entity.cities)+video.title)
    doc2 = nlp(str(places_spoken.countries)+" "+str(places_spoken.regions)+" "+str(places_spoken.cities))


    # filter by GPE label filter to only return geopolitical entities, and filter out duplicate entries
    seen=set()
    heard=set()
    locations = ""
    locations_mentioned = ""

    for entity in doc.ents:
       if entity.label_ == 'GPE' and entity.text not in seen: 
          locations = locations+entity.text+" "
          seen.add(entity.text)

    for entity in doc2.ents:
       if entity.label_ == 'GPE' and entity.text not in heard:
          locations_mentioned = locations_mentioned+entity.text+" "
          heard.add(entity.text)
    
    print("Locations recognised: "+locations)
    print("Locations mentioned: "+locations_mentioned+"\n")
    
    
