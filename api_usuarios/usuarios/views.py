from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Usuario
from .schemas import UsuarioSchema, UsuarioCreateSchema

api = Router()


@api.get("/usuarios/", response=list[UsuarioSchema])
def get_usuario(request):
    return list(Usuario.objects.all())


@api.get("/usuarios/{usuario_id}/", response=UsuarioSchema)
def get_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return usuario


@api.post("/usuarios/", response=UsuarioSchema)
def create_usuario(request, payload: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**payload.dict())
    return usuario


@api.put("/usuarios/{usuario_id}/", response=UsuarioSchema)
def update_usuario(request, usuario_id: int, payload: UsuarioCreateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in payload.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return usuario


@api.delete("/usuarios/{usuario_id}/")
def delete_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
