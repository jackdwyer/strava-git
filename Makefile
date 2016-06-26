.PHONY: assets

years:
	./generate_maps_filter_year.py
	cp /tmp/*_index.html /home/jdwyer/programming/yearly_biking/
	cp /tmp/2016_index.html /home/jdwyer/programming/yearly_biking/index.html
	aws s3 cp --acl public-read /home/jdwyer/programming/yearly_biking/index.html s3://cycling.jackdwyer.org/ --profile personal
	aws s3 cp --acl public-read /home/jdwyer/programming/yearly_biking/2015_index.html s3://cycling.jackdwyer.org/ --profile personal

assets:
	aws s3 cp --acl public-read --recursive assets/ s3://cycling.jackdwyer.org/ --profile personal
