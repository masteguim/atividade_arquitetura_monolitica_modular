from fastapi import HTTPException


def not_found(what='Registro'):
    raise HTTPException(status_code=404, detail=f'{what} não encontrado(a).')


def conflict(message):
    raise HTTPException(status_code=409, detail=message)


def bad_request(message):
    raise HTTPException(status_code=400, detail=message)
