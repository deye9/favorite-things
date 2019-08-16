# BriteCore Software Engineer Hiring Test

## Setup

After cloning this repo, kindly run npm install so that all needed modules can be installed directly unto your system.

To run the tests associated with this project, kindly use the command below:

## API documentation

### Caveats

1. Relied heavy on Modals rather than having individual vue.js pages for each action on the page.
2. The metadata field should be a foreign key that points to a metadata table that has a KEY/VALUE structure setup. Which should have it's own vue component.
3. State management via Vuex was not implemented.

### API List

| Route                                     | Verb(s)  | Handler                                 | Middleware                                | Name                         |
| :---                                      | :---     | :---                                    | :---                                      | :---                         |
| `/admin/`                                 | GET      | django.contrib.admin.sites.index        | auth                                      | /creditCard                  |

### Database Diagram
