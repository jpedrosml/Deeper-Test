# Technical Assessment - Deeper Systems
Task given by Deeper Systems to fill the Web Developer position. 

## Introduction
As instructed, the following application is a simple CRUD on a 2-page website.

The main page displays a table of users previously added to a NoSQL database, where in this case the pre-defined one to be used was MongoDB. The forementioned table shows on the screen the content below:
```
Username | Roles | Timezone | Is Active? | Last Updated At | Created At | Actions
```
These *actions* involve editing and deleting users; whenever a user is edited, the column 'Last Updated At' changes its value. Besides, it is also possible to add new users by clicking on the 'create' button.

As for the second page, you can reach it by clicking on someone's name on the table. This will lead you to the User Page, where basically the same information is displayed, but only that corresponding the clicked user. You can also edit and delete on this page.

## Instructions

This repository is structured as follows:
```
Deeper-Test
├── _pycache_
├── backend
│   ├── _pycache_
│   ├── config.py
│   ├── main.py
│   ├── parser.py
│   └── udata.json
└── frontend
    ├── .vscode
    ├── node_modules
    ├── public
    └── src
        ├── assets
        ├── components
        ├── routes
        ├── services
        ├── App.vue
        └── main.js
    ├── .gitignore
    ├── index
    ├── jsconfig
    ├── package
    ├── package-lock
    ├── README
    └── vite.config.js
```

For simplicity, I chose to keep the parser.py and udata.json inside the *backend* folder.

### Requisites

Make sure you have the following installed:

* NodeJS;
* Python 3;
* MongoDB;
* Vue.js;
* Flask

### Setting up the backend 

First and foremost, clone this repository using the following piece of code on your terminal: 

```git clone https://github.com/jpedrosml/Deeper-Test.git ```

In my case, I used VsCode plus the integrated terminal of Git Bash. 

After this, you're gonna set up the backend. Type (assuming you aren't yet in the root folder):

```
cd Deeper-Test
```
```
cd backend
```

Both commands below are indispensable, so make sure to install them before the next steps:
```
pip install pymongo
```
```
pip install flask-cors
```
While in the backend folder, and considering you have required dependencies ready to go, you simply run:

```
python main.py
```
This will run the backend application on http://127.0.0.1:5000.

### Setting up the frontend

Once you have started the backend, type:

``` 
cd ..
 ```
```
cd frontend
```

This will take you to the front end folder. Remember, Node.js **must** be in your system to run the pieces of code in this section. If Vue.js isn't already installed, type the following command in your terminal:

```
npm install -g @vue/cli (or yarn global add @vue/cli)
```

Other dependencies, if needed, shall be installed by:

```
npm install
```
Then you run the frontend application typing in your terminal:
```
npm run dev (or npm run serve)
```
Navigate to http://localhost:3000, where the frontend will be running.


That's pretty much it. The table might have a substantial delay to appear, as well as the user page.


