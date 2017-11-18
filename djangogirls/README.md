# DjangoGirls

**Description**

[My first website I've ever deployed to production!](https://rodellblog.herokuapp.com/). The website was produced by following the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) and the website is deployed via [Heroku](https://devcenter.heroku.com/articles/deploying-python).

## To-Do List

- [x] Create blog
- [x] Allow CRUD (Create, Read, Update, Delete) operations with blog
- [x] Allow only users to add, delete, or edit blogs
- [] Include user registration functionality. I currently have only admin as the user
- [] Create a "settings" directory to distinguish development settings from production settings. I currently use the same settings in development and production. One major consequence is having my DEBUG mode turned on.
- [] Create automated tests to practice healthy coding habits
- [] Include the name of the user who created the blog
- [] Include the name of the user who last edited the blog
- [] Include the name of the user who last edited the blog
- [] Include hashtag feature to tag blogs
- [] Implement search feature to search for blogs or hashtags

## Bug-Fixes

- [] Blogs don't distinguish between an edit and a publish
- [] Although anonymous users can't add, edit, or delete blogs they can still click those buttons on the front-end but will get an error upon trying to use them