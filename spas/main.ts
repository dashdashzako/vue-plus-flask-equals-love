import './assets/main.css'
import './assets/colors.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './main-app.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
