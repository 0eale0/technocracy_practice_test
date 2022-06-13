<h1> Technocracy_practice_test  </h1>

[Trello](https://trello.com/b/8ad9cpfV/technocracypracticetest)

## USE :hatching_chick:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) 
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)



## Description :game_die:
That project is example of simple backend for notes. In this project realised simple CRUD for models with permissions. For example user can work and see only own notes, but admin every note. User can see every category, but edit, delete, update only own. There is used JWT for auth users. User can create account by username and email. Admin have full CRUD for any model by DRF.

## DB diagram :scroll:
<img src="https://github.com/0eale0/files_for_github/blob/main/pictures/diagram_technocracy.png?raw=true" alt="drawing" width="700"/>

## Urls :earth_americas:

* **/api/logic/note/** - viewset for note with full CRUD, have permissions, writed in description
* **/api/logic/category/** - viewset for category with full CRUD, have permissions, writed in description
* **/api/accounts/register/** - registration
* **/api/accounts/users/** - CRUD for user account, can access only admin
* **/api/token/** - get jwt token
* **/api/token/refresh** - refresh jwt

## Tests :space_invader:

For this project was frited a few tests using pytest and django modelfactory. For tests created a fake database with fake objects agter testing database is deleting. **Percentage of coverage 90%**


## Installation :see_no_evil:

[Install `docker` and `docker-compose`](https://docs.docker.com/engine/install/).

### Configuration :wrench:

Create `.env.dev` like `.env.example`. Set the settings.

### Start up :rocket:

```bash
docker compose up
```
