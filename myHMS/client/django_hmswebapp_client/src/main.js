import { createApp, VueElement } from 'vue'
import App from './App.vue'
import axios from 'axios'

createApp(App).mount('#app')

VueElement.prototype.$http = axios;