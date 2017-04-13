package: clean build
	zip -r -9 tickerdotph.zip tickerdotph/*
	cd build; zip -r -g ../tickerdotph.zip lxml
	cd build; zip -r -g ../tickerdotph.zip cssselect

clean:
	rm -fv *.zip
	rm -rfv build
	find . -type f -name "*.pyc" -delete

build:
	pip install -t build lxml
	pip install -t build cssselect
	find . -type f -name "*.pyc" -delete

