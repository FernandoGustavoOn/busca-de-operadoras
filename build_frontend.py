#!/usr/bin/env python3
"""
Script para fazer build do frontend Vue.js
"""
import subprocess
import os
import shutil
import sys

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

def main():
    print("🚀 Iniciando build do frontend...")
    
    # Navegar para o diretório do frontend
    frontend_dir = "frontend/busca-operadoras"
    
    if not os.path.exists(frontend_dir):
        print(f"❌ Diretório {frontend_dir} não encontrado!")
        return False
    
    # Instalar dependências
    print("📦 Instalando dependências...")
    if not run_command("npm install", cwd=frontend_dir):
        return False
    
    # Fazer build do projeto
    print("🔨 Fazendo build do projeto...")
    if not run_command("npm run build", cwd=frontend_dir):
        return False
    
    # Verificar se o build foi criado
    dist_dir = os.path.join(frontend_dir, "dist")
    if not os.path.exists(dist_dir):
        print("❌ Diretório dist não foi criado!")
        return False
    
    print("✅ Build do frontend concluído com sucesso!")
    print(f"📁 Arquivos gerados em: {dist_dir}")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
