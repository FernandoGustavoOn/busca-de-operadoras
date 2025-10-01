#!/usr/bin/env python3
"""
Script completo para preparar o projeto para deploy no Render.com
"""
import subprocess
import os
import shutil
import sys
import json

def run_command(command, cwd=None):
    """Executa um comando e retorna o resultado"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, capture_output=True, text=True)
        print(f"✅ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar: {command}")
        print(f"Erro: {e.stderr}")
        return False

def check_node_npm():
    """Verifica se Node.js e npm estão instalados"""
    try:
        subprocess.run("node --version", shell=True, check=True, capture_output=True)
        subprocess.run("npm --version", shell=True, check=True, capture_output=True)
        print("✅ Node.js e npm estão instalados")
        return True
    except subprocess.CalledProcessError:
        print("❌ Node.js ou npm não estão instalados!")
        print("Por favor, instale Node.js: https://nodejs.org/")
        return False

def build_frontend():
    """Faz o build do frontend Vue.js"""
    print("🔨 Fazendo build do frontend...")
    
    frontend_dir = "frontend/busca-operadoras"
    
    if not os.path.exists(frontend_dir):
        print(f"❌ Diretório {frontend_dir} não encontrado!")
        return False
    
    # Instalar dependências
    print("📦 Instalando dependências do frontend...")
    if not run_command("npm install", cwd=frontend_dir):
        return False
    
    # Fazer build
    print("🔨 Compilando projeto Vue.js...")
    if not run_command("npm run build", cwd=frontend_dir):
        return False
    
    # Verificar se o build foi criado
    dist_dir = os.path.join(frontend_dir, "dist")
    if not os.path.exists(dist_dir):
        print("❌ Diretório dist não foi criado!")
        return False
    
    print(f"✅ Frontend buildado com sucesso em: {dist_dir}")
    return True

def create_deploy_structure():
    """Cria a estrutura otimizada para deploy"""
    print("📁 Criando estrutura para deploy...")
    
    # Criar diretório de deploy
    if os.path.exists("deploy"):
        shutil.rmtree("deploy")
    os.makedirs("deploy")
    
    # Copiar arquivos do backend
    backend_files = ["app.py", "relatorio_cadop.csv"]
    for file in backend_files:
        if os.path.exists(f"backend/{file}"):
            shutil.copy2(f"backend/{file}", f"deploy/{file}")
            print(f"✅ Copiado: {file}")
    
    # Copiar build do frontend
    if os.path.exists("frontend/busca-operadoras/dist"):
        shutil.copytree("frontend/busca-operadoras/dist", "deploy/dist")
        print("✅ Copiado: dist/ (frontend buildado)")
    
    # Copiar arquivos de configuração
    config_files = ["requirements.txt", "Procfile", "render.yaml"]
    for file in config_files:
        if os.path.exists(file):
            shutil.copy2(file, f"deploy/{file}")
            print(f"✅ Copiado: {file}")
    
    print("✅ Estrutura de deploy criada em: deploy/")
    return True

def main():
    print("🚀 Preparando projeto para deploy no Render.com")
    print("=" * 50)
    
    # Verificar dependências
    if not check_node_npm():
        return False
    
    # Build do frontend
    if not build_frontend():
        return False
    
    # Criar estrutura de deploy
    if not create_deploy_structure():
        return False
    
    print("\n" + "=" * 50)
    print("✅ Projeto preparado para deploy!")
    print("\n📋 Próximos passos:")
    print("1. Faça upload da pasta 'deploy/' para o Render.com")
    print("2. Ou conecte seu repositório Git ao Render.com")
    print("3. Configure as variáveis de ambiente se necessário")
    print("\n📁 Arquivos prontos para deploy:")
    print("- deploy/app.py (backend)")
    print("- deploy/relatorio_cadop.csv (dados)")
    print("- deploy/dist/ (frontend buildado)")
    print("- deploy/requirements.txt (dependências)")
    print("- deploy/Procfile (comando de start)")
    print("- deploy/render.yaml (configuração do Render)")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
