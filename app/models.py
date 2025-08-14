from django.db import models

class Inicio(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=300, null=True, blank=True)
    historia = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Time(models.Model):
    nome = models.CharField(max_length=100)
    bandeira = models.ImageField(upload_to='bandeira-time/')

    def __str__(self):
        return self.nome

class Partida(models.Model):
    casa = models.ForeignKey(Time, related_name='casa', on_delete=models.CASCADE)
    visitante = models.ForeignKey(Time, related_name='visitante', on_delete=models.CASCADE)
    gols_casa = models.PositiveSmallIntegerField()
    gols_visitante = models.PositiveSmallIntegerField()

    competicao = models.CharField(max_length=500)
    data = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('agendada', 'Agendada'),
        ('andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
        ('adiada', 'Adiada'),
        ('cancelada', 'Cancelada'),
        ])
    artilheiro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.casa.nome} x {self.visitante.nome}"


class Jogadores(models.Model):
    nome = models.CharField(max_length=200)
    posicao = models.CharField(max_length=20, choices=[
    ('GK', 'Goleiro'),
    ('LD', 'Lateral Direito'),
    ('LE', 'Lateral Esquerdo'),
    ('ZAG', 'Zagueiro'),
    ('VOL', 'Volante'),
    ('MD', 'Meia Direita'),
    ('ME', 'Meia Esquerda'),
    ('MC', 'Meia Central'),
    ('MAT', 'Meia Atacante'),
    ('AD', 'Ala Direito'),
    ('AE', 'Ala Esquerdo'),
    ('PD', 'Ponta Direita'),
    ('PE', 'Ponta Esquerda'),
    ('SA', 'Segundo Atacante'),
    ('CA', 'Centroavante'),
    ])
    idade = models.IntegerField()
    dt_nasc = models.DateField()
    imagem = models.ImageField(upload_to='jogadores-elenco/')

    def __str__(self):
        return self.nome

class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=300, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    criador = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo