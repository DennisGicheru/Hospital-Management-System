<template>
  <div id="app">
    <NavBar />
    <!-- <Patients />
    <CovidData /> -->
    <MainPage />
    <router-view/>  
  </div>
</template>

<script type="text/javascript">
// import Patients from './components/Patients.vue';
// import CovidData from './components/CovidData.vue';
import MainPage from './components/MainPage.vue';
import NavBar from './components/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar,
    MainPage,
    // Patients,
    // CovidData,
    // MainPage,
},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black; 

}
</style>
