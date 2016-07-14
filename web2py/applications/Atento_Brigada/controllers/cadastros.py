def setor():
    form = SQLFORM.grid(db.setor, csv=False)

    response.title = 'cadastros'
    response.subtitle = 'Area'
    return dict(form=form)

def funcao():
    form = SQLFORM.grid(db.funcao, csv=False)

    response.title = 'Função'
    return dict(form=form)