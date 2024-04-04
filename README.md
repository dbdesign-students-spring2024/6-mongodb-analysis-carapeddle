# AirBnB MongoDB Analysis

## Data set details:
### Origin of the Data Set 
The data included in this analysis is sourced from Inside Airbnb, where regional quarterly data for the last year can be downloaded. The data includes informantion about Airbnb listings throughout Geneva, Switzerland, including about the host, the neighborhood, ratings, number of beds and bathrooms, etc. The general website includes information about listings throughout the world, organized primarily by city.

[[LINK TO GENERAL WEBSITE]](https://insideairbnb.com/get-the-data/) 

[[LINK TO GENEVA PAGE]](https://insideairbnb.com/geneva) 

[[LINK TO DOWNLOAD DATA]](https://data.insideairbnb.com/switzerland/geneva/geneva/2023-12-27/data/listings.csv.gz)


### Format of Original Data File 
The original data file is formatted as a CSV file.

### Raw Data from Original Data File 
(first 20 rows is enough - feel free to clip the text in fields to prevent line-wrapping). 

| id    | listing_url |  scrape_id    | last_scraped |  source    | name | description    | neighborhood_overview |  picture_url    | host_id |  host_url    | host_name |  ... | 
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- |
| 42515 | https://www.airbnb.com/rooms/42515 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.73 · 1 bedroom · 1 bed · 1.5 shared baths |   |  | https://a0.muscache.com/pictures/10640277/ff1da5fd_original.jpg | 185647 |  https://www.airbnb.com/users/show/18564 | "Geneva, Switzerland" | ... |
| 107438 | https://www.airbnb.com/rooms/107438 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.87 · 1 bedroom · 1 bed · 1.5 shared baths |   |  | https://a0.muscache.com/pictures/93bb00cc-03bb-47c3-905f-a7ae7fa4e328.jpg | 556499 |  https://www.airbnb.com/users/show/556499 | F. M. | ... |
| 203997 | https://www.airbnb.com/rooms/203997 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.90 · 1 bedroom · 1 bath |   | "This is the most sought after area in Geneva: the lake is practically on your doorstep | https://a0.muscache.com/pictures/14163740/9392557b_original.jpg | 1001280 |  https://www.airbnb.com/users/show/1001280 | Mike | ... |
| 276025 | https://www.airbnb.com/rooms/276025 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Versoix · ★4.62 · 1 bedroom · 4 beds · 1 bath |   |  | https://a0.muscache.com/pictures/4156456/d3aed209_original.jpg | 1442438 |  https://www.airbnb.com/users/show/1442438 | Gaby | ... |
| 338682 | https://www.airbnb.com/rooms/338682 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.81 · 1 bedroom · 1 bed · 1.5 baths |   | "This is the favourite area for expats in Geneva. It's near the lake | https://a0.muscache.com/pictures/14164129/db92c79b_original.jpg | 1001280 |  https://www.airbnb.com/users/show/1001280 | Mike | ... |
| 399388 | https://www.airbnb.com/rooms/399388 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Carouge · ★4.83 · 1 bedroom · 1 bed · 1 shared bath |   |  | https://a0.muscache.com/pictures/82542974/c8568e72_original.jpg | 1994454 |  https://www.airbnb.com/users/show/1994454 | Oscar | ... |
| 411058 | https://www.airbnb.com/rooms/411058 |  20231227030725 | 2023-12-27 | city scrape | Loft in Geneva · ★4.77 · 1 bedroom · 1 bed · 1.5 shared baths |   | "The Pâquis quarter is one of Geneva's most colourful | https://a0.muscache.com/pictures/airflow/Hosting-411058/original/5e0aaac9-8a72-4f6b-9376-42d2413d2756.jpg | 1706035 |  https://www.airbnb.com/users/show/1706035 | Julik | ... |
| 419631 | https://www.airbnb.com/rooms/419631 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.94 · 1 bedroom · 1 bed · 1.5 baths |   | Quiet yet very central <br /><br />N.B.| https://a0.muscache.com/pictures/e591abb4-fc83-458b-b29a-edc859346567.jpg | 2086993 |  https://www.airbnb.com/users/show/2086993 | Mark | ... |
| 476344 | https://www.airbnb.com/rooms/476344 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.76 · 3 bedrooms · 4 beds · 2.5 baths |   | Calm. Shops nearby. Very nice park for children. | https://a0.muscache.com/pictures/6239604/a651ff2d_original.jpg | 2361206 |  https://www.airbnb.com/users/show/2361206 | Jean | ... |
| 494701 | https://www.airbnb.com/rooms/494701 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Geneva · ★4.10 · 4 bedrooms · 4 beds · 1.5 baths |   |  | https://a0.muscache.com/pictures/2d968b6d-4e9b-4346-a21e-197cf6545365.jpg | 2388229 |  https://www.airbnb.com/users/show/2388229 | Alberto | ... |
| 610738 | https://www.airbnb.com/rooms/610738 |  20231227030725 | 2023-12-27 | city scrape | Rental unit in Genève · ★4.38 · 2 bedrooms · 2 beds · 1 bath |   |  | https://a0.muscache.com/pictures/83847321/28ad6bdb_original.jpg | 2388229 |  https://www.airbnb.com/users/show/2388229 | Alberto | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |
| -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | -------- | ------- |  -------- | ------- | ... |


### Problems in Data and Scrubbing Tasks 
#### Many characters in the file run the risk of importing incorrectly, so they must be addressed so that importing data does not pose a problem.
- Replace è with e

Special characters such as **è** may pose a problem when importing and assessing data, so they were removed and replaced with **e** for consistency.
```
if 'è' in value:
    newvar = value.replace('è', 'e')
    data[count][key] = newvar
```
- Replace ë with e
```
if 'ë' in value:
    newvar = value.replace('ë', 'e')
    data[count][key] = newvar
```
- Replace · with /
```
if '·' in value:
    newvar = value.replace('·', '/')
    data[count][key] = newvar
```
- Replace ★ with *
```
if '★' in value:
    newvar = value.replace('★', '*')
    data[count][key] = newvar
```

#### Some data included line breaks and tabs, which were removed for consistency.
- \<br />
- \t
- \n
```
for key, value in line.items():   
    data[count][key] = value.replace('\n', ' ').replace('\t', ' ').replace('<br />', '').replace('\r', '').strip()
```

#### The values denoting a lack of data were inconsistent, some using N/A, others using [], while others were left blank. This issue was addressed for consistency by replacing each for a blank value. To account for any other characters that may cause problems when importing data, these values were replaced with a blank value.
```
for key, value in line.items():
    if value.isascii() == False or 'N/A' in value or '[]' in value:
        data[count][key] = ''
```
 
## Analysis:
### Import the data:
```
mongoimport --headerline --type=csv --db=cep454 --collection=listings_clean --host=class-mongodb.cims.nyu.edu --file=listings_clean.csv --username=cep454 --password=password
```

### 1. Two Documents from `listings` Collection in Any Order
#### Description of Query
This query pulls two documents from the listings_clean collection, without a specific order. The query will return two documents with each column heading and relevant values. There is no criteria or projection so the query will return all data included in the documents.
#### Code
```
db.listings_clean.find().limit(2)
```
#### Results
>[
  {
    _id: ObjectId('660cad19b6515eb2057558e2'),
    id: 42515,
    listing_url: 'https://www.airbnb.com/rooms/42515',
    scrape_id: 20231200000000,
    last_scraped: '12/27/23',
    source: 'city scrape',
    name: 'Rental unit in Geneva / *4.73 / 1 bedroom / 1 bed / 1.5 shared baths',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/10640277/ff1da5fd_original.jpg',
    host_id: 185647,
    host_url: 'https://www.airbnb.com/users/show/185647',
    host_name: 'Noelle',
    host_since: '7/30/10',
    host_location: 'Geneva, Switzerland',
    host_about: 'Hi, I am a Management consultant professional, working with multinational 
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '40%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/185647/profile_pic/1316167292/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/185647/profile_pic/1316167292/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Commune de Geneve',
    neighbourhood_group_cleansed: '',
    latitude: 46.20198,
    longitude: 6.15672,
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1.5 shared baths',
    bedrooms: '',
    beds: 1,
    amenities: '',
    price: '$89.00',
    minimum_nights: 3,
    maximum_nights: 1125,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 3,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 28,
    availability_60: 58,
    availability_90: 88,
    availability_365: 363,
    calendar_last_scraped: '12/27/23',
    number_of_reviews: 73,
    number_of_reviews_ltm: 6,
    number_of_reviews_l30d: 0,
    first_review: '9/24/11',
    last_review: '11/3/23',
    review_scores_rating: 4.73,
    review_scores_accuracy: 4.72,
    review_scores_cleanliness: 4.77,
    review_scores_checkin: 4.84,
    review_scores_communication: 4.83,
    review_scores_location: 4.84,
    review_scores_value: 4.52,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.49
  >},
  <br>
  <br>
  >{
    _id: ObjectId('660cad19b6515eb2057558e3'),
    id: 107438,
    listing_url: 'https://www.airbnb.com/rooms/107438',
    scrape_id: 20231200000000,
    last_scraped: '12/27/23',
    source: 'city scrape',
    name: 'Rental unit in Geneva / *4.87 / 1 bedroom / 1 bed / 1.5 shared baths',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/93bb00cc-03bb-47c3-905f-a7ae7fa4e328.jpg',
    host_id: 556499,
    host_url: 'https://www.airbnb.com/users/show/556499',
    host_name: 'F. M.',
    host_since: '5/4/11',
    host_location: 'Geneva, Switzerland',
    host_about: 'It is a cosy furnished room with wifi connexion and cable TV in an amazing modern flat of 115m2 near to the centre of Geneva',
    host_response_time: 'a few days or more',
    host_response_rate: '0%',
    host_acceptance_rate: '0%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/556499/profile_pic/1304521913/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/556499/profile_pic/1304521913/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Passy',
    host_listings_count: 2,
    host_total_listings_count: 5,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Commune de Geneve',
    neighbourhood_group_cleansed: '',
    latitude: 46.18905,
    longitude: 6.16154,
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1.5 shared baths',
    bedrooms: '',
    beds: 1,
    amenities: '',
    price: '$60.00',
    minimum_nights: 5,
    maximum_nights: 1125,
    minimum_minimum_nights: 5,
    maximum_minimum_nights: 5,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 5,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 27,
    availability_60: 57,
    availability_90: 87,
    availability_365: 362,
    calendar_last_scraped: '12/27/23',
    number_of_reviews: 23,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '5/15/11',
    last_review: '11/30/19',
    review_scores_rating: 4.87,
    review_scores_accuracy: 4.9,
    review_scores_cleanliness: 4.76,
    review_scores_checkin: 4.76,
    review_scores_communication: 4.76,
    review_scores_location: 4.57,
    review_scores_value: 4.57,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.15
  }
>]

#### Insights Not Obvious in Raw Data
In the raw data, the relationships between the headings and the values are difficult to connect. With the data formatted so the heading points directly to the value, it is much easier to understand what each value represents and to compare these values with those in other documents. For example, it is easier to compare the price of these two documents. Noelle's listing with id# 42515 is $89.00 per night while F. M.'s listing with id# 107438 is $60.00 per night. Noelle's listing has a minimum night requirement of 3 nights, while F. M.'s listing has a minimum night requirement of 5 nights.

### 2. Show 10 documents in Any Order, using `pretty()` Function

#### Description of Query
The default query without the pretty() function generally returns the data in a dense format, while the pretty() function returns data in a format that can be read easily. The query will return ten documents with each column heading and relevant values. Because there is no criteria or projection, the query will return all data included in the documents in a formatted manner.
#### Code
```
db.listings_clean.find().limit(10).pretty()
```
#### Results

##### Three Lines with Formatting
>[
<br>
    {
        <br>
        _id: ObjectId('660cad19b6515eb2057558e2'),
        <br>
        id: 42515,
        <br>
        listing_url: 'https://www.airbnb.com/rooms/42515'
        <br>
    }
    <br>
]

##### Without Added Line Breaks
>[
  {
    _id: ObjectId('660cad19b6515eb2057558e2'),
    id: 42515,
    listing_url: 'https://www.airbnb.com/rooms/42515',
    scrape_id: 20231200000000,
    last_scraped: '12/27/23',
    source: 'city scrape',
    name: 'Rental unit in Geneva / *4.73 / 1 bedroom / 1 bed / 1.5 shared baths',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/10640277/ff1da5fd_original.jpg',
    host_id: 185647,
    host_url: 'https://www.airbnb.com/users/show/185647',
    host_name: 'Noelle',
    host_since: '7/30/10',
    host_location: 'Geneva, Switzerland',
    host_about: 'Hi, I am a Management consultant professional, working with multinational and ',
    host_response_rate: '100%',
    host_acceptance_rate: '40%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/185647/profile_pic/1316167292/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/185647/profile_pic/1316167292/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Commune de Geneve',
    neighbourhood_group_cleansed: '',
    latitude: 46.20198,
    longitude: 6.15672,
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1.5 shared baths',
    bedrooms: '',
    beds: 1,
    amenities: '',
    price: '$89.00',
    minimum_nights: 3,
    maximum_nights: 1125,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 3,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 28,
    availability_60: 58,
    availability_90: 88,
    availability_365: 363,
    calendar_last_scraped: '12/27/23',
    number_of_reviews: 73,
    number_of_reviews_ltm: 6,
    number_of_reviews_l30d: 0,
    first_review: '9/24/11',
    last_review: '11/3/23',
    review_scores_rating: 4.73,
    review_scores_accuracy: 4.72,
    review_scores_cleanliness: 4.77,
    review_scores_checkin: 4.84,
    review_scores_communication: 4.83,
    review_scores_location: 4.84,
    review_scores_value: 4.52,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.49
  },
  <br>
  <br>
  {
    _id: ObjectId('660cad19b6515eb2057558e3'),
    id: 107438,
    listing_url: 'https://www.airbnb.com/rooms/107438',
    scrape_id: 20231200000000,
    last_scraped: '12/27/23',
    source: 'city scrape',
    name: 'Rental unit in Geneva / *4.87 / 1 bedroom / 1 bed / 1.5 shared baths',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/93bb00cc-03bb-47c3-905f-a7ae7fa4e328.jpg',
    host_id: 556499,
    host_url: 'https://www.airbnb.com/users/show/556499',
    host_name: 'F. M.',
    host_since: '5/4/11',
    host_location: 'Geneva, Switzerland',
    host_about: 'It is a cosy furnished room with wifi connexion and cable TV in an amazing ',
    host_response_time: 'a few days or more',
    host_response_rate: '0%',
    host_acceptance_rate: '0%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/556499/profile_pic/1304521913/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/556499/profile_pic/1304521913/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Passy',
    host_listings_count: 2,
    host_total_listings_count: 5,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Commune de Geneve',
    neighbourhood_group_cleansed: '',
    latitude: 46.18905,
    longitude: 6.16154,
    property_type: 'Private room in rental unit',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1.5 shared baths',
    bedrooms: '',
    beds: 1,
    amenities: '',
    price: '$60.00',
    minimum_nights: 5,
    maximum_nights: 1125,
    minimum_minimum_nights: 5,
    maximum_minimum_nights: 5,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 5,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 27,
    availability_60: 57,
    availability_90: 87,
    availability_365: 362,
    calendar_last_scraped: '12/27/23',
    number_of_reviews: 23,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '5/15/11',
    last_review: '11/30/19',
    review_scores_rating: 4.87,
    review_scores_accuracy: 4.9,
    review_scores_cleanliness: 4.76,
    review_scores_checkin: 4.76,
    review_scores_communication: 4.76,
    review_scores_location: 4.57,
    review_scores_value: 4.57,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.15
  }
>]

#### Insights Not Obvious in Raw Data
Because of the organized format of the data, it is easy to understand the relationships between the column headings and the values they point to. The format of the data allows the viewer to recognize that F. M. and Noelle's listings do not have data under the neighbourhood heading. Furthermore, it is easy to visualize the listings' ratings for various factors. For example, Julik's listing with id# 411058 was given a 4.85 for review_scores_cleanliness, a 4.94 for review_scores_checkin, a 4.96 for review_scores_communication, and a 4.88 for review_scores_location.

### 3. Choose Two Hosts `host_id` Who Are Superhosts `host_is_superhost` and All Listings Offered by Both
   - Show `name`, `price`, `neighbourhood`, `host_name`, `host_is_superhost` 
#### Description of Query
An initial query requests the host_id of 10 listings where the host is a superhost. This query is used to choose two distinct host_id values who are also superhosts. The query returned 10 results and two distinct host_id values were chosen. The following query had one criteria: that the host_id was equal to 1001280 or 2361206. The projection limited the fields that would be returned to name, price, neighbourhood, host_name, and host_is_superhost. The query chooses two hosts that are superhosts and lists all listings offered by both.
#### Code
```
db.listings_clean.find({host_is_superhost: "t"}, {_id: 0, host_id:1}).limit(10)

db.listings_clean.find({$or: [{host_id: 1001280}, {host_id: 2361206},],}, {_id:0, name:1, price:1, neighbourhood:1, host_name:1, host_is_superhost:1})
```
#### Results 

>[
  {
    name: 'Rental unit in Geneva / *4.90 / 1 bedroom / 1 bath',
    <br>
    host_name: 'Mike',
    <br>
    host_is_superhost: 't',
    <br>
    neighbourhood: 'Geneva, Switzerland',
    <br>
    price: '$165.00'
  },
  <br>
  <br>
  {
    name: 'Rental unit in Geneva / *4.81 / 1 bedroom / 1 bed / 1.5 baths',
    <br>
    host_name: 'Mike',
    <br>
    host_is_superhost: 't',
    <br>
    neighbourhood: 'Geneva, Switzerland',
    <br>
    price: '$157.00'
  },
  <br>
  <br>
  {
    name: 'Rental unit in Geneva / *4.76 / 3 bedrooms / 4 beds / 2.5 baths',
    <br>
    host_name: 'Jean',
    <br>
    host_is_superhost: 't',
    <br>
    neighbourhood: 'Geneva, Canton of Geneva, Switzerland',
    <br>
    price: '$269.00'
  }
>]

#### Insights Not Obvious in Raw Data
The query returned information that would not be obvious in the raw data. Specifically, the query returned only the relevant information that would be difficult to search for using the raw data. It becomes apparent that the superhost, Mike, has two listings that are both cheaper than the superhost Jean's listing. The query also makes it easy to determine the size of the listing in relation to the price without having to sort through an immense amount of data. Jean's listing has 3 bedrooms and 2.5 baths while Mike's listings have 1 bedroom each and 1/1.5 baths.

### 4. Find Unique `host_name` Values

#### Description of Query
The query lists the names of all individuals who have listings. The query lists the distinct names, meaning that the names are not repeated even when one individual has multiple listings. One criteria describes that the host_name field cannot be blank. Therefore, the distinct host names will be returned besides those listings that do not contain data about the host name.
  
#### Code
```
db.listings_clean.distinct("host_name", { "host_name": { $ne: "" } })
```
#### Results

>[
  'A',
  <br>
  'A.',
  <br>
  'Aaron'
>]

#### Insights Not Obvious in Raw Data
Without the criteria that prohibits host_name from being equal to a blank space, it becomes apparent that at least one listing does not have information about the host name. The query also demonstrates that at least two people use the initial "A" as their host name, where one includes a period and another does not. 

### 5. Find Places With More Than 2 `beds` in Neighborhood `neighborhood` or `neighbourhood_group_cleansed` Ordered by `review_scores_rating` Descending
   - only show `name`, `beds`, `review_scores_rating`, `price`

#### Description of Query
This query returns all listings within a single neighborhood that has more than 2 beds. The data is returned in descending order by review_scores_rating. The criteria requires that the neighborhood is equal to "Geneve, Switzerland" and the number of beds is greater than 2. The projection limits the fields returned to name, beds, review_scores_rating, and price. 
#### Code
```
db.listings_clean.find({neighbourhood: "Geneve, Switzerland", beds:{$gt:2}}, {_id:0, name:1, beds:1, review_scores_rating:1, price:1}).sort({"review_scores_rating":-1})
```
#### Results

>[
  {
    name: 'Rental unit in Geneve / 2 bedrooms / 3 beds / 2 baths',
    <br>
    beds: 3,
    <br>
    price: '$135.00',
    <br>
    review_scores_rating: ''
  },
  <br>
  <br>
  {
    name: 'Rental unit in Geneve / 3 bedrooms / 4 beds / 2 baths',
    <br>
    beds: 4,
    <br>
    price: '$130.00',
    <br>
    review_scores_rating: ''
  },
  <br>
  <br>
  {
    name: 'Condo in Geneve / 3 bedrooms / 3 beds / 2.5 baths',
    <br>
    beds: 3,
    <br>
    price: '$290.00',
    <br>
    review_scores_rating: ''
  }
>]

#### Insights Not Obvious in Raw Data
The results indicate that multiple listings are not rated. The beginning of the list of returned data provides information on listings that have not been rated or that have no information on ratings. The following listings are those with 5 stars. This information allows the viewer to compare prices for those listings that match their needs of more than 2 beds. The price can be compared among listings with the same ratings or with listings with other ratings. The viewer can see that one 3-bed listing with a rating of 5 goes for $100 while another 3-bed listing with a rating of 5 goes for $425. The viewer can compare these prices to a 3-bed listing with 3.5 stars, going for $302.

### 6. Number of Listings Per Host

#### Description of Query
This query counts the number of listings per host by grouping together listings with the same value in the host_id field and then finding the sum.
  
#### Code
```
db.listings_clean.aggregate({$group: {_id: "$host_id", count: {$sum:1}}})
```
#### Results

>[
  { _id: 552225573, count: 1 },
  <br>
  { _id: 183199633, count: 2 },
  <br>
  { _id: 347734429, count: 1 }
>]


#### Insights Not Obvious in Raw Data
The results indicate that many hosts have only 1 listing. Discovering this information would be especially difficult in the raw data because one would be required to search for the host_id value in each document. With the above query, the viewer can find the specific host_id value and view the exact number of listings belonging to that host_id value. It is easy to find, for example, that when host_id is equal to 544285538, the count of listings is 5 whereas when the host_id is equal to 158866785, the count of listings is 1. 

### 7. Average `review_scores_rating` Per Neighborhood, Only Show `4` or Above, Sorted in Descending Order of Rating 

#### Description of Query
This query groups the listings by neighborhood and finds the average review_scores_rating of each neighborhood. It returns only those neighborhoods with an average rating above or equal to 4, and sorts the information in descending order of the average rating. 
#### Code
```
db.listings_clean.aggregate([{$group:{_id: "$neighbourhood", avgRating: {$avg: "$review_scores_rating"}}}, {$match: {avgRating: {$gte:4}}}, {$sort: {avgRating:-1}}])
```
#### Results

> [
    { _id: 'Meinier, Geneve, Switzerland', avgRating: 5 },
    <br>
    { _id: 'Onex, GE, Switzerland', avgRating: 5 },
    <br>
    { _id: 'Laconnex, Geneve, Switzerland', avgRating: 5 }
>]

#### Insights Not Obvious in Raw Data
This query allows viewers to search specifically for neighborhoods with a certain average rating that suits their needs. Rather than being forced to search through the raw data to find information on each listing in each neighborhood, the average rating of listings in each neighborhood is set out in an organized fashion. Several neighborhoods have an average rating of 5, such as 'Meinier, Geneve, Switzerland', 'Onex, GE, Switzerland', and 'Genthod, Geneva, Switzerland'. The organized nature of the returned data makes it easy to observe that the neighborhood with the highest rating under 5 stars is 'Collonge-Bellerive, Geneve, Switzerland'.