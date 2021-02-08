from django.db.models import Model


class BaseController:
    def __init__(self, model: Model) -> None:
        self.model = model

    def read_all(self) -> list:
        return self.model.objects.all()

    def read_by_id(self, id: int) -> Model:
        return self.model.objects.filter(id=id).get()

    def create(self, object_params: dict) -> Model:
        new_object = self.model(**object_params)
        new_object.save()
        return new_object

#    def update(self, id: int, new_object_params: dict) -> Model:
#        object_in_database = self.model.objects.filter(id=id).get()
#        object_in_database = self.model(**new_object_params)
#        return object_in_database.save()

    def delete(self, id: int) -> None:
        object_ = self.read_by_id(id=id)
        object_.delete()
