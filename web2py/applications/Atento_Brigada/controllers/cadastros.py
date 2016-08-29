def setor():
    form = SQLFORM.grid(db.setor, csv=False)

    response.title = 'cadastros'
    response.subtitle = 'Area'
    return dict(form=form)

def funcao():
    form = SQLFORM.grid(db.funcao, csv=False)

    response.title = 'Função'
    return dict(form=form)

def planta():
    db.planta.id.readable = False
    form = SQLFORM.grid(db.planta, csv=False, create=False, deletable=False, searchable=False)

    response.title = 'planta'
    response.subtitle = 'Planta'
    return dict(form=form)

def download():
    return response.download(request,db)