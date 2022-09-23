import { createApp, VueElement } from 'vue'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import './assets/tailwind.css'

createApp(App).use(store).mount('#app')

VueElement.prototype.$http = axios;