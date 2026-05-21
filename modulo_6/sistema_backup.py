import shutil
import os


pasta_origem = "arquivos_importantes"
pasta_destino = "pasta_backup"


if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)
    print(f"Pasta '{pasta_origem}' foi criada! Coloque arquivos dentro dela e execute novamente.")
    exit() 


if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

for nome_arquivo in os.listdir(pasta_origem):
    caminho_origem = os.path.join(pasta_origem, nome_arquivo)
    caminho_destino = os.path.join(pasta_destino, nome_arquivo)

    # Copia só se for arquivo (ignora pastas dentro dela)
    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_destino)
        print(f"Copiado: {nome_arquivo}")

print("✅ Backup finalizado com sucesso!")