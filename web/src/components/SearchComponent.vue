<template>
  <div>
    <SearchBar :query="query" @search="search" />

    <ResultsTable v-if="results.length > 0" :results="results" />

    <!-- Mensagem quando não há resultados -->
    <div v-else-if="query.trim()" class="no-results">
      Nenhum resultado encontrado para "{{ query }}".
    </div>
  </div>
</template>

<script>
import SearchBar from "./SearchBar.vue";
import ResultsTable from "./ResultsTable.vue";

export default {
  components: {
    SearchBar,
    ResultsTable,
  },
  data() {
    return {
      query: "",
      results: [],
    };
  },
  methods: {
    async search(query) {
      this.query = query; // Atualiza o valor de query no pai
      if (!this.query.trim()) {
        alert("Por favor, insira um termo de busca.");
        return;
      }

      try {
        const response = await fetch(`http://127.0.0.1:5000/search?q=${this.query}`);
        if (!response.ok) {
          throw new Error(`Erro ${response.status}: ${response.statusText}`);
        }
        this.results = await response.json();
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
        alert("Ocorreu um erro ao buscar os dados. Verifique o console para mais detalhes.");
      }
    },
  },
};
</script>

<style scoped>
/* Mensagem de nenhum resultado */
.no-results {
  text-align: center;
  font-size: 18px;
  color: #8e44ad; /* Roxo escuro */
  margin-top: 20px;
}
</style>