import json

def alocar():
    query= db(db.planta).select().first()
    plantaurl = URL('cadastros', 'download', args=query.image)
    todas_caixas = db(db.setor).select()
    return dict(plantaurl=plantaurl, todas_caixas=todas_caixas
                )

def alocar_referencia():
    query= db(db.planta).select().first()
    plantaurl = URL('cadastros', 'download', args=query.image)
    return dict(plantaurl=plantaurl)

def salvar_caixa():
    listaCaixa =json.loads(request.vars.listaCaixa)
    db(db.setor).delete()
    for caixa in listaCaixa:
        caixa = {str(k): v for k, v in caixa.items()}
        db.setor.insert(**caixa)
    response.flash="Salvo"
