# 🚀 Sistema de Busca de Operadoras de Saúde

Interface web em Vue.js e servidor em Python para buscas em dados de operadoras da ANS (Agência Nacional de Saúde Suplementar).

## 📋 Sobre o Projeto

Este é um sistema full-stack que permite buscar informações sobre operadoras de planos de saúde cadastradas na ANS. O projeto foi desenvolvido como teste técnico e está otimizado para deploy em produção.

### ✨ Funcionalidades

- 🔍 **Busca Textual**: Busca por razão social ou nome fantasia
- 📊 **Dados Completos**: Exibe informações detalhadas das operadoras
- 🌐 **Interface Responsiva**: Frontend moderno em Vue.js
- 🚀 **Deploy Pronto**: Configurado para Render.com

## 🏗️ Arquitetura

- **Backend**: Flask (Python) com API REST
- **Frontend**: Vue.js 3 com Axios
- **Dados**: CSV com dados das operadoras da ANS
- **Deploy**: Render.com (gratuito)

## 🚀 Deploy no Render.com

### Opção 1: Deploy Automático (Recomendado)

1. **Execute o script de preparação:**
   ```bash
   python deploy.py
   ```

2. **Faça upload da pasta `deploy/` para o Render.com:**
   - Acesse [render.com](https://render.com)
   - Crie uma nova conta ou faça login
   - Clique em "New +" → "Web Service"
   - Faça upload da pasta `deploy/` ou conecte seu repositório Git

3. **Configure o serviço:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Python Version**: 3.11.0

### Opção 2: Deploy Manual

1. **Prepare o ambiente:**
   ```bash
   # Instalar dependências do frontend
   cd frontend/busca-operadoras
   npm install
   npm run build
   
   # Voltar para a raiz
   cd ../..
   ```

2. **Estrutura para deploy:**
   ```
   deploy/
   ├── app.py                 # Backend Flask
   ├── relatorio_cadop.csv    # Dados das operadoras
   ├── dist/                  # Frontend buildado
   ├── requirements.txt       # Dependências Python
   ├── Procfile              # Comando de start
   └── render.yaml           # Configuração do Render
   ```

## 🛠️ Desenvolvimento Local

### Pré-requisitos
- Python 3.7+
- Node.js 16+
- npm

### Executar Localmente

1. **Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

2. **Frontend:**
   ```bash
   cd frontend/busca-operadoras
   npm install
   npm run serve
   ```

3. **Acesse:** http://localhost:8080

## 📊 Estrutura do Projeto

```
├── backend/                    # Servidor Flask
│   ├── app.py                 # API principal
│   ├── relatorio_cadop.csv    # Dados das operadoras
│   └── requirements.txt       # Dependências Python
├── frontend/busca-operadoras/ # Frontend Vue.js
│   ├── src/
│   │   ├── App.vue
│   │   └── components/
│   │       └── BuscaOperadora.vue
│   └── package.json
├── postman/                   # Testes da API
├── deploy.py                  # Script de preparação
├── requirements.txt           # Dependências para deploy
├── Procfile                  # Comando de start
└── render.yaml               # Configuração Render.com
```

## 🔧 API Endpoints

- `GET /buscar?termo={termo}` - Busca operadoras por termo
- `GET /` - Interface web principal

## 📱 Interface

A interface permite:
- Buscar operadoras por razão social ou nome fantasia
- Visualizar dados completos (CNPJ, endereço, contatos)
- Tratamento de dados ausentes
- Design responsivo

## 🚀 Deploy Rápido

Para fazer deploy imediatamente:

1. Execute: `python deploy.py`
2. Faça upload da pasta `deploy/` no Render.com
3. Configure como Web Service
4. Aguarde o deploy automático

---


