# Hamster Store Listing Tool

## Prerequisites

* Installation of [fastlane][1] tools for android: [supply][2]
* Google Credential format (.json) as mention in [supply][2] page. Please PM Senspark for this file.
* Access permission to [google metadata sheet][3]. Please PM Senspark for the permission.

## Installation

1. Clone this repo
	
		git clone --recursive git@github.com:Senspark/hamster-store-listing.git 
2. Copy the Google Credential file as mention above step into the store listing folder above.
3. Folder structure will be:

		hamster-store-listing:
			|- gplay: 
				  |- run_populate.py
				  |- run_supply.py
			|- src:
				  |- gplay:
				       |- vi:
				           |- full_description.txt
				           |- short_description.txt
				           |- title.txt
			|- store-listing-toolkit:
			|- Google Play Android Developer-412b5ee99736.json

## Usage

### I. Editing description
1. **Auto-translated description**
	
	We 're currently using this [google sheet][3] to manipulate text metadata of this game. We have to update english data, the other languages will be updated with help of Google Translate service.
	
2. Manual-translated description

	In cases which you want to use your translation of text, such as Vietnamese:
	1. Make folder with Vietnamese language code `vi` in `src` folder.
	2. Create and edit the file correspond to the metadata field of the game as following:
		* *full_description.txt*: Full description of  the game.
		* *short_description.txt*: Short description of the game.
		* *title.txt*: Title of the game.
	


### II. Deploying changes
1. Using `Terminal`, change current directory to `src/gplay` folder.
2. Run `python run_populate.py` to populate metadata.
3. Run `python run_supply.py` to submit your metadata changes.

[1]: https://fastlane.tools/ "fastlane"
[2]: https://github.com/fastlane/fastlane/tree/master/supply#readme "supply"
[3]: https://docs.google.com/spreadsheets/d/1tPOZNM47rf3ERvVcMi2hyKHkt8fxTrsOhM9_2aCWQ6g/edit#gid=0 "google metadata sheet"