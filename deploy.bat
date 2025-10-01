@echo off
echo 🚀 Preparando projeto para deploy no Render.com
echo ================================================

echo 📦 Instalando dependências do frontend...
cd frontend\busca-operadoras
call npm install
if %errorlevel% neq 0 (
    echo ❌ Erro ao instalar dependências do frontend
    pause
    exit /b 1
)

echo 🔨 Fazendo build do frontend...
call npm run build
if %errorlevel% neq 0 (
    echo ❌ Erro ao fazer build do frontend
    pause
    exit /b 1
)

echo 📁 Criando estrutura de deploy...
cd ..\..
if exist deploy rmdir /s /q deploy
mkdir deploy

echo ✅ Copiando arquivos do backend...
copy backend\app.py deploy\
copy backend\relatorio_cadop.csv deploy\

echo ✅ Copiando build do frontend...
xcopy frontend\busca-operadoras\dist deploy\dist\ /e /i

echo ✅ Copiando arquivos de configuração...
copy requirements.txt deploy\
copy Procfile deploy\
copy render.yaml deploy\

echo.
echo ✅ Projeto preparado para deploy!
echo 📁 Pasta 'deploy' criada com todos os arquivos necessários
echo.
echo 📋 Próximos passos:
echo 1. Acesse https://render.com
echo 2. Crie uma conta ou faça login
echo 3. Clique em "New +" → "Web Service"
echo 4. Faça upload da pasta 'deploy' ou conecte seu repositório Git
echo 5. Configure:
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: python app.py
echo    - Python Version: 3.11.0
echo.
pause

