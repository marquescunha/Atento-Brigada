def alocar():
    query= db(db.planta).select().first()
    plantaurl = URL('cadastros', 'download', args=query.image)
    return dict(plantaurl=plantaurl)