/* eslint-disable */
<template>
 <div>
    <div class="add_patient" v-show="showdata">
        <form v-on:submit.prevent="submitForm">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" v-model="name"/>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="text" class="form-control" id="email" v-model="email"/>
            </div>
            <div class="form-group">
                <label for="gender">Gender:</label>
                <input type="text" class="form-control" id="gender" v-model="gender"/>
            </div>
            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="number" class="form-control" id="phone" v-model="phone"/>
            </div>
            <div class="form-group">
                <label for="address">Address</label>
                <textarea class="form-control" id="address" v-model="address"></textarea>
            </div>
            <div class="form-group">
                <label for="birthdate">Date of Birth</label>
                <input type="date" class="form-control" id="birthdate" v-model="birthdate"/>
            </div>
            <div class="form-group">
                <button type="submit">Add Patient</button>
            </div>
        </form>
    </div>
    <div class="patient_container">
        <h1>Patient Details</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Gender</th>
                <th>phone</th>
                <th>Address</th>
                <th>Date of Birth</th>

            </tr>
            <tr v-for="patient in patients" :key="patient.id">
                <td>{{patient.name}}</td>
                <td>{{patient.email}}</td>
                <td>{{patient.gender}}</td>
                <td>{{patient.phone}}</td>
                <td>{{patient.address}}</td>
                <td>{{patient.birthdate}}</td>
            </tr>
        </table>
    </div>
    <CovidData v-show="Showdata = false" />

 </div>
    
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            patients: [],
            name: '',
            email: '',
            gender: '',
            phone: '',
            address: '',
            birthdate: ''
        }
    },
    methods: {
        async getData() {
            try {
                // fetch patient data
                const response = await axios.get('http://localhost:8000/api/hmswebapp/');
                // set the returned data as patient data;
                this.patients = response.data;
            } catch (error) {
                //log the error
                console.log(error)
            }
        },
        async submitForm() {
            try {
                const response = await axios.post('http://localhost:8000/api/hmswebapp/', {
                name: this.name,
                email: this.email,
                gender: this.gender,
                phone: this.phone,
                address: this.address,
                birthdate: this.birthdate
                });
                // appending the returned data to the patients array
                this.patients.push(response.data);
                //reset the field values after that
                this.name = '';
                this.email = '';
                this.gender = '';
                this.phone = '';
                this.address = '';
                this.birthdate = '';
            }
            catch(error) {
                //log error
                console.log(error)
            }
        },
        
    },
    created() {
        // fetch patient data on page load
        this.getData();
    }
}
</script>

<style>

</style>