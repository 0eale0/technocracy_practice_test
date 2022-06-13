from django.forms import model_to_dict

from logic.models import Note
from tests.conftest import InitUsers
from logic.serializers import NoteSerializerView


class TestNotes(InitUsers):
    def test_retrieve(self):
        note = self.notes[0]
        slug = note.slug

        url = f'/api/logic/note/{slug}/'
        response = self.user_authorized.get(url)

        result_from_db = NoteSerializerView(note).data
        result = response.json()

        assert response.status_code == 200
        assert result == result_from_db

    def test_list(self):
        url = f'/api/logic/note/'
        response = self.user_authorized.get(url)

        result_from_db = [NoteSerializerView(note).data for note in self.notes]
        result = response.json()

        assert response.status_code == 200
        assert result == result_from_db

    def test_create(self):
        url = f"/api/logic/note/"
        payload = {"header": "attention",
                   "text": "wow, so cute ^_^",
                   "slug": "warning",
                   "user": self.user.pk}

        response = self.user_authorized.post(path=url, data=payload)

        result = response.json()

        result_from_db = model_to_dict(Note.objects.get(id=result["id"]))

        assert response.status_code == 201
        assert result == result_from_db

