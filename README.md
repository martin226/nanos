<div align="center">
    <img alt="Logo" src="docs/logo.png" width="100" />
</div>
<h1 align="center">
    nanos
</h1>
<p align="center">
    nanos is a minimalistic link shortener that lets you easily reduce your long links in one click and view analytics for your shortened URLs. Nano it with nanos! 
</p>

> _tldr;_ nanos shortens any URL you want, preserving SEO value and providing you with detailed analytics so that you can track your link clicks.

# How it Works

> Nuxt Frontend → Django Backend API → PostgreSQL DB → Nuxt Frontend

## Frontend

- NuxtJS/Vue as JS framework
- Axios to interact with the backend API
- http-proxy-middleware to proxy backend requests
- Vuex for state management
- WindiCSS for styling

## Backend API

- Django as server
- Django Rest Framework (DRF) for building REST API
- PostgreSQL as database for storing shortened links
- Uses ipapi for geolocation information
- Parses user agent for referrer and device information

# Distinctiveness and Complexity

I believe that this project satisfies the distinctiveness and complexity requirements as specified in the assignment details.

It is evident that this application is unique from the other CS50W projects, as there is no other project similar to a URL shortener. Additionally, it uses NuxtJS and Vue on the frontend, setting it apart from the other assignments.

As per the criteria, the website is built on the Django framework which is used for managing the API. It is responsible for the backend routes, database models, and business logic of the application.

Likewise, JavaScript—specifically the NuxtJS framework—is used on the frontend. It is used mainly for client-side page routing, interaction with the API, and dynamic data management.

Furthermore, using the WindiCSS CSS framework, the website is designed to be completely mobile responsive. All components are able to dynamically resize and reorder as necessary based on the viewport width.

To emulate a production environment, a design decision was made to use PostgreSQL instead of the default Django SQLite. This provides advantages including allowing concurrency and extensibility.

Finally, to enhance development, various tooling is used in this project. Git hooks are created and installed using Husky, which allows for commit message and staged file linting. Github Actions are used for autonomous continuous integration. It is currently used for linting, but it can be expanded to automated testing.

# Requirements

- NodeJS
- Python
- PostgreSQL
- [Poetry](https://python-poetry.org/) (optional but recommended for dependency management)

# Folder Structure

This project is structured as follows:

- **backend**: Has the Django project, _structured the same way as the other CS50W projects_. Contains the `api` app, which is called by the frontend for creating shortened URLs and viewing analytics.
- **frontend**: Has the NuxtJS project. Contains all the pages that users browse, such as the home page and analytics page. It interacts with the Django API to provide functionality.
- **.github**: Contains Github configuration files and workflows
- **docs**: Documentation assets

# File Contents

## Backend

- `./backend`
  - `manage.py`: Used as a command-line utility (CLI) that allows one to interact with the Django project with various commands
  - `pyproject.toml`: Contains metadata and dependencies for the project
  - `poetry.lock`: Lockfile that stores current versions of dependencies in a projec
  - `requirements.txt`: List of project dependencies
- `./backend/backend`
  - `.env`: Contains project secrets (environment variables).
  - `__init__.py`: Exists solely to mark the directory as a Python package
  - `settings.py`: Contains the Django project configuration, such as database settings, middleware, and apps
  - `wsgi.py`: Contains WSGI server configuration
  - `asgi.py`: Contains ASGI server configuration
  - `urls.py`: Contains the URL routes in the project
- `./backend/api`
  - `__init__.py`: Exists solely to mark the directory as a Python package
  - `apps.py`: Contains the Django application configuration
  - `admin.py`: Registers models into the Django admin panel
  - `urls.py`: Contains the URL routes in the app. This project has routes for:
    - Creating short URL
    - Viewing analytics for URL
    - Redirecting short URLs to their original URLs
    - Admin panel
    - Redirecting the root path ("/") to "/app"
  - `models.py`: Contains the database models for this app. There are 2 database models used in the application.
    1. URLShorten: Keeps track of each shortened URL by holding the ID, long URL, analytics ID, and other information.
    2. View: Keeps track of each URL view/click. It is linked to the URLShorten model via ForeignKey.
  - `views.py`: Contains the controller files, which handle the project's business logic. API views are built with Django Rest Framework. This project has views for
    - Creating short URL
    - Viewing analytics for URL
    - Redirecting short URLs to their original URLs
  - `util.py`: Contains utility functions for use in views. This project has utility functions for:
    - Generating short/analytics ID
    - Resolving country names
    - Getting client IP address

## Frontend

- `./frontend`:
  - `package.json`: Contains metadata, dependencies, and scripts for the project
  - `nuxt.config.js`: Config file for NuxtJS, the JS framework used in this project
  - `windi.config.ts`: Config file for WindiCSS, the CSS framework used in this project
  - `tsconfig.json`: Config file for Typescript
  - `eslintrc.js`, `.prettierrc`, `.prettierignore`, `commitlint.config.js`, `stylelint.config.js`: Config files for linting and formatting
  - `yarn.lock`: Lockfile that stores current versions of dependencies in project
- `./frontend/.husky`:
  - `commit-msg`: Husky Git hook for linting commit messages to adhere to conventional commit standards
  - `pre-commit`: Husky Git hook for linting staged files
  - `common.sh`: Contains workaround to allow the use of Git hooks when using Yarn on Windows with Git Bash
- `./frontend/components`:
  - `./Form/Create.vue`: Component with form for creating shortened URLs
  - `./Widget/History.vue`: Component with reverse-chronological list of link shortening history
  - `./Widget/Views.vue`: Component that displays list of link views
- `./frontend/layouts`:
  - `.default.vue`: Contains the default page layout
- `./frontend/pages`:
  - `./analytics/_id.vue`: Contains the dynamic analytics page. Interacts with the API to display a variety of stats for specified shortened URL
  - `index.vue`: Contains the home page. Has the link creation form and the link shortening history list
- `./frontend/plugins`:
  - `vuex-persist.ts`: Loads the vuex-persist plugin to allow history to persist through refreshes
- `./frontend/static`:
  - `favicon.ico`: Site favicon
- `./frontend/store`:
  - `index.ts`: Project Vuex store. Holds the application state, storing the shortening history. Has mutations for adding to and clearing shortening history, as well as actions for creating links and getting analytics

# Project Setup

## Frontend

```bash
cd frontend
yarn install
yarn dev
```

## Backend API

Rename `/backend/backend/.env.example` to `/backend/backend/.env` and edit any required configuration first.

```bash
cd backend
poetry install # or pip install -r requirements.txt
poetry run python manage.py runserver # or python manage.py runserver
```
