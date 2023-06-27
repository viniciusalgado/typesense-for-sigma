# This is a fork with specific configurations for internal use of typesense

In order to run it, follow the tutorials at:
https://typesense.org/guide/
https://github.com/algolia/docsearch-scraper
https://github.com/typesense/typesense-docsearch.js

# Commands cheat sheet
sudo systemctl stop typesense-server

sudo /usr/bin/typesense-server --data-dir=./typesense-data --api-key=xyz --log-dir=./typesense-logs --enable-cors --api-port=8108

# Tips
Typesense only works with the builded webpage of docussaurus
The scrapper config.json file must point to the port 80 or 443 of your ip address