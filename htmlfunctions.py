def geralistapecas(pecas):
    listaHtml = ""
    
    linha = ""
    for peca in pecas:
        linha = f'''<li class="list-group-item">{peca["Part Number"]}</li>'''
        listaHtml += linha

    return listaHtml