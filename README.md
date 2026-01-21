🚧 Auditoria Automatizada de Pedágios

Solução em Python para automatizar a auditoria de faturas de pedágio, identificando passagens duplicadas, calculando valores recuperáveis e gerando relatórios estruturados em Excel.
O projeto foi desenvolvido com foco em confiabilidade financeira, reutilização mensal e arquitetura modular.

📌 Visão Geral

Auditorias manuais de faturas de pedágio são suscetíveis a erros, retrabalho e perda financeira.
Este projeto automatiza esse processo ao:

Normalizar dados de diferentes fontes

Validar a estrutura das informações

Aplicar regras de auditoria

Consolidar resultados em relatórios claros e auditáveis

A solução é adequada tanto para uso corporativo quanto para estudos e portfólio em automação e análise de dados.

⚙️ Funcionalidades

📂 Leitura de faturas e relatórios em Excel

🔄 Normalização e padronização de dados

✅ Validação de colunas obrigatórias

🔍 Identificação de passagens duplicadas

💰 Cálculo de valores duplicados e recuperáveis

📊 Exportação de relatório final em Excel

🧱 Arquitetura modular e reutilizável

🛠️ Tecnologias Utilizadas

Python 3

pandas

openpyxl

Excel

🧱 Estrutura do Projeto
auditoria-pedagios/
│
├── main.py
│
├── src/
│   ├── loaders/
│   │   ├── file_loader.py
│   │   └── validators/
│   │       ├── schema_validator.py
│   │       └── processors/
│   │           └── normalizer.py
│   │
│   ├── audit/
│   │   └── rules/
│   │       ├── duplicate_passages.py
│   │       └── recoverable_value.py
│   │
│   └── exporters/
│       └── excel_exporter.py
│
└── README.md

🔄 Fluxo de Execução

Carregamento do arquivo Excel

Normalização dos dados

Validação do schema

Pré-processamento para auditoria

Identificação de duplicidades

Cálculo do valor recuperável

Exportação do relatório final

📑 Colunas Obrigatórias

Após a normalização, o DataFrame deve conter:

PLACA
DATA PASSAGEM
PRAÇA
VALOR


A ausência de qualquer uma dessas colunas interrompe a execução, garantindo integridade da auditoria.

▶️ Como Executar
1. Clone o repositório
git clone https://github.com/seu-usuario/auditoria-pedagios.git
cd auditoria-pedagios

2. Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

3. Instale as dependências
pip install pandas openpyxl

4. Configure o arquivo de entrada

No main.py, ajuste:

caminho_arquivo = r"C:\caminho\para\fatura.xlsx"
aba = "PASSAGENS PEDÁGIO"

5. Execute o projeto
python main.py

📤 Saída Gerada

O script gera um arquivo Excel contendo:

Base completa das passagens

Passagens duplicadas identificadas

Valores duplicados

Valores efetivamente recuperáveis

Totais consolidados para auditoria

Exemplo:

RELATÓRIO AUDITORIA SEM PARAR_ FATURA QUIMICO 20.01.2026.xlsx

📈 Benefícios

Redução de erros manuais

Mitigação de riscos financeiros

Padronização do processo de auditoria

Facilidade de manutenção e evolução

Código limpo, legível e orientado a regras de negócio

🚀 Possíveis Evoluções

Suporte a múltiplos layouts de faturas

Parametrização das regras de auditoria

Interface CLI interativa

Integração com banco de dados

Logs estruturados e versionamento de execuções

📄 Licença

Este projeto está sob a licença MIT.
Sinta-se à vontade para usar, modificar e contribuir.

👤 Autor

Guto
Estudante de Engenharia de Software / TI
Foco em Back-End, Automação e Análise de Dados