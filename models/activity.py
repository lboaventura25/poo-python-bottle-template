class Activity:
    def __init__(self, id, name, description, done):
        self.id = id
        self.name = name
        self.description = description
        self.done = done

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'done': self.done
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class ActivityModel:
    FILE_PATH = 'data/activities.json'

    def __init__(self):
        self.activities = self._load()

    def _load(self):
        print('----> Carregando atividades da aplicação...')
        import json, os
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            return [Activity.from_dict(item) for item in json.load(f)]

    def _save(self):
        import json
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.activities], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.activities

    def get_by_id(self, activity_id):
        return next((a for a in self.activities if a.id == activity_id), None)

    def add(self, activity):
        self.activities.append(activity)
        self._save()

    def update(self, updated_activity):
        for i, a in enumerate(self.activities):
            if a.id == updated_activity.id:
                self.activities[i] = updated_activity
                self._save()
                break

    def delete(self, activity_id):
        self.activities = [a for a in self.activities if a.id != activity_id]
        self._save()


# if __name__ == '__main__':
    # activity_json = {
    #     'id': 1, 
    #     'name': 'Estudar', 
    #     'description': 'Estudar para a prova de cálculo', 
    #     'done': False
    # }

    # activity = Activity.from_dict(activity_json)

    # act_model = ActivityModel()
    # print(act_model.get_all())
    # print('='*9)

    # a = act_model.get_by_id(1)
    # print(a.to_dict(), end="\n===\n")
