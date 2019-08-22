# BriteCore Software Engineer Hiring Test

## Setup

After cloning this repo, kindly run npm install so that all needed modules can be installed directly unto your system.

To run the tests associated with this project, kindly use the commands as listed in the sequence below:

1. `cd djangovue && docker-compose up -d`
2. `python manage.py runserver`
3. `python manage.py migrate`
4. `./manage.py loaddata category.json`

To get started frontend wise run the commands as listed in the sequence below in the root folder:

1. `npm install`
2. `npm run dev`

To run test scripts the command needed is

1. `python manage.py test`

To install all files in the requrements.txt files run the command below:

1. `pip install -r requirements.txt`

To view all available Django Routes run the command below

1. `./manage.py show_urls`

## API documentation

### Caveats

1. State management via Vuex was not implemented.
2. Did not implement sorting, filtering and pagination for all Record listing.
3. Global search functionality was not implemented
4. Swagger documentation was not implemented
5. Log filtering by date was not implemented.
6. Was unable to implement the ranking Stored Procedure / Query as i was nearly out of time.

### API List

| Route                                     |  Handler                                 |
| :---                                      | :---                                     |
| `/api/categories`                         | backend.views.CategoryView               |
| `/api/categories/<int:pk>`                | backend.views.CategoryView               |
| `/api/items`                              | backend.views.TrackerView                |
| `/api/items/<int:pk>`                     | backend.views.TrackerView                |
| `/api/logs`                               | backend.views.AuditLogView               |
| `/api/metadata`                           | backend.views.MetadataView               |
| `/api/metadata/<int:pk>`                  | backend.views.MetadataView               |

### Database Diagram
