from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    image = models.URLField(verbose_name="URL da Imagem")
    github_url = models.URLField(verbose_name="URL do GitHub")
    live_url = models.URLField(blank=True, null=True, verbose_name="URL ao Vivo")
    technologies = models.JSONField(default=list, verbose_name="Tecnologias")
    date_created = models.DateField(verbose_name="Data de Criação")
    featured = models.BooleanField(default=False, verbose_name="Destaque")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
    
    def __str__(self):
        return self.title