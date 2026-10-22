from django.contrib import admin
from .models import Album, Cancion

def _formatear_monto(monto):
    return f"${monto:,}".replace(",", ".")

# Acción en lote para dar de baja registros seleccionados
@admin.action(description="Marcar álbumes seleccionados como NO disponibles")
def marcar_como_no_disponible(modeladmin, request, queryset):
    actualizados = queryset.update(disponible=False)
    modeladmin.message_user(request, f"{actualizados} álbum(es) fueron marcados como no disponibles.")

class CancionInline(admin.TabularInline):
    model = Cancion
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio_formateado', 'estado_disponibilidad', 'fecha_lanzamiento')
    list_filter = ('disponible', 'fecha_lanzamiento')
    search_fields = ('titulo', 'descripcion')
    inlines = [CancionInline]
    actions = [marcar_como_no_disponible] # Registra la acción masiva

    # Columna calculada con formato de pesos
    @admin.display(description='Precio')
    def precio_formateado(self, obj):
        return _formatear_monto(obj.precio)

    # Columna calculada para ver el estado claro
    @admin.display(description='Estado')
    def estado_disponibilidad(self, obj):
        return "Disponible" if obj.disponible else "Agotado / No publicado"