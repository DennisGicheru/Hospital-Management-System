<template>
    <div>
        <table>
            <h4>Covid Data</h4>
            <tr>
                <th>iso</th>
                <th>name</th>
            </tr>
            <tr v-for="region in regions" :key="region.id">
                <th>{{name.iso}}</th>
                <th>{{name.name}}</th>
            </tr>
        </table>
        <button @click="showmodal==true">Show Covid Data</button>
    </div>  
</template>


<script>
import axios from 'axios';
import {ref} from 'vue';
export default {
    data(){  
        const showmodal=ref(true)
        const axios = require("axios");

        const options = {
        method: 'GET',
        url: 'https://covid-19-statistics.p.rapidapi.com/reports',
        headers: {
            'X-RapidAPI-Key': '7846b728a6msh42a630fe1a2b933p1fc031jsn2b4a4e8faca5',
            'X-RapidAPI-Host': 'covid-19-statistics.p.rapidapi.com'
        }
        };

        axios.request(options).then(function (response) {
            console.log(response.data);
        }).catch(function (error) {
            console.error(error);
        });
    },
    computed: {
        
    },
    mounted(){
        getRegions:{
            options
        }
    }
}
</script>

<style>

</style>