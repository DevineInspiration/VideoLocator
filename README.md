# VideoLocator

Script using Natural Language Processing in Python to scrape all videos on a chosen YouTube channel, utilising the captions/title/description to provide location information to allow for easier locating of where videos are shot.
Current development builds are being tested on Tom Scott videos. The end goal of this project is to get to roughly a similar accuracy as the community maintained [TomScottMap](https://github.com/frog23/TomScottMap)

## Dependancies

Built on and for <strong> Python 3.13.3 </strong>

Due to the the use of SpaCy, Visual Studio C++ build tools is required: which can be downloaded [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

The Python modules used are: <br />
[NLTK](https://pypi.org/project/nltk/) <br />
[locationtagger](https://pypi.org/project/locationtagger/) <br />
[SpaCy](https://pypi.org/project/spacy/) <br />
[pytubefix](https://pypi.org/project/pytubefix/) <br />
