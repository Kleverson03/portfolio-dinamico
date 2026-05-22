from django.db import models

class Skill(models.Model):
    CATEGORIES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Banco de Dados'),
        ('tools', 'Ferramentas'),
        ('other', 'Outro'),
    ]
    
    LEVELS = [
        ('beginner', 'Iniciante'),
        ('intermediate', 'Intermediário'),
        ('advanced', 'Avançado'),
        ('expert', 'Especialista'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nome")
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name="Categoria")
    level = models.CharField(max_length=20, choices=LEVELS, verbose_name="Nível")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['category', '-level', 'name']
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return f"{self.name} - {self.get_level_display()}"
