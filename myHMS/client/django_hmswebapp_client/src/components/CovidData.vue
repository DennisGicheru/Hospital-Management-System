<template>
    <div class="flex flex-col">
        <div>
            <table>
                <h4 class="bg-red">Covid Data</h4>
                <tr>
                    <th>iso</th>
                    <th>name</th>
                </tr>
                <tr v-for="data in coviddata" :key="data.id">
                    <th>{{data.data.region}}</th>
                    <th>{{data.data.iso}}</th>
                </tr>
            </table>
        </div>
        <button>Close Panel</button>
    </div>  
</template>


<script>
import { useStore } from 'vuex';
import {ref, onMounted, computed} from 'vue';
export default {
    setup() {
        const store = useStore()

        const coviddata = computed(() => {
            return store.state.coviddata
        })

        onMounted(() => {
            store.dispatch('fetchData')
        })
    }
    // data(){  
    //     const showmodal=ref(true)
    //     const axios = require("axios");
    //     // var mykey = config.API_KEY;

    //     const options = {
    //     method: 'GET',
    //     url: 'https://covid-19-statistics.p.rapidapi.com/reports',
    //     headers: {
    //         'X-RapidAPI-Key': '7846b728a6msh42a630fe1a2b933p1fc031jsn2b4a4e8faca5',
    //         'X-RapidAPI-Host': 'covid-19-statistics.p.rapidapi.com'
    //     }
    //     };

    //     axios.request(options).then(function (response) {
    //         console.log(response.data);
    //     }).catch(function (error) {
    //         console.error(error);
    //     });
    // },
    // computed: {
        
    // },
    // mounted(){
    //     getRegions:{
    //         options
    //     }
    // }
}
</script>

<style>

</style>