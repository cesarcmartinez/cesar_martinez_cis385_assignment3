# Assignment 3

## REST API
This assignment submission includes a Python file that creates the REST API using Flask. The API will keep track of simple notes. The PDF file provides the screenshots of the API calls. 

<br>

### Instructions
- Each note will have an ID and twp properties: title and body.
- The user is able to retrieve or update the note by ID or title.
- The user could create a new note by the title only or deleted by the ID
- Every call will return an appropriate HTTP status code and a message whether it was successful or not
- A simple array, list or dictionary is sufficient to store the notes. 

<br>

### API calls to complete

| Method | URL | Action |
| ------ | --- | ------ |
| GET | /notes/ | Retrieve all notes |
| GET | /notes/:id | Retrieve the note for the matching ID |
| GET | /notes/:title | Retrieve the note with the specified title |
| PUT | /notes/:id | Update note with the specified ID |
| PUT | /notes/:title | Update note with the specified title |
| POST | /notes/:id | Add a new note and return the note ID |
| DELETE | /notes/:id | Delete the note with the specified ID |
