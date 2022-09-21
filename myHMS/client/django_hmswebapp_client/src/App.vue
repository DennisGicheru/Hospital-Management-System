<template>
  <div id="app">
    <Patients />
    <CovidData />
  
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Patients from './components/Patients.vue';
import CovidData from './components/CovidData.vue';
export default {
  name: 'App',
  components: {
    Patients,
    CovidData
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
</style>
