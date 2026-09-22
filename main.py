# Dicionário que representa o menu principal do SpotFEI, exibido ao iniciar o programa
menu = {
    1: "🎤 CRIAR UMA NOVA CONTA ➕",
    2: "🔐 ENTRAR NA SUA CONTA 🔑",
    0: "🚪 SAIR DO SPOTFEI 👋",
}


# Dicionário que representa o menu exibido após o usuário entrar em sua conta
menu2 = {
    1: "🔎 BUSCAR MÚSICAS DISPONÍVEIS 🎵",
    2: "🎶 GERENCIAR SUAS PLAYLISTS 📂",
    3: "📜 VER HISTÓRICO DE LIKES E DISLIKES 👍👎",
    0: "⬅️ SAIR DA CONTA 🚪",
}


# Dicionário com opções que aparecem ao interagir com uma música específica
menu3 = {
    1: "➕ ADICIONAR MÚSICA A UMA PLAYLIST 🎵",
    2: "❤️ CURTIR A MÚSICA 👍",
    3: "💔 DESCURTIR A MÚSICA 👎",
    0: "↩️ VOLTAR 🔙",
}


# Dicionário com opções para gerenciar playlists
menu4 = {
    1: "➕ CRIAR NOVA PLAYLIST 📂",
    2: "🗑️ EXCLUIR PLAYLIST ❌",
    3: "✏️ EDITAR PLAYLIST 📝",
    4: "👀 VISUALIZAR PLAYLISTS 📋",
    0: "↩️ VOLTAR 🔙",
}


# Dicionário com opções dentro do submenu de edição de uma playlist
menu5 = {
    1: "✏️ EDITAR NOME DE UMA PLAYLIST 📝",
    2: "🗑️ REMOVER MÚSICA DE UMA PLAYLIST ❌",
    0: "↩️ VOLTAR 🔙",
}


# Essa função imprime o cabeçalho do programa com nome do projeto, slogan e meu nome:
def slogan():
    print("\n" + "=" * 60)
    print("🎧🎶 BEM-VINDO AO SPOTFEI 🎶🎧".center(60)) # Imprime o título centralizado
    print("=" * 60)
    print("✨ SUA VIBE, SEU SOM, DO SEU JEITO ✨".center(60)) # Imprime o slogan centralizado
    print("-" * 60)
    print("👨‍💻 CREATED BY: DAVI PINHEIRO FERREIRA".center(60))  # Imprime minhas informações centralizadas
    print("-" * 60 + "\n")


# Essa função roda todas as funções deste programa, é nela que estão sendo chamadas as funções secundárias:
def main():
    slogan()

    while True: #Loop principal (menu inicial)
        escolha = exibir_menu() #Exibe menu inicial

        if escolha == "1":
            criar_conta()

        elif escolha == "2":
            logado, email_login = entrar_conta()

            if logado: #Se der certo o login
                while True: #Loop do menu usuário
                    escolha2 = exibir_menu2() #Exibe menu2

                    if escolha2 == "1":
                        encontrou_musica, codigo = buscar_musica()

                        if encontrou_musica:
                            while True: #Loop com a música encontrada
                                escolha3 = exibir_menu3() #Exibe menu3

                                if escolha3 == "1":
                                    add_m_playlist(email_login, codigo)

                                elif escolha3 == "2" or escolha3 == "3":
                                    add_historico(escolha3, codigo, email_login)

                                elif escolha3 == "0":
                                    break #Volta para o menu anterior

                                else:
                                    print("\n❌ OPÇÃO INVÁLIDA! ESCOLHA UMA OPÇÃO VÁLIDA.\n")

                    elif escolha2 == "2":
                        while True: # Loop para gerenciar playlists
                            escolha4 = exibir_menu4() #Exibe menu4

                            if escolha4 == "1":
                                criar_playlist(email_login)

                            elif escolha4 == "2":
                                remover_playlist(email_login)

                            elif escolha4 == "3":
                                while True: # Loop para editar uma playlist
                                    escolha5 = exibir_menu5() #Exibe menu5

                                    if escolha5 == "1":
                                        editar_nome_playlist(email_login)

                                    elif escolha5 == "2":
                                        remover_m_playlist(email_login)

                                    elif escolha5 == "0":
                                        break #Volta para o menu anterior

                                    else:
                                        print("\n❌ OPÇÃO INVÁLIDA! TENTE NOVAMENTE.\n")

                            elif escolha4 == "4":
                                visualizar_playlist(email_login)

                            elif escolha4 == "0":
                                break #Volta para o menu anterior

                            else:
                                print("\n❌ OPÇÃO INVÁLIDA! TENTE NOVAMENTE.\n")

                    elif escolha2 == "3":
                        exibir_historico(email_login)

                    elif escolha2 == "0":
                        print("\n⬅️ VOCÊ SAIU DA CONTA. ATÉ A PRÓXIMA!\n")
                        break #Volta para o menu inicial

                    else:
                        print("\n❌ OPÇÃO INVÁLIDA! ESCOLHA UMA OPÇÃO VÁLIDA.\n")

        elif escolha == "0":
            sair() #Encerra o programa

        else:
            print("\n❌ OPÇÃO INVÁLIDA! TENTE NOVAMENTE.\n")


# Essa função exibe um menu e solicita uma escolha para o user:
def exibir_menu():
    print("📋 MENU PRINCIPAL:")
    print("-" * 60)

    # Percorre o dicionário 'menu' e imprime cada opção com sua descrição
    for opcao, descricao in menu.items():
        print(f"{opcao} ➤ {descricao}")

    print("-" * 60)

    # Input para o usuário realizar sua opção e armazenado em 'escolha'
    escolha = input("🟡 ESCOLHA UMA OPÇÃO: ")

    return escolha #Retorna a opção escolhida pelo usuário


# Essa função exibe um menu e solicita uma escolha para o user:
def exibir_menu2():
    print("\n👤🎵 MENU DO USUÁRIO:")
    print("-" * 60)

    # Percorre o dicionário 'menu' e imprime cada opção com sua descrição
    for opcao, descricao in menu2.items():
        print(f"{opcao} ➤ {descricao}")

    print("-" * 60)

    # Input para o usuário realizar sua opção e armazenado em 'escolha2'
    escolha2 = input("🟡 ESCOLHA UMA OPÇÃO: ")

    return escolha2 #Retorna a opção escolhida pelo usuário


# Essa função exibe um menu e solicita uma escolha para o user:
def exibir_menu3():
    print("\n🛠️ MENU DE OPERAÇÕES COM MÚSICA:")
    print("-" * 60)

    # Percorre o dicionário 'menu' e imprime cada opção com sua descrição
    for opcao, descricao in menu3.items():
        print(f"{opcao} ➤ {descricao}")

    print("-" * 60)

    # Input para o usuário realizar sua opção e armazenado em 'escolha3'
    escolha3 = input("🟡 ESCOLHA UMA OPÇÃO: ")

    return escolha3 #Retorna a opção escolhida pelo usuário


# Essa função exibe um menu e solicita uma escolha para o user:
def exibir_menu4():
    print("\n🎛️ MENU DE PLAYLISTS:")
    print("-" * 60)

    # Percorre o dicionário 'menu' e imprime cada opção com sua descrição
    for opcao, descricao in menu4.items():
        print(f"{opcao} ➤ {descricao}")

    print("-" * 60)

    # Input para o usuário realizar sua opção e armazenado em 'escolha4'
    escolha4 = input("🟡 ESCOLHA UMA OPÇÃO: ")

    return escolha4 #Retorna a opção escolhida pelo usuário


# Essa função exibe um menu e solicita uma escolha para o user:
def exibir_menu5():
    print("\n📝 MENU DE EDIÇÃO DE PLAYLIST:")
    print("-" * 60)

    # Percorre o dicionário 'menu' e imprime cada opção com sua descrição 
    for opcao, descricao in menu5.items():
        print(f"{opcao} ➤ {descricao}")

    print("-" * 60)

    # Input para o usuário realizar sua opção e armazenado em 'escolha5'
    escolha5 = input("🟡 ESCOLHA UMA OPÇÃO: ")

    return escolha5 #Retorna a opção escolhida pelo usuário


# Essa função cria um novo login para o user e armazena no cadastos.txt
def criar_conta():
    print("\n📋 CRIAÇÃO DE CONTA - VAMOS COMEÇAR SUA JORNADA MUSICAL!")
    print("-" * 60)

    # Validador de email se tem @ e .
    while True:
        email = input("📧 DIGITE SEU E-MAIL: ").strip().lower() #Tira os espaços e deixa lower (minusculo)
        if email == "":
            print("❌ O E-MAIL NÃO PODE ESTAR VAZIO.")
        elif "@" in email and "." in email:
            print("✅ E-MAIL VALIDADO COM SUCESSO!")
            break
        else:
            print("❌ E-MAIL INVÁLIDO! TENTE NOVAMENTE.")

    # Validador de senha 
    while True:
        senha = input("🔒 CRIE UMA SENHA: ").strip() #Tira os espaços em ambas as linhas
        confirm_senha = input("🔒 CONFIRME A SENHA: ").strip() 

        if senha == "" or confirm_senha == "":
            print("❌ A SENHA NÃO PODE SER VAZIA.")
        elif senha == confirm_senha:
            print("✅ SENHA CONFIRMADA COM SUCESSO!")
            break
        else:
            print("❌ AS SENHAS NÃO COINCIDEM! TENTE NOVAMENTE.")

    # Validador de nome
    while True:
        nome = input("📝 INFORME SEU NOME: ").strip() #Tira os espaços
        if nome:
            print(f"✅ NOME '{nome.upper()}' REGISTRADO COM SUCESSO!") #Nome maiúsculo
            break
        else:
            print("❌ NOME INVÁLIDO. DIGITE UM NOME VÁLIDO.")

    #Abre cadastros.txt e salva as novas informações
    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(f"{email},{senha},{nome}\n") # Guarda na mesma linha separando por ","

    print("\n🎉 CONTA CRIADA COM SUCESSO!")
    print(f"🎧 SEJA MUITO BEM-VINDO(A) AO SPOTFEI, {nome.upper()}! 🎧\n")


# Essa função faz login com base no banco de dados cadastros.txt
def entrar_conta():
    print("\n🔐 LOGIN - ACESSE SUA CONTA MUSICAL:")
    print("-" * 60)

    #Solicitações
    email_login = input("📧 E-MAIL: ").strip().lower() #Tira espaços e deixa minusculo
    senha_login = input("🔒 SENHA: ").strip()

    #Controle: Não logado e email não localizado ainda
    logado = False 
    encontrou_email = False

    #Abre o cadastro.txt para validar se os inputs do usuário estão válidos
    with open("cadastros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        email, senha, nome = linha.strip().split(",") # Separa as informações
        if email_login == email.lower():
            encontrou_email = True # Atualiza o controle encontrou_email
            if senha_login == senha:
                print(f"\n✅ LOGIN BEM-SUCEDIDO! 🎉 BEM-VINDO(A), {nome.upper()}!\n")
                logado = True # Atualiza o controle logado
                break #EMAIL OK|SENHO OK
            else:
                print("\n❌ SENHA INCORRETA. TENTE NOVAMENTE.\n")
                break #EMAIL OK|SENHO NO

    if not encontrou_email:
        print("\n❌ E-MAIL NÃO ENCONTRADO. VERIFIQUE OU CRIE UMA CONTA.\n") #EMAIL NO

    return logado, email_login # Retorna o status e o email que está logado


# Essa função encerra o programa
def sair():
    print("\n📴 ENCERRANDO SUA EXPERIÊNCIA NO SPOTFEI...")
    print("🙏 OBRIGADO POR USAR NOSSA PLATAFORMA. ATÉ LOGO!\n")
    exit() #FIM


# Essa função busca uma música no banco de dados do programa
def buscar_musica():
    print("\n🔍 BUSCAR MÚSICAS 🎶")
    print("-" * 60)

    musica_busca = input("📝 DIGITE O NOME DA MÚSICA: ").strip()
    encontrou_musica = False #Controle

    # Abre e le as linhas de musica.txt
    with open("musicas.txt", "r") as arquivo_musicas:
        musicas = arquivo_musicas.readlines()

    for linha in musicas:
        id, nome_musica, nome_artista, album_musica, duracao = linha.strip().split(",") #Divide a linha em partes

        # Altera o controle se a musica buscada está no banco de dados
        if musica_busca.lower() == nome_musica.lower():
            encontrou_musica = True #Altera o controle

            print("\n✅ 🎵 MÚSICA ENCONTRADA!\n")
            print(f"🎶 Música: {nome_musica}")
            print(f"🎤 Artista: {nome_artista}")
            print(f"💿 Álbum: {album_musica}")
            print(f"⏱️ Duração: {duracao}")
            break
    
    #Se não tiver a música
    if not encontrou_musica:
        print("\n❌ 😞 MÚSICA NÃO ENCONTRADA. TENTE NOVAMENTE.")

    return encontrou_musica, id #Retorna o status e o id da música


# Essa função adiciona um histórico ao registro histórico.txt
def add_historico(escolha3, cod, email):
    #Defien o tipo com base na escolha
    if escolha3 == "2":
        tipo = "👍"
    elif escolha3 == "3":
        tipo = "👎"

    # Abre histórico para verificar se já tem a opção que o user quer colocar
    with open("historico.txt", "r", encoding="utf-8") as arquivo_historico: #Usando encoding="utf-8" para conseguir ler os emjis
        conteudo_historico = arquivo_historico.readlines()

    #Controle de existencia de linha:
    nova_linha = None # Vai guardar a nova entrada para o histórico
    ja_existe = False

    # Busca a música com o código correspondente
    with open("musicas.txt", "r", encoding="utf-8") as musicas: 
        for linha in musicas:
            id, nome_musica, nome_artista, album_musica, duracao = linha.strip().split(",")
            if cod == id: #Esse cod vem da música encontrada
                nova_linha = f"{tipo},{nome_musica},{nome_artista},{email}\n"
                break

    # Percorre o histórico procurando se a música já sofreu alguma ação nesse usuário
    for i, linha in enumerate(conteudo_historico):
        tipo_hist, nome_hist, artista_hist, email_hist = linha.strip().split(",")

        if nome_hist == nome_musica and artista_hist == nome_artista and email_hist == email:
            ja_existe = True #Confirma que já foi add em historico antes

            #Se tiver igual
            if tipo_hist == tipo:
                print(f"⚠️ '{nome_musica}' JÁ FOI MARCADA COM {tipo} ANTERIORMENTE.")
            else: #Se tiver oposta
                conteudo_historico[i] = nova_linha
                print(f"🔁 HISTÓRICO ATUALIZADO: MÚSICA MARCADA COM {tipo}!")
            break
    
    #Se ainda não existir em historico.txt
    if not ja_existe:
        conteudo_historico.append(nova_linha) #add em historico
        print(f"✅ MÚSICA '{nome_musica}' REGISTRADA NO HISTÓRICO COMO {tipo}!")

    with open("historico.txt", "w", encoding="utf-8") as arquivo_historico:
        for linha in conteudo_historico:
            arquivo_historico.write(linha) #atualiza o arquivo de historico


# Essa função exibe o histórico de um usuário, mostrando seus likes e dislikes
def exibir_historico(email_login):
    print("\n📜 EXIBINDO SEU HISTÓRICO MUSICAL 🎶")
    print("=" * 60)

    with open("historico.txt", "r", encoding="utf-8") as hist:
        historico = hist.readlines()

    # Se ainda não ter o historico.txt
    if not historico:
        print("📁 HISTÓRICO ESTÁ VAZIO!")
        print("😕 CURTA OU DESCURTA MÚSICAS PARA VER SEU HISTÓRICO AQUI.")
        print("=" * 60 + "\n")
        return

    #Controle de busca
    encontrou = False

    for linha in historico:
        tipo, musica, artista, email = linha.strip().split(",")

        # Se o email guardado em historico for igual ao email logado
        if email == email_login:
            encontrou = True #Histoco deste login encontrado
            if tipo == "👍":
                acao = "VOCÊ CURTIU"
            elif tipo == "👎":
                acao = "VOCÊ DESCURTIU"

            print(f"{tipo} {acao}: 🎵 '{musica.upper()}' DE {artista.upper()}")

    #Se o user não fez nenhuma ação no histórico
    if not encontrou:
        print("😕 VOCÊ AINDA NÃO TEM NENHUMA INTERAÇÃO SALVA NO HISTÓRICO.")

    print("=" * 60 + "\n")


# Essa funçãp cria uma playlist para o usuário logado
def criar_playlist(email_login):
    print("\n🎶 CRIAÇÃO DE NOVA PLAYLIST")
    print("✨ VAMOS MONTAR SUA COLEÇÃO DE MÚSICAS FAVORITAS!")

    nome_playlist = input("📝 DIGITE O NOME DA NOVA PLAYLIST: ").strip()
    conteudo_playlist = {} #Aquificarão as músicas da playlist

    if nome_playlist == "":
        print("❌ NOME INVÁLIDO. DIGITE UM NOME PARA SUA PLAYLIST.")
        return

    #Addiciona as informações da playlist em playlists.txt
    with open("playlists.txt", "a") as playlists:
        playlists.write(f"{nome_playlist},{conteudo_playlist},{email_login}\n")

    print(f"✅ PLAYLIST '{nome_playlist.upper()}' CRIADA COM SUCESSO! 🎧")
    print("💡 Agora você pode adicionar músicas a ela no menu de opções!\n")
    return


# Essa função exclui uma playlist do usuário logado
def remover_playlist(email_login):
    print("\n📂 SUAS PLAYLISTS DISPONÍVEIS:")

    playlists_usuario = [] # Lista para guardar as playlists do user logado

    # Abre o arquivo playlists.txt e busca as playlists do user
    with open("playlists.txt", "r") as playlists:
        for linha in playlists:
            nome, conteudo, email = linha.strip().split(",", 2)
            if email == email_login:
                playlists_usuario.append(nome) #Add nome da playlist na lista de playlists do user logado

    # Se o user não tiver playlists
    if not playlists_usuario:
        print("⚠️ VOCÊ AINDA NÃO CRIOU NENHUMA PLAYLIST PARA REMOVER.\n")
        return
    
    # Exibe as playlists encontradas
    for nome in playlists_usuario:
        print(f"🎧 {nome}")

    print("\n🗑️ EXCLUSÃO DE PLAYLIST")
    nome_playlist = input("✏️ DIGITE O NOME EXATO DA PLAYLIST QUE DESEJA REMOVER: ").strip() # Solicita o nome da playlist que será escolhida

    nova_lista = [] # Lista para manter as demais playlists
    removida = False # Verificador da remoção da playlist

    # Le denovo o arquivo agora para validar o nome da playlist
    with open("playlists.txt", "r") as playlists:
        for linha in playlists:
            nome, conteudo, email = linha.strip().split(",")
            if nome == nome_playlist and email == email_login:
                removida = True
                continue #Skip a linha que será removida
            nova_lista.append(linha) # Add linha na nova_lista

    #Se removida, reescrever o arquivo com as demais playlists
    if removida:
        with open("playlists.txt", "w") as playlists:
            playlists.writelines(nova_lista)
        print(f"✅ PLAYLIST '{nome_playlist.upper()}' FOI REMOVIDA COM SUCESSO! 🧹\n")
    else:
        print("❌ PLAYLIST NÃO ENCONTRADA OU NÃO PERTENCE A VOCÊ. TENTE NOVAMENTE.\n")


# Essa função adiciona novas músicas a uma playlist já criada pelo user logado
def add_m_playlist(email_login, codigo):
    # Abre playlists.txt e le todas as linhas
    with open("playlists.txt", "r") as playlists:
        linhas = playlists.readlines()

    playlists = [] #Armazenador das playlists do user

    for linha in linhas:
        nome_playlist, conteudo_playlist, email = linha.strip().split(",")
        if email == email_login: # Verifica se a playlist pertence ao usuário
            playlists.append([nome_playlist, conteudo_playlist, email])

    # Se não tiver playlists
    if not playlists:
        print("❌ VOCÊ AINDA NÃO POSSUI NENHUMA PLAYLIST.")
        return

    print("\n📂 ESCOLHA UMA PLAYLIST PARA ADICIONAR A MÚSICA:")
    for i, (nome, _, _) in enumerate(playlists): # Enumera os nomes das playlists
        print(f"{i + 1} ➤ {nome}") # i começa em 0+1

    escolha = input("✏️ DIGITE O NÚMERO DA PLAYLIST: ")
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(playlists)): # Verifica se o input tem apenas dígitos numéricos e se ele está detro do limite de opções
        print("🚫 OPÇÃO INVÁLIDA.")
        return

    playlist_selecionada = playlists[int(escolha) - 1] # Aponta qual a playlist escolhida e ajusta o indice para 0 novamente
    nome_escolhido = playlist_selecionada[0]  # Aponta o nome da playlist escolhida

    # Buscar a musica para add na playlist
    with open("musicas.txt", "r") as musicas:
        musicas = musicas.readlines()

    musica_formatada = "" # strig que será adicionada na playlist
    for m in musicas:
        id, nome, nome_artista, album, duracao = m.strip().split(",")
        if id == codigo:
            musica_formatada = f"{id}:{nome}"
            break

    novas_linhas = []
    for l in linhas:
        nome, conteudo, email = l.strip().split(",")
        if nome == nome_escolhido and email == email_login:
            # Verifica se a playlist está vazia ou contém "{}"
            if conteudo == "" or conteudo == "{}":
                novo_conteudo = musica_formatada #Apenas a nova música será o conteudo
            else:
                # Caso já exista conteúdo na playlist
                lista_musicas = conteudo.split("|")
                if musica_formatada in lista_musicas:
                    print("⚠️ ESSA MÚSICA JÁ ESTÁ NA PLAYLIST.")
                    return
                # Caso não tenha
                novo_conteudo = conteudo + "|" + musica_formatada
            l = f"{nome},{novo_conteudo},{email}\n" # Nova linha gerada
        novas_linhas.append(l) # nova linha inserida

    #Escrevendo as novas linhas na playlist.txt
    with open("playlists.txt", "w") as playlists:
        playlists.writelines(novas_linhas)

    print(f"✅ MÚSICA ADICIONADA À PLAYLIST '{nome_escolhido.upper()}'! 🎶")


# Essa função remove músicas de uma playlist já criada pelo usuário
def remover_m_playlist(email_login):
    with open("playlists.txt", "r") as play:
        linhas = play.readlines()

    playlists_user = [] #Armazena as playlists do user

    for linha in linhas:
        nome, conteudo, email = linha.strip().split(",")
        if email == email_login:
            playlists_user.append((nome, conteudo, email)) # Add na lista se a playlist for do user

    #Se o user não tiver playlists
    if not playlists_user:
        print("❌ VOCÊ NÃO POSSUI PLAYLISTS.")
        return

    print("\n🎵 SUAS PLAYLISTS:")
    # Printa as opções
    for elemento in playlists_user:
        nome = elemento[0]
        print(f"• {nome}")

    nome_escolhido = input("\n📝 DIGITE O NOME EXATO DA PLAYLIST: ").strip() # Solicita a escolha

    playlist_encontrada = None # Controle de busca da playlist

    for item in playlists_user:
        nome = item[0]
        conteudo = item[1]
        email = item[2]
        if nome == nome_escolhido:#Se encontrar o nome informado
            playlist_encontrada = (nome, conteudo, email) #Guarda a informação dalinha completa
            break
    
    #SE não
    if playlist_encontrada is None:
        print("❌ PLAYLIST NÃO ENCONTRADA.")
        return

    #Dados da playlist encontrada
    nome = playlist_encontrada[0]
    conteudo = playlist_encontrada[1]
    email = playlist_encontrada[2]

    #Se estiver vazia
    if conteudo == "" or conteudo == "{}":
        musicas = [] # Cria lista vazia de musicas
    else:
        musicas = conteudo.split("|") # Separa as musicas com | em uma lista

    # Se a playlist tiver vazia, verificação do conteudo 
    if len(musicas) == 0:
        print("⚠️ ESSA PLAYLIST NÃO TEM MÚSICAS.")
        return

    print("\n🎶 MÚSICAS NA PLAYLIST:")
    for musica in musicas:
        if ":" in musica:
            id_musica, nome_musica = musica.strip().split(":")
            print(f"ID: {id_musica} | 🎵 {nome_musica}")

    id_remover = input("\n🗑️ DIGITE O ID DA MÚSICA A SER REMOVIDA: ").strip() #Solicita qual música ele quer tirar

    nova_lista = []
    for musica in musicas:
        if ":" in musica:
            id_musica, nome_musica = musica.strip().split(":")
            if id_musica != id_remover: # Se for uma múscia diferente da que ele quer remover, ele armazena
                nova_lista.append(musica)

    # Se não remover nenhuma musica
    if len(nova_lista) == len(musicas):
        print("❌ MÚSICA NÃO ENCONTRADA.")
        return

    # Formata a nova linha que será inserida
    nova_linha = nome + "," + "|".join(nova_lista) + "," + email + "\n"

    with open("playlists.txt", "w") as playlist:
        for linha in linhas:
            nome_playlist, conteudo_playlist, email_playlist = linha.strip().split(",")
            if nome_playlist == nome and email_playlist == email:
                playlist.write(nova_linha) # Escreve a versão atualizada
            else:
                playlist.write(linha) # Escreve a versão original

    print("✅ MÚSICA REMOVIDA COM SUCESSO DA PLAYLIST!")


# Essa função renomeia uma playlist do usuário logado
def editar_nome_playlist(email_login):
    with open("playlists.txt", "r") as playlists:
        linhas = playlists.readlines()

    playlists_user = []

    for linha in linhas:
        nome, conteudo, email = linha.strip().split(",")
        if email == email_login:
            playlists_user.append([nome, conteudo, email])

    if len(playlists_user) == 0:
        print("❌ VOCÊ NÃO POSSUI PLAYLISTS.")
        return

    print("\n🎵 SUAS PLAYLISTS:")
    for item in playlists_user:
        nome = item[0]
        print(f"• {nome}")

    nome_antigo = input("\n✏️ DIGITE O NOME EXATO DA PLAYLIST: ").strip() # Solicita qual playlist ele quer renomear

    playlist_encontrada = None
    for item in playlists_user:
        nome = item[0]
        conteudo = item[1]
        email = item[2]
        if nome == nome_antigo:
            playlist_encontrada = (nome, conteudo, email) # Quando encontra a playlist, grava ela nessa variável
            break

    # Se não encontrar
    if playlist_encontrada is None:
        print("❌ PLAYLIST NÃO ENCONTRADA.")
        return

    novo_nome = input("🆕 DIGITE O NOVO NOME: ").strip() # Solicita qual será o novo nome da playlist
    if novo_nome == "":
        print("❌ NOME INVÁLIDO.")
        return

    # Define o que é cada coisa da playlist encontrada
    nome_antigo = playlist_encontrada[0]
    conteudo = playlist_encontrada[1]
    email = playlist_encontrada[2]
    nova_linha = novo_nome + "," + conteudo + "," + email + "\n" # Formata a nova linha que será adicionada

    with open("playlists.txt", "w") as arquivo:
        for linha in linhas:
            nome_linha, conteudo_linha, email_linha = linha.strip().split(",")
            if nome_linha == nome_antigo and email_linha == email:
                arquivo.write(nova_linha) # Escreve a versão atualizada
            else:
                arquivo.write(linha) # Escreve a versão original

    print("✅ NOME DA PLAYLIST ALTERADO COM SUCESSO!")


def visualizar_playlist(email_login):
    with open("playlists.txt", "r") as play:
        linhas = play.readlines()

    playlists = []

    for linha in linhas:
        nome, conteudo, email = linha.strip().split(",")
        if email == email_login:
            playlists.append((nome, conteudo, email)) # Adiciona os dados da playlist se pertencer ao usuario logado

    if len(playlists) == 0:
        print("❌ VOCÊ NÃO POSSUI PLAYLISTS.")
        return

    print("\n🎵 SUAS PLAYLISTS:")
    for item in playlists:
        nome = item[0]
        print(f"• {nome}")

    nome_escolhido = input("\n🔍 DIGITE O NOME EXATO DA PLAYLIST: ").strip() # Solicita qual playlist ele quer ver

    playlist_encontrada = None
    for item in playlists:
        nome = item[0]
        conteudo = item[1]
        email = item[2]
        if nome == nome_escolhido:
            playlist_encontrada = (nome, conteudo, email) # Guarda as informações da playlist escolhida
            break

    if playlist_encontrada is None:
        print("❌ PLAYLIST NÃO ENCONTRADA.")
        return

    #Dados da playlist que será exibida
    nome = playlist_encontrada[0]
    conteudo = playlist_encontrada[1]

    if conteudo == "" or conteudo == "{}":
        print(f"📭 A PLAYLIST '{nome.upper()}' ESTÁ VAZIA.")
        return

    musicas = conteudo.split("|") # Separa o conteúdo da playlist nas músicas (separadas por '|')

    print(f"\n🎧 MÚSICAS NA PLAYLIST '{nome.upper()}':")
    for m in musicas:
        if ":" in m:
            id, nome_musica = m.split(":")
            print(f"ID: {id} | 🎵 {nome_musica}") # Print as musicas da playlist escolhida pelo user

if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente(sem import)
    main() #Chama a função main
