from django.test import TestCase

class MensagemParaDataAtualTest(TestCase):
    def test_natal(self):
        response = self.client.get('/')
        self.assertContains(response, 'É Natal')

    def test_tiradentes(self):
        response = self.client.get('/')
        self.assertContains(response, 'É Tiradentes')

    def test_dia_especial(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hoje não é um dia especial')
