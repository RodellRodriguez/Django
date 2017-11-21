# DjangoGirls

**Description**

[My first website I've ever deployed to production!](https://rodellblog.herokuapp.com/) The website was produced by following the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) and the website is deployed via [Heroku](https://devcenter.heroku.com/articles/deploying-python).

The tutorial provides instruction to produce a blog that allows the user to CRUD (Create Read Update Delete) blogs. The tutorial covers the bare basics so there is SO much room for improvement! (This is a good thing).

See Improvement List below for features I plan on implementing.

See my [Master Django Repo](https://github.com/RodellRodriguez/Django) for additional documentation of my journey with Django

**Dependencies**
* Python 3.5
* Django
* PostgreSQL
* Heroku
* Bootstrap
* CSS
* Gunicorn

## Improvement List

- [x] Include user registration/authentication functionality. I currently have only admin as the user
- [ ] Include user registration button
- [ ] Create a "settings" directory to distinguish development settings from production settings. I currently use the same settings in development and production. One major consequence is having my DEBUG mode turned on.
- [ ] Look into deploying the website via [Docker](https://www.docker.com/what-docker) to learn modern real-life automated deployment practices
- [ ] Create automated tests to practice healthy coding habits and spot more bugs 
- [ ] Use [Faker library for more blog data](https://github.com/joke2k/faker)
- [ ] Include the name of the user who created the blog
- [ ] Include the name of the user who last edited the blog
- [ ] Include hashtag feature to tag blogs
- [ ] Implement search bar feature to search for blogs or hashtags

## Bug-Fixes

- [ ] Blogs don't distinguish between an edit and a publish action
- [ ] Although anonymous users can't add, edit, or delete blogs they can still click those buttons on the front-end but will get an error upon trying to use them
