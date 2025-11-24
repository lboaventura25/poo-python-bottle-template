import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Animal:
    def __init__(self, id, raca, nome, data_nascimento, cor, tem_pedigree):
        self.id = id
        self.raca = raca
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cor = cor
        self.tem_pedigree = tem_pedigree
        

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento,
            'cor': self.cor,
            'tem_pedigree': self.tem_pedigree
        }


class AnimalModel:
    FILE_PATH = os.path.join(DATA_DIR, 'animals.json')

    def __init__(self):
        self.animals = self._load()
        print('-----------------')
        print(f'-> Animais carregados: {len(self.animals)}')
        print('-----------------')

    
    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        else:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f'data={data}')
                return data
    

    def get_all_animals(self):
        return self.animals