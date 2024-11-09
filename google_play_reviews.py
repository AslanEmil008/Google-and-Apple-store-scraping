from google_play_scraper import app
import csv

# result = app(
#     'com.commbank.netbank',
#     lang='en', # defaults to 'en'
#     country='au' # defaults to 'us'
# )

# from google_play_scraper import Sort, reviews


from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.commbank.netbank',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='au', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=10000,
    filter_score_with=None # defaults to None(means all score)
)

reviews_data = []

for review in result:
    reviews_data.append({
        'date of review': review['at'],  # Date of the review
        'stars/rating': review['score'],  # Rating
        'reviewer': review['userName'],  # Reviewer name
        'review text': review['content'],  # Review text
    })



# csv_file = 'App 1- Google reviews.csv'

# # Write the reviews to the CSV file
# with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)

#     # Write the headers (keys from one review dictionary)
#     if result:  # Check if result is not empty
#         headers = result[0].keys()  # Get the headers from the first review
#         writer.writerow(headers)

#         # Write the review data
#         for review in result:
#             writer.writerow(review.values())  # Write each review's values

# print(f"Data has been written to {csv_file}")

csv_file = 'App try- Google reviews.csv'

# Define the desired columns
desired_columns = ['date of review', 'stars/rating', 'reviewer', 'review text']

# Write the filtered reviews to the CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the headers (desired columns)
    writer.writerow(desired_columns)

    # Write the review data, filtering for desired columns only
    for review in result:
        filtered_review = {key: review[key] for key in desired_columns if key in review}  # Keep only desired columns
        writer.writerow(filtered_review.values())  # Write the filtered values

print(f"Data has been written to {csv_file}")



# print(result)


# {'reviewId': 'bb3bd86f-9e28-438b-8370-fc1f555ae7a3', 
#         'userName': 'Life is a Nightmare', 
#  'userImage': 'https://play-lh.googleusercontent.com/a-/ALV-UjUWKHYWQTjv-OjyUb4rIcpVad_NbTc-WEia95hH0cWjfAQZc2s', 
#         'content': '❤️❤️❤️', 
#         'score': 5, 
#  'thumbsUpCount': 0, 
#  'reviewCreatedVersion': None, 
#         'at': datetime.datetime(2020, 12, 30, 19, 45, 26), 
#  'replyContent': None, 
#  'repliedAt': None, 
#  'appVersion': None}