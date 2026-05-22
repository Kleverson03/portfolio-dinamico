from django.db import models

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('work', 'Trabalho'),
        ('education', 'Educação'),
        ('certification', 'Certificação'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Cargo/Título")
    company = models.CharField(max_length=200, verbose_name="Empresa/Instituição")
    description = models.TextField(verbose_name="Descrição")
    type_of_experience = models.CharField(
        max_length=20, 
        choices=EXPERIENCE_TYPES,
        default='work',
        verbose_name="Tipo"
    )
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(null=True, blank=True, verbose_name="Data de Término")
    is_current = models.BooleanField(default=False, verbose_name="Atual")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
    
    def __str__(self):
        return f"{self.title} - {self.company}"
