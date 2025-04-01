<template>
  <div class="search-bar">
    <input
      v-model="localQuery"
      type="text"
      placeholder="Digite o termo de busca"
      @keyup.enter="emitSearch"
    />
    <button @click="emitSearch">Buscar</button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  props: {
    query: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      localQuery: this.query, // Inicializa com o valor da prop
    };
  },
  methods: {
    emitSearch() {
      this.$emit("search", this.localQuery); // Emite o valor atualizado para o pai
    },
  },
};
</script>

<style scoped>
.search-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-bar input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  outline: none;
}

.search-bar input:focus {
  border-color: #8e44ad; /* Roxo escuro */
  box-shadow: 0 0 4px rgba(142, 68, 173, 0.5);
}

.search-bar button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #8e44ad; /* Roxo escuro */
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-bar button:hover {
  background-color: #732d91; /* Roxo mais escuro */
}
</style>