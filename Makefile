.PHONY: download PythonDataScienceHandbook Urban-Data-Challenge altair altair-examples
.PHONY: demo createfiles

demo: download createfiles
createfiles: move_this_file move_it_here
download: demofiles PythonDataScienceHandbook Urban-Data-Challenge altair

PythonDataScienceHandbook: demofiles
	cd demofiles && git clone https://github.com/jakevdp/PythonDataScienceHandbook.git

Urban-Data-Challenge: demofiles
	cd demofiles && git clone https://github.com/swissnexSF/Urban-Data-Challenge.git

altair: demofiles
	cd demofiles && git clone https://github.com/altair-viz/altair.git

move_this_file: demofiles
	cd demofiles && touch move_this_file.txt

move_it_here: demofiles
	cd demofiles && mkdir move_it_here

demofiles:
	mkdir demofiles

clean:
	rm -rf demofiles

