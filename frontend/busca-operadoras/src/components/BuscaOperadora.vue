<template>
    <div>
      <h1>Buscar Operadoras</h1>
      <input v-model="termo" placeholder="Digite um termo para buscar..." />
      <button @click="buscarOperadoras">Buscar</button>
  
      <!-- Exibe mensagem quando nenhum resultado for encontrado -->
      <p v-if="mensagem" style="color: red;">{{ mensagem }}</p>
  
      <!-- Lista os resultados -->
      <ul v-else>
        <li v-for="operadora in operadoras" :key="operadora.Registro_ANS">
            <div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;">
                <p><strong>Razão Social:</strong> {{ operadora.Razao_Social || "Indisponível" }}</p>
                <p><strong>Nome Fantasia:</strong> {{ operadora.Nome_Fantasia || "Indisponível" }}</p>
                <p><strong>Cidade:</strong> {{ operadora.Cidade || "Indisponível" }}</p>
                <p><strong>UF:</strong> {{ operadora.UF || "Indisponível" }}</p>
                <p><strong>Registro ANS:</strong> {{ operadora.Registro_ANS || "Indisponível" }}</p>
            </div>
        </li>
  </ul>
    </div>
  </template>
  
  
  
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
  return {
    termo: '',
    operadoras: [],
    mensagem: '' // Para mensagens de erro ou aviso
  };
},
    methods: {
      async buscarOperadoras() {
        try {
        const baseURL = process.env.VUE_APP_API_URL || '';
        const resposta = await axios.get(`${baseURL}/buscar`, { params: { termo: this.termo } });

        console.log("Resposta completa:", resposta);
        console.log("Dados no campo data:", resposta.data);
        console.log("Tipo de resposta.data:", typeof resposta.data);
        console.log("Conteúdo de resposta.data:", resposta.data);
        console.log("Dados recebidos da API:", this.operadoras);

        // Verifica se há uma mensagem de "Nenhum resultado encontrado"
        if (resposta.data.mensagem) {
            this.operadoras = []; // Limpa a lista
            this.mensagem = resposta.data.mensagem; // Exibe a mensagem
        }else {
            this.operadoras = resposta.data;
            this.mensagem = ''; // Limpa a mensagem
        }
  } catch (error) {
    console.error("Erro ao buscar operadoras:", error);

        }
      }
    }
  };
  </script>
  
  <style scoped>
  input {
    margin-right: 10px;
  }
  </style>
  