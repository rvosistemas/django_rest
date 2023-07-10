
# DJANGO REST APIS

Basic project with APIs developed with Django rest frameworks, using JWT authentication, expose endpoints API REST for user management to be able to connect with Frontend frameworks like Vue, React, Angular, etc. and using databases like Postgres and MongoDB.




## Documentation

[Documentation](https://linktodocumentation)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## API Reference

#### Admin DJango Rest

```http
  GET /admin/
```

| Parameter  | Type     | Description                           |
| :--------- | :------- | :------------------------------------ |
| `username` | `string` | **Required**. username of you account |
| `password` | `string` | **Required**. password of you account |


#### Register(create) User

```http
  POST /api/register/
```

| Parameter          | Type     | Description                                   |
| :----------------- | :------- | :-------------------------------------------- |
| `username`         | `string` | **Required**. username of you account         |
| `password`         | `string` | **Required**. password of you account         |
| `confirm_password` | `string` | **Required**. confirm password of you account |
| `first_name`       | `string` | First name of you user                        |
| `last_name`        | `string` | Last name of you user                         |
| `email`            | `string` | Email of you user                             |

#### Login User

```http
  POST /api/login/
```

| Parameter  | Type     | Description                           |
| :--------- | :------- | :------------------------------------ |
| `username` | `string` | **Required**. username of you account |
| `password` | `string` | **Required**. password of you account |

#### Logout User  - Authorization Bearer <jwt>

```http
  POST /api/logout/
```

No parameters

#### Get All Users - Authorization Bearer <jwt>

```http
  GET /api/users/
```

No parameters

#### Get User - Authorization Bearer <jwt>

```http
  GET /api/users/get/${id}/
```

| Parameter | Type  | Description                       |
| :-------- | :---- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Update User - Authorization Bearer <jwt>

```http
  PUT /api/users/update/${id}/
```

| Parameter | Type  | Description                        |
| :-------- | :---- | :--------------------------------- |
| `id`      | `int` | **Required**. Id of item to update |

#### Delete User - Authorization Bearer <jwt>

```http
  DELETE /api/users/delete/${id}/
```

| Parameter | Type  | Description                        |
| :-------- | :---- | :--------------------------------- |
| `id`      | `int` | **Required**. Id of item to delete |

#### Deactivate User - Authorization Bearer <jwt>

```http
  PATCH /api/users/deactivate/${id}/
```

| Parameter | Type  | Description                            |
| :-------- | :---- | :------------------------------------- |
| `id`      | `int` | **Required**. Id of item to deactivate |
## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Acknowledgements

Greats resources and tools for developing APIs.

 - [Django Rest Framework](https://www.django-rest-framework.org/)
 - [Django Rest Framework and JWT Authentication (Spanish)](https://coffeebytes.dev/django-rest-framework-y-jwt-para-autenticar-usuarios/)
 - [Postgresql](https://www.postgresql.org/docs/current/index.html)
 - [MongoDB](https://www.mongodb.com/docs/manual/)


## Authors

- [@rvosistemas](https://github.com/rvosistemas)

