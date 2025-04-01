<template>
  <div id="app">
    <header>
      <h1>Busca de Operadoras</h1>
    </header>
    <main>
      <SearchComponent />
    </main>
  </div>
</template>

<script>
import SearchComponent from './components/SearchComponent.vue';

export default {
  name: 'App',
  components: {
    SearchComponent,
  },
};
</script>

<style>
/* Estilos globais */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
}

header {
  text-align: center;
  padding: 20px;
  background-color: #f3e5f5; /* Fundo roxo claro */
  color: #8e44ad; /* Roxo escuro */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

main {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
