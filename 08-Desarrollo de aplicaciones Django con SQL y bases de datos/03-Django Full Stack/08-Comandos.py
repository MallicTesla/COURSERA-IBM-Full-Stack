count()

# Cuenta el número de objetos.

MyModel.objects.count()

# ------------------------------------------------------------------------------------------
Sum()

# Proporciona la suma de un campo.

MyModel.objects.aggregate(Sum('field'))

# ------------------------------------------------------------------------------------------
Avg()

# Calcula la media de un campo.

MyModel.objects.aggregate(Avg('field'))

# ------------------------------------------------------------------------------------------
Max()

# Proporciona el valor máximo de un campo.

MyModel.objects.aggregate(Max('field'))

# ------------------------------------------------------------------------------------------
Mín()

# Proporciona el valor mínimo de un campo.

MyModel.objects.aggregate(Min('field'))

# ------------------------------------------------------------------------------------------
order_by()

# Ordena los objetos en función de un campo.

MyModel.objects.order_by('field')

# ------------------------------------------------------------------------------------------
order_by(-)

# Ordena los objetos basándose en los campos en orden descendente.

MyModel.objects.order_by('-field')

# ------------------------------------------------------------------------------------------
select_related

# Realiza una unión interna.

MyModel.objects.select_related('modelo_relacionado')

# ------------------------------------------------------------------------------------------
prefetch_related

# Realiza una unión externa izquierda.

MyModel.objects.prefetch_related('modelo_relacionado')

# ------------------------------------------------------------------------------------------
many_to_many

# Realiza la unión muchos-a-muchos.

obj.many_to_many_field.all()
# ------------------------------------------------------------------------------------------
filter(ForeignKey)

# Realiza uniones condicionales.

MyModel.objects.filter(related_model__isnull=True)