<template>
  <div>
    <Fach></Fach>
  </div>
</template>

<script>
import Fach from "./components/Fach.vue"

export default {
  name: "App",
  components: {
    Fach
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
