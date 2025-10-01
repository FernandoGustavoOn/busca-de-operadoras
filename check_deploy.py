#!/usr/bin/env python3
"""
Script para verificar se o projeto está pronto para deploy
"""
import os
import sys

def check_file_exists(filepath, description):
    """Verifica se um arquivo existe"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - ARQUIVO NÃO ENCONTRADO")
        return False

def check_directory_exists(dirpath, description):
    """Verifica se um diretório existe"""
    if os.path.exists(dirpath):
        print(f"✅ {description}: {dirpath}")
        return True
    else:
        print(f"❌ {description}: {dirpath} - DIRETÓRIO NÃO ENCONTRADO")
        return False

def main():
    print("🔍 Verificando se o projeto está pronto para deploy...")
    print("=" * 60)
    
    all_good = True
    
    # Verificar arquivos do backend
    print("\n📁 Backend:")
    all_good &= check_file_exists("backend/app.py", "App Flask")
    all_good &= check_file_exists("backend/relatorio_cadop.csv", "Dados CSV")
    all_good &= check_file_exists("backend/requirements.txt", "Dependências Python")
    
    # Verificar arquivos do frontend
    print("\n🌐 Frontend:")
    all_good &= check_directory_exists("frontend/busca-operadoras", "Projeto Vue.js")
    all_good &= check_file_exists("frontend/busca-operadoras/package.json", "Package.json")
    all_good &= check_file_exists("frontend/busca-operadoras/src/components/BuscaOperadora.vue", "Componente principal")
    
    # Verificar arquivos de configuração
    print("\n⚙️ Configuração:")
    all_good &= check_file_exists("requirements.txt", "Requirements.txt (raiz)")
    all_good &= check_file_exists("Procfile", "Procfile")
    all_good &= check_file_exists("render.yaml", "Render.yaml")
    all_good &= check_file_exists("runtime.txt", "Runtime.txt")
    
    # Verificar scripts de deploy
    print("\n🚀 Scripts de Deploy:")
    all_good &= check_file_exists("deploy.py", "Script Python")
    all_good &= check_file_exists("deploy.bat", "Script Windows")
    all_good &= check_file_exists("DEPLOY_GUIDE.md", "Guia de Deploy")
    
    print("\n" + "=" * 60)
    
    if all_good:
        print("🎉 PROJETO PRONTO PARA DEPLOY!")
        print("\n📋 Próximos passos:")
        print("1. Execute: deploy.bat (Windows) ou python deploy.py")
        print("2. Acesse: https://render.com")
        print("3. Faça upload da pasta 'deploy/'")
        print("4. Configure como Web Service")
        print("5. Aguarde o deploy automático")
    else:
        print("❌ ALGUNS ARQUIVOS ESTÃO FALTANDO!")
        print("Verifique os arquivos marcados com ❌ acima")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

