from django.db import models

# Create your models here.CREAR TABLAS POR MEDIOS DE CLASS ay que heredar de models.Model

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5) 
    #convertir el objero carrera a txt para mostrar 
    def __str__(self) :
        txt = "{0} (Duración: {1} ano(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPeterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino') 
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    
    #funcion para sacar nombre completa
    def nombreCompleto(self):
        txt = "{0} {1},{2}"
        return txt.format(self.apellidoPeterno, self.apellidoMaterno, self.nombre)
    #funcion str para ver el estado del estudiante y mostrarlo como texto
    def __str__(self) :
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "ACTIVO"
        else: 
            estadoEstudiante = "BAJA"    
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)
    
class Curso (models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)
    
    #convertir el object Curso  A sTRING
    def __str__(self) :
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)
        
  

class Matricula (models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    
    #a string
    def __str__(self):
        txt = "{0}  matriculad{1} en el curso {2} / Fecha: {3}"
        #condicion para que diga si es matriculado/a
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"   
        #formatear la fecha
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")     
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso , fecMat )
        
    