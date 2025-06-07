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


def geralistasingle():
    
    if dados.singlecounts >= 3:
        return "<h1>contagen singles finalizadas</h1>"
    
    lista = []
       
    
    for peca in dados.pecassingle:
        if peca[11] == dados.singlecounts:
            lista.append(peca)

    dados.singlecounts += 1
    
    listaHtml = ''' <thead>
    <tr>
        <th scope="col">BACK</th>
        <th scope="col">PartNumber</th>
        <th scope="col">Nome</th>
        <th scope="col">Modulo</th>
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
    <button class="btn btn-success" type="button" onclick="salvaListaSingle()">Nota</button>'''

    return listaHtml


def salvaLista(contagem):
    x="Backs:"
    for valor in contagem:
        for peca in dados.pecas:
            if int(valor["name"]) == int(peca[1]):
                if(valor["value"] == ''):
                    valor["value"] = '0'
                peca[7] = int(valor["value"])
                print(":p")
                x+= f"<br>Back:{peca[1]}| QTD:{peca[7]}"
          
    
    return x


def salvaListaSingle(contagem):
    x="Backs:"
    for valor in contagem:
        for peca in dados.pecassingle:
            if int(valor["name"]) == int(peca[1]):
                if(peca[11] == 2):
                    if(valor["value"] == ''):
                        valor["value"] = '0'
                    peca[10] = int(valor["value"])
                    peca[11] = 3
                        
                    x+= f"<br>Back:{peca[1]}| QTD:{peca[8]}"
                if(peca[11] == 1):
                    if(valor["value"] == ''):
                        valor["value"] = '0'
                    peca[8] = int(valor["value"])
                    
                    if peca[8] == peca[7]:
                        peca[11] = 3
                        peca[9] = "OK"
                    if peca[8] != peca[7]:
                        peca[11] = 2
                        peca[9] = "Terceira Cotagem"
                        
                    x+= f"<br>Back:{peca[1]}| QTD:{peca[8]}"
                    
                if(peca[11] == 0):
                    if(valor["value"] == ''):
                        valor["value"] = '0'
                    peca[7] = int(valor["value"])
                    peca[11] = 1
                    x+= f"<br>Back:{peca[1]}| QTD:{peca[7]}"

          
    
    return x


def relatorioFinal():
    relatorio = []
    relatoriosingles = []
    
    for peca in dados.pecaspchack:
        relato = {
            "id":peca[0],
            "back":peca[1],
            "PartNumber":peca[2],
            "PartName":peca[3],
            "LotSize":peca[4],
            "Endereco":peca[5],
            "Check":peca[6],
            "Cont1":peca[7],
            "Cont2":peca[8],
            "Xcheck":peca[9],
            "Cont3":peca[10],
            "Status":peca[11]
        }
        relatorio.append(relato)
    
    for peca in dados.pecassingle:
        relato = {
            "id":peca[0],
            "back":peca[1],
            "PartNumber":peca[2],
            "PartName":peca[3],
            "LotSize":peca[4],
            "Modulo":peca[5],
            "OBS":peca[6],
            "Cont1":peca[7],
            "Cont2":peca[8],
            "Xcheck":peca[9],
            "Cont3":peca[10],
            "Status":peca[11]
        }
        relatoriosingles.append(relato)
    
    with open("relato_singles.json", "w") as final:
       json.dump(relatoriosingles, final)        
        
    with open("mydata.json", "w") as final:
       json.dump(dados.pecaspchack, final)
       
    return "OK"

     

    