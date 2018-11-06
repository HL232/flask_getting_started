
## Mini-project
Create a flask web service that implements the following RESTful API specifications. Push this code to a repository called `flask_getting_started`. This code should be modular and reusable, but does not need testing for anything related to flask. Include reasonable tests for computations like the distance calculation functionality.  
* `GET /name` -- which returns the following JSON:
  ```
  {
    "name": "<your name here>"
  }
  ```
* `GET /hello/:name` -- this should return the following JSON:
  ```
  {
    "message": "Hello there, <:name parameter here>"
  }
  :eyes:Note that `:name` in the `GET` command above just a common way to
  specify that `name` is a variable, but it is actually specified as `<name>`
  in the URL.:eyes:
  ```
  :eyes:Note that `:name` in the `GET` command above just a common way to
  specify that `name` is a variable, but it is actually specified as `<name>`
  in the flask route specification decorator.:eyes:
* `POST /distance` with data input of two 2D cartesian points that looks like:
  ```
  {
    "a": [2, 4],
    "b": [5, 6]
  }
  ```
  this should return the cartesian distance between the points `a` and `b` in the following form:
  ```
  {
    "distance": <number here>,
    "a": [2, 4],
    "b": [5, 6]
  }
  ```