
# %%
import boto3
from dotenv import load_dotenv
import os 
from pathlib import Path
import shutil

# Carrega as variáveis
load_dotenv()

# Lê as variáveis de ambiente 
ACCESS_KEY_CLIENTE = os.getenv ("ACCESS_KEY_CLIENTE")
SECRET_KEY_CLIENTE = os.getenv ("SECRET_KEY_CLIENTE")
ENDPOINT_URL = os.getenv("ENDPOINT_URL")

# Set up MinIO client
s3 = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY_CLIENTE,
    aws_secret_access_key=SECRET_KEY_CLIENTE,
    endpoint_url=ENDPOINT_URL,
)

# %%
pasta_local = Path("mock_cliente/seeds")

#Envio arquivos

for pasta in ["baixa", "cessao", "reneg"]:

    caminho_origem = pasta_local / pasta
    caminho_enviado = caminho_origem / "enviados"

    # garante que a pasta enviados existe
    caminho_enviado.mkdir(exist_ok=True)

    for arquivo in caminho_origem.iterdir():

        if arquivo.is_file() and arquivo.suffix == ".txt":

            chave = arquivo.relative_to(pasta_local).as_posix()

            s3.upload_file(
                        Filename=str(arquivo),
                        Bucket="cliente-a-fidc",
                        Key=chave
                    )
            
            print(f"Enviado: {chave}")

            #Move arquivo para enivados
            destino = caminho_enviado / arquivo.name

            shutil.move(
                str(arquivo),
                str(destino)
            )

            print(f"Movido para: {destino}")