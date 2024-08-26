# Movie Database API

This project is a simple Movie Database API built using Django and Django REST Framework. It allows you to manage a database of movies, actors, directors, genres, and technicians. You can perform CRUD (Create, Read, Update, Delete) operations, filter movies by different criteria, order the results, and search by keywords.

## Features

- Add, retrieve, update, and delete movies.
- Filter movies by actor, director, and genre.
- Order movies by name, year of release, and user rating.
- Search for movies by name, director, actor, or genre.
- Delete an actor only if they are not associated with any movies.

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default, can be changed to any other database)
- Docker

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dhimanparas20/movie-database-api.git
cd movie-database-api
```

### 2. Directly run using Docker Compose

```bash
sudo docker compose up --build
```

### The server will start at http://127.0.0.1:80/.

## API Endpoints

### Movies

  - List all movies: GET /movies/
  - Create a new movie: POST /movies/
  - Retrieve a specific movie: GET /movies/{id}/
  - Update a movie: PUT /movies/{id}/
  - Partial update a movie: PATCH /movies/{id}/
  - Delete a movie: DELETE /movies/{id}/

### Actors
- List all actors: GET /actors/
- Create a new actor: POST /actors/
- Retrieve a specific actor: GET /actors/{id}/
- Update an actor: PUT /actors/{id}/
- Partial update an actor: PATCH /actors/{id}/
- Delete an actor: DELETE /actors/{id}/delete-if-not-associated/ (only if not associated with any movies)  

### Filtering and Ordering
- Filter by actor: GET /movies/?actors__name=ActorName
- Filter by director: GET /movies/?director__name=DirectorName
- Filter by genre: GET /movies/?genres__name=GenreName
- Order by name: GET /movies/?ordering=name
- Order by year of release: GET /movies/?ordering=year_of_release
- Order by user rating: GET /movies/?ordering=-user_rating (descending)

## Admin Panel
- Access the Django admin panel to manage movies, actors, directors, genres, and technicians:

- URL: `http://127.0.0.1:80/admin/`
Use the superuser credentials created earlier to log in.

### License
 - This project is licensed under the [MIT License](https://opensource.org/license/mit). See the [LICENSE](LICENSE) file for details.

### Contact
- For any questions or issues, please open an issue on the GitHub repository.

