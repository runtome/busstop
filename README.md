# [Busstop Project](https://www.google.com)

This project is senior project of  **Walailak University** create by student of `Computer Engineering`  .  

- 👉 [Walailak University](https://www.wu.ac.th/en) - University page.
- 👉 [Bus stop Project](https://) - Project page.
- 🚀 [Development team ](https://) Can contact via `Email`

<br />

> 🚀 Built with Flask [Link ](https://flask.palletsprojects.com/en/2.2.x/)

<br />

![Flask logo](https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png)

<br /> 

- ✅ `Under development`
- ✅ `Database`: `MongoDB`,[MongoDB Link](https://www.mongodb.com/)
- ✅ `Database`: `SQLite`, MySql --> May be change in future 
  - Subcomment  `Comment`
- ✅ `Development Tools`: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- ✅ Session-Based  during consider 
- 🚀 `Deployment` 
  - `github` flow to `pythonanywhere.com`
  - [Pythonanywhere](https://www.pythonanywhere.com/)

<br />

![Pythonanywhere logo](https://www.pythonanywhere.com/static/anywhere/images/PA-logo.svg)

<br /> 

## ✨ How to use it

> Download the code 

```bash
$ git clone https://github.com/runtome/busstop.git
$ cd busstop
```

<br />

### 👉 Set Up for `Windows` 

> Install modules via `CONDA`  

```bash
$ conda create -n busstop python=3.9
$ conda activate busstop
$ pip3 install -r requirements.txt
```

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```


> Start the app

```bash
$ flask app
```

At this point, the app runs at `http://127.0.0.1:5000/`. 


### 👉 Note 

Impotance : 

- Start the app via `flask server`
- Access the `Main` page by:
  - `http://127.0.0.1:5000/register`
- Access the `Bus situation ` page 
  - `http://127.0.0.1:5000/situation`

<br />

## ✨ Code-base structure

The project is code stracture ad following.

```bash
< PROJECT ROOT >
   |    
   |-- static/
   |     |-- css                # css file
   |     |-- images             #Save all image 
   |
   |-- templates/                 # Templates used to render pages
   |     |-- base.html            # Base html
   |     |-- index.html            # First page
   |     |-- 404-page.html         # 404 page
   |     |-- *.html                # All other pages in futurte
   |
   |-- app.py  #Main application
   |        
   |-- config.json                # config conncection data  your setting data 
   |
   |-- requirements.txt              # App Dependencies
   |
   |
   |-- ************************************************************************
```

<br />

## [About Development team ](https:)

> Name 
> Name 
