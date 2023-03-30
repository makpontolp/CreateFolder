import os
import pathlib
#LOCAL ATUAL DOS ARQUIVOS
FolderLocation = "OldFolder/"
#ARMAZENA NOME DOS ARRQUIVOS EM PILHA
GetNamesFiles = os.listdir(FolderLocation)
i = 0
for FileName in os.listdir(FolderLocation):
    #IDENTIFICA EXTENSAO DO ARQUIVO
    FileExtension = pathlib.Path(GetNamesFiles[i]).suffix
    #IDENTIFICA NOME DO ARQUIVO
    FileName = GetNamesFiles[i]
    #REMOVE EXTENSAO DO NOME
    FolderName = (GetNamesFiles[i].removesuffix(FileExtension))
    #CRIA PASTA COM O NOME DO ARQUIVO
    os.mkdir(FolderName)
    #ARMAZENA LOCAL ANTIGO DO ARQUIVO
    FolderLocationOld = FolderLocation + FileName
    #ARMAZENA NOVO LOCAL DO ARQUIVO
    FolderLocationNew = FolderName + "/" + FileName
    # ESSES PRINTS SAO PRA VALIDAR AS INFOS DAS VARIAVEIS
    #print(FolderName)
    #print(FolderLocationOld)
    #print(FolderLocationNew)
    #FolderName = FolderName + "/" + GetNamesFiles[i]
    #MOVE OS ARQUIVOS PARA AS PASTAS COM OS RESPECTIVOS NOMES
    os.rename(FolderLocationOld,FolderLocationNew)
    #CONTADOR PARA O PROXIMO ARQUIVO
    i += 1
