import json

def alocar():
    query= db(db.planta).select().first()
    plantaurl = URL('cadastros', 'download', args=query.image)
    return dict(plantaurl=plantaurl)

def alocar_referencia():
    query= db(db.planta).select().first()
    plantaurl = URL('cadastros', 'download', args=query.image)
    return dict(plantaurl=plantaurl)

def salvar_caixa():
    listaCaixa =json.loads(request.vars.listaCaixa)
    pass

