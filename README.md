# O que é o projeto
Esse é um projeto de engenharia de dados no qual o resultado final é o estoque de um fidc e relatórios diários com cálculo de VP, PDD, VPL. 
O processo envolve a Ingestão de arquivos através do Minio, carregamento no bigquery e transformação com dbt. 

O resultado final esperado é um relatório BI para gestor do fundo e relatórios via arquivo compartilhados no bucket para o cliente. 

# Entregáveis planejados
### Entregáveis

- [x]  Container docker com minio s3
- [x]  Habilitar bucket para envio de arquivos via api
- [ ]  Script python para envio dos arquivos no bucket
- [ ]  Leitura dos arquivos direto no s3 via bigquery (raw)
- [ ]  Pequena transformação para carregar na tabela de stg (Validação de dados + particionamento por data)
- [ ]  Transformação usando dbt (uniao dos arquivos transformando em movimentações)
- [ ]  int dos calculos de VP, PDD, VPL, Taxa cessão (+validação dos dados)
- [ ]  Resultado final → Tabela de histórico do estoque por data ref e cálculo de VP, PDD, VPL diário
- [ ]  Disparo por E-mail sobre fundo calculado e resumo dos valores
- [ ]  Envio de arquivo de estoque + aquisicao + baixas por bucket s3
- [ ]  Relatório em plataforma moderna de dados com histórico de VP, PDD, VPL e Caixa da carteira


# Etapas para execução do projeto
As etapas a seguir servem como um gui para quem quiser replicar o projeto e fazer do zero todas as etapas. 

## Docker 
1. Rode para validar o config do docker
   > docker compose --env-file .env -f docker/docker-compose.yml config
2. Config confirmado pode subir o container
   > docker compose --env-file .env -f docker/docker-compose.yml up -d
3. Para confirmar se container está de pé
   > docker ps

## Minio
1. Caso não tenha instalado, installe o mc no seu computador.
> C:\Program Files\mc
2. Set an alias for your local or remote MinIO server
> mc alias set mb http://127.0.0.1:9000 admin zTM6qt2xp1MrjTu46K4e

3. Create the bucket if you haven't already
> mc mb myminio/cliente-a-fidc

4. Cria a policy para o bucket
> mc admin policy create mb cliente-upload docker/policies/cliente-upload.json

5. Cria um acesskey
> mc admin accesskey create mb --policy docker/policies/cliente-upload.json

6. Para listar os acesskey
> mc admin accesskey list mb
7. Setando alias para o acesso do cliente 