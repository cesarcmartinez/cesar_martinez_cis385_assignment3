from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from matplotlib.pyplot import title

app = Flask(__name__)
api = Api(app)

NOTES = {
    1 : {'title': 'First Note', 'body': 'Some general text for the 1st note.'},
    2 : {'title': 'Second Note', 'body': 'Some general text for the 2nd note.'},
    3 : {'title': 'Third Note', 'body': 'Some general text for the 3rd note.'}, 
    4 : {'title': 'Fourth Note', 'body': 'Some general text for the 4th note.'},
    5 : {'title': 'Fifth Note', 'body': 'Some general text for the 5th note.'}
}

def abort_if_note_doesnt_exist(note_id, int):
    if note_id not in NOTES:
        abort(404, message="Note {} does NOT exist".format(note_id, int))
        
def abort_if_noteByTitle_doesnt_exist(title, str):
    titles = []
    for note in NOTES:
        thisNote = NOTES[note]
        titles.append(thisNote['title'])
    if title not in titles:
        abort(404, message="Note {} does NOT exist".format(title, str))

parser = reqparse.RequestParser()
# // parser.add_argument('task')
parser.add_argument('title')
parser.add_argument('body')

# ! Note
# *  show a single note item and lets you GET, DELETE, PUT a note item

class Note(Resource):
    def get(self, note_id):
        abort_if_note_doesnt_exist(note_id, int)
        return NOTES[note_id]

    def delete(self, note_id):
        abort_if_note_doesnt_exist(note_id, int)
        del NOTES[note_id]
        return '', 204

    def put(self, note_id):
        abort_if_note_doesnt_exist(note_id, int)
        args = parser.parse_args()
        note = {'title': args['title'], 'body': args['body']}
        NOTES[note_id] = note
        return note, 201

# ! Notes List
# * shows a list of all notes and lets you GET, POST a note item

class NotesList(Resource):
    def get(self):
        return NOTES

    def post(self):
        args = parser.parse_args()
        idValue = len(NOTES) + 1
        NOTES[idValue] = {'title': args['title'], 'body': args['body']}
        return NOTES[idValue], 201
    
# ! Notes by Title List
# * shows a list of all notes and lets you GET. PUT the note's title

class NotesByTitle(Resource):
    def get(self, title):
        abort_if_noteByTitle_doesnt_exist(title, str)
        for note in NOTES:
            thisItem = NOTES[note]
            if thisItem['title'] == title:
                return thisItem

    def put(self, title):
        abort_if_noteByTitle_doesnt_exist(title, str)
        for note in NOTES:
            thisItem = NOTES[note]
            if thisItem['title'] == title:
                args = parser.parse_args()             
                updatedNote = {'title': args['title'], 'body': args['body']}
                NOTES[note] = updatedNote
                return NOTES[note], 201

# setup the API resource routing here

api.add_resource(NotesByTitle, '/notes/<string:title>')
api.add_resource(NotesList, '/notes')
api.add_resource(Note, '/notes/<int:note_id>')

if __name__ == '__main__':
    app.run(debug=True)