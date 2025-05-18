import data as dados
import json

def login():
    x=0


def geralistapecas():
    
    lista = []
    endereco: str
    numlista = 0
    for lis in dados.listas:
        if lis[2] == 0:
            endereco = lis[1]
            numlista = lis[0]
            lis[2] = 1
            break
    
    
    for peca in dados.pecas:
        if peca[5][0:3] == endereco:
            lista.append(peca)

    listaHtml = ''' <thead>
    <tr>
        <th scope="col">BACK</th>
        <th scope="col">PartNumber</th>
        <th scope="col">Nome</th>
        <th scope="col">Endereço</th>
        <th scope="col">Contagem Caixa</th>
        <th scope="col">Anotação</th>
        </tr>
    </thead>
    <tbody>
    '''
    
    linha = ""
    for peca in lista:
        linha = f'''
         <tr>
            <th scope="row">{peca[1]}</th>
            <td>{peca[2]}</td>
            <td>{peca[3]}</td>
            <td>{peca[5]}</td>
            <td><input type="number" min="0" class="form-control" name="{peca[1]}" id="contagem_{peca[1]}" required></td>
            <td><button class="btn btn-warning" type="button" onclick="alert('{peca[1]}')">Nota</button></td>
        </tr>
        '''
        listaHtml += linha
    listaHtml += f'''</tbody> 
    <hr>
    <button class="btn btn-success" type="button" onclick="salvaLista({numlista})">Nota</button>'''

    return listaHtml


def salvaLista(contagem):
    x="Backs:"
    for valor in contagem:
        for peca in dados.pecas:
            if int(valor["name"]) == int(peca[1]):
                peca[7] = int(valor["value"])
                print(":p")
                x+= f"<br>Back:{peca[1]}| QTD:{peca[7]}"
    
          
    
    return x

def relatorioFinal():    
    with open("mydata.json", "w") as final:
       json.dump(dados.pecas, final)
       
    return "OK"

     

    