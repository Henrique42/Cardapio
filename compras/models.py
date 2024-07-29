from django.db import models
import os

class Categoria(models.Model):
    nome = models.CharField(unique=True, max_length=50, help_text="Tipo de prato", verbose_name="Categoria")

    def __str__(self):
        return self.nome

def caminho_imagem(instance, filename):
    # Assuming 'instance' is an instance of Prato
    # 'filename' will be the original filename of the uploaded file
    # We'll generate a unique filename based on the nome field
    ext = filename.split('.')[-1]  # Get file extension
    new_filename = f"{instance.nome}.{ext}"
    return os.path.join('uploads/', new_filename)

class Prato(models.Model):
    nome = models.CharField(unique=True, max_length=100, help_text="Nome do prato.", verbose_name="Nome")
    descricao = models.TextField(help_text="Descrição do prato.", verbose_name="Descrição")
    preco = models.DecimalField(help_text="Preço do prato.", verbose_name="Preço", max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to=caminho_imagem)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
