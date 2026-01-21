# 🚧 Auditoria Automatizada de Pedágios -> Projeto inicial

Solução desenvolvida em **Python** para automatizar a auditoria de faturas de pedágio, identificando passagens duplicadas, calculando valores recuperáveis e gerando relatórios estruturados em **Excel**.

O projeto foi concebido com foco em **confiabilidade financeira**, **reutilização mensal**, **clareza de regras de negócio** e **arquitetura modular**, sendo aplicável tanto em contextos corporativos quanto como projeto de portfólio em **automação, dados e back-end**.

---

## 📌 Visão Geral

Auditorias manuais de faturas de pedágio são processos suscetíveis a:

* Erros humanos
* Retrabalho operacional
* Falhas de conferência
* Perda financeira recorrente

Este projeto automatiza o processo de auditoria ao:

* Normalizar dados provenientes de diferentes fontes
* Validar a estrutura e integridade das informações
* Aplicar regras claras de auditoria
* Consolidar resultados em relatórios claros, rastreáveis e auditáveis

A solução foi desenhada para ser **executada mensalmente**, com mínimo ajuste e alto grau de confiabilidade.

---

## ⚙️ Funcionalidades

* 📂 Leitura de faturas e relatórios em Excel
* 🔄 Normalização e padronização de dados
* ✅ Validação de colunas obrigatórias (schema validation)
* 🔍 Identificação de passagens duplicadas
* 💰 Cálculo de valores duplicados e valores recuperáveis
* 📊 Exportação de relatório final estruturado em Excel
* 🧱 Arquitetura modular, reutilizável e orientada a regras de negócio

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **pandas**
* **openpyxl**
* **Microsoft Excel**

---

## 🧱 Estrutura do Projeto

```text
auditoria-pedagios/
│
├── main.py
├── src/
│   ├── loaders/
│   │   └── file_loader.py
│   ├── validators/
│   │   └── schema_validator.py
│   ├── processors/
│   │   └── normalizer.py
│   ├── audit/
│   │   └── rules/
│   │       ├── duplicate_passages.py
│   │       └── recoverable_value.py
│   └── exporters/
│       └── excel_exporter.py
│
└── README.md
```

A separação por camadas facilita manutenção, testes, evolução das regras e reaproveitamento do código.

---

## 🔄 Fluxo de Execução

1. Carregamento do arquivo Excel
2. Normalização e padronização dos dados
3. Validação do schema
4. Pré-processamento para auditoria
5. Identificação de duplicidades
6. Cálculo do valor recuperável
7. Exportação do relatório final

---

## 📑 Colunas Obrigatórias

Após a normalização, o `DataFrame` deve conter obrigatoriamente as seguintes colunas:

* `PLACA`
* `DATA`
* `PASSAGEM`
* `PRAÇA`
* `VALOR`

A ausência de qualquer uma dessas colunas **interrompe a execução**, garantindo a integridade e a confiabilidade da auditoria.

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/auditoria-pedagios.git
cd auditoria-pedagios
```

### 2. Crie um ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install pandas openpyxl
```

### 4. Configure o arquivo de entrada

No arquivo `main.py`, ajuste:

```python
caminho_arquivo = r"C:\caminho\para\fatura.xlsx"
aba = "PASSAGENS PEDÁGIO"
```

### 5. Execute o projeto

```bash
python main.py
```

---

## 📤 Saída Gerada

O script gera um arquivo Excel contendo:

* Base completa das passagens
* Passagens duplicadas identificadas
* Valores duplicados
* Valores efetivamente recuperáveis
* Totais consolidados para auditoria financeira

**Exemplo de arquivo gerado:**

```
RELATORIO_AUDITORIA_SEM_PARAR_FATURA_20_01_2026.xlsx
```

---

## 📈 Benefícios

* Redução significativa de erros manuais
* Mitigação de riscos financeiros recorrentes
* Padronização do processo de auditoria
* Facilidade de manutenção e evolução
* Código limpo, legível e orientado a regras de negócio

---

## 🚀 Possíveis Evoluções

* Suporte a múltiplos layouts de faturas
* Parametrização dinâmica das regras de auditoria
* Interface CLI interativa
* Integração com banco de dados
* Logs estruturados e versionamento das execuções

---

## 👤 Autor

**Walter Fonseca**  
Estudante de Engenharia de Software / TI  
Foco em **Back-End**, **Automação** e **Análise de Dados**

---
