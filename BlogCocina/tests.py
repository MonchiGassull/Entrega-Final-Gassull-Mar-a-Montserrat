from django.test import TestCase
from BlogCocina.models import Articulo

# Create your tests here.

class ArticuloTests(TestCase):
    def test_creacion_articulo(self):
        articulo = Articulo(titulo = "Titulo", subtitulo = "Subtitulo", cuerpo = "Cuerpo", autor = "Autor")
        articulo.save()
        
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertIsNotNone(articulo.id)
        
    def test_articulo_str(self):
        articulo = Articulo(titulo = "Titulo", subtitulo = "Subtitulo", cuerpo = "Cuerpo", autor = "Autor")
        articulo.save()

        self.assertEqual(articulo._str_(), "Titulo | Subtitulo | Autor")