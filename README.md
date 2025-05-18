# Google-and-Apple-store-scraping

## Introduction
This repository contains two codes that retrieve data from the Google Play Store and the Apple App Store, about reviews

# Getting started
# Usage
**1.** Clone the Repository

```bash
git clone https://github.com/AslanEmil008/Google-and-Apple-store-scraping.git
cd Google-and-Apple-store-scraping
```
**2.** Then install requirments.txt
```bash
pip install -r requirements.txt
```

# How to run
For running `app_store_reviews.py` you need find this line in code
```bash
bobbank = AppStore(country='uy', app_name='my-heritage', app_id = '1441537962')
```
Change the country, the app name you want, and the app ID which you can find in the URL of the app on the Apple Store <br>
After making necessary changes run the code
```bash
python3 app_store_reviews.py
```
**After running the code, you will get data about reviews like:**
- Date of Review 
- Review Text
- Stars / Rating
- isEdited
- Reviewer
- Title


For running `google_play_reviews.py` you need find this line in code:
```bash
result = reviews_all(
    'com.commbank.netbank',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='au', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=10000,
    filter_score_with=None # defaults to None(means all score)
)
```

Change the ID, which you can find in the URL of the app you want to get reviews for. <br>
Set the language to the language you want.<br>
Set the country to the country you want.<br>
And set the count—if you want more, increase it; if less, decrease it. <br>

After making changes run the code using this command:
```bash
python3 google_play_reviews.py
```

**After running the code, you will get data about reviews like:**
- Date of the review
- Rating
- Reviewer name
- Review text
  












