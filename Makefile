.PHONY: download PythonDataScienceHandbook UrbanDataChallenge \
	Altair QuanEcon NatureGenetics TensorflowExamples BuzzFeedNewsFakeNews
.PHONY: demo createfiles

demo: download createfiles
createfiles: move_this_file move_it_here
download: demofiles PythonDataScienceHandbook UrbanDataChallenge \
	Altair QuanEcon NatureGenetics TensorflowExamples BuzzFeedNewsFakeNews

PythonDataScienceHandbook: demofiles
	cd demofiles && git clone https://github.com/jakevdp/PythonDataScienceHandbook.git

UrbanDataChallenge: demofiles
	cd demofiles && git clone https://github.com/swissnexSF/Urban-Data-Challenge.git

Altair: demofiles
	cd demofiles && git clone https://github.com/altair-viz/altair.git

QuanEcon:
	cd demofiles && git clone https://github.com/QuantEcon/QuantEcon.notebooks.git

NatureGenetics:
	cd demofiles && git clone https://github.com/theandygross/TCGA.git

TensorflowExamples:
	cd demofiles && git clone https://github.com/aymericdamien/TensorFlow-Examples.git

BuzzFeedNewsFakeNews:
	cd demofiles && git clone https://github.com/BuzzFeedNews/2017-04-fake-news-ad-trackers.git

move_this_file: demofiles
	cd demofiles && touch move_this_file.txt

move_it_here: demofiles
	cd demofiles && mkdir move_it_here

demofiles:
	mkdir demofiles

clean:
	rm -rf demofiles

