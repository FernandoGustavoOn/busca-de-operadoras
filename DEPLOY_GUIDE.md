# 🚀 Guia de Deploy no Render.com

## ⚡ Deploy Rápido (5 minutos)

### 1. Preparar o Projeto

**Opção A - Script Automático (Windows):**
```bash
deploy.bat
```

**Opção B - Manual:**
```bash
# 1. Instalar dependências do frontend
cd frontend/busca-operadoras
npm install
npm run build

# 2. Criar pasta deploy
cd ../..
mkdir deploy

# 3. Copiar arquivos
copy backend/app.py deploy/
copy backend/relatorio_cadop.csv deploy/
copy frontend/busca-operadoras/dist deploy/dist
copy requirements.txt deploy/
copy Procfile deploy/
copy render.yaml deploy/
```

### 2. Deploy no Render.com

1. **Acesse:** https://render.com
2. **Crie conta** ou faça login
3. **Clique em:** "New +" → "Web Service"
4. **Escolha uma opção:**
   - **Opção A:** Conecte seu repositório Git
   - **Opção B:** Faça upload da pasta `deploy/`

### 3. Configuração

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`
- **Python Version:** `3.11.0`
- **Plan:** Free

### 4. Aguardar Deploy

- O Render fará o build automaticamente
- Aguarde 2-5 minutos
- Sua aplicação estará disponível em: `https://seu-app.onrender.com`

## 🔧 Configurações Avançadas

### Variáveis de Ambiente (Opcional)
```
PYTHON_VERSION=3.11.0
FLASK_ENV=production
```

### Domínio Personalizado (Opcional)
- Vá em Settings → Custom Domains
- Adicione seu domínio personalizado

## 🐛 Solução de Problemas

### Erro: "Module not found"
- Verifique se todas as dependências estão no `requirements.txt`
- Execute: `pip install -r requirements.txt` localmente

### Erro: "Port already in use"
- O Render define a porta automaticamente
- Use: `port = int(os.environ.get('PORT', 5000))`

### Erro: "Build failed"
- Verifique se o Node.js está instalado para build do frontend
- Execute o build localmente primeiro

### Frontend não carrega
- Verifique se a pasta `dist/` foi copiada corretamente
- Confirme se o Flask está servindo arquivos estáticos

## 📊 Monitoramento

- **Logs:** Disponível no dashboard do Render
- **Métricas:** CPU, RAM, requests
- **Uptime:** Monitoramento automático

## 💰 Custos

- **Plano Free:** 750 horas/mês
- **Limitações:** App "dorme" após 15min de inatividade
- **Upgrade:** $7/mês para plano pago (sempre ativo)

## 🚀 Próximos Passos

1. **Teste a aplicação** após o deploy
2. **Configure domínio personalizado** (opcional)
3. **Monitore performance** no dashboard
4. **Configure backup** se necessário

---

**🎉 Parabéns! Sua aplicação está no ar!**
