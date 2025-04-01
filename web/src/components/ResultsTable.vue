<template>
  <div class="results-table">
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>Modalidade</th>
            <th>Cidade/UF</th>
            <th>Contato</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in results" :key="result.Registro_ANS">
            <td>{{ result.Razao_Social }}</td>
            <td>{{ result.Nome_Fantasia || 'N/A' }}</td>
            <td>{{ result.Modalidade }}</td>
            <td>{{ result.Cidade }}/{{ result.UF }}</td>
            <td>
              <div>
                <p v-if="result.Telefone">📞 {{ result.Telefone }}</p>
                <p v-if="result.Endereco_eletronico">✉️ {{ result.Endereco_eletronico }}</p>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultsTable",
  props: {
    results: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.results-table .table-container {
  max-height: 400px; /* Limita a altura da tabela */
  overflow-y: auto; /* Habilita rolagem vertical */
  border: 1px solid #dcdcdc; /* Adiciona uma borda ao contêiner */
  border-radius: 8px;
}

.results-table table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
}

.results-table th,
.results-table td {
  border: 1px solid #dcdcdc;
  padding: 10px;
  text-align: left;
}

.results-table th {
  background-color: #8e44ad; /* Roxo escuro */
  color: #fff;
  font-weight: bold;
}

.results-table td {
  color: #2c3e50; /* Texto escuro */
}

.results-table tr:nth-child(even) {
  background-color: #f9f9f9; /* Fundo cinza claro para linhas pares */
}

.results-table tr:nth-child(odd) {
  background-color: #fff; /* Fundo branco para linhas ímpares */
}
</style>