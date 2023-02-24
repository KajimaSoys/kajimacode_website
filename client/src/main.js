import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";
import axios from "axios";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import SmoothScroll from 'smoothscroll-for-websites'

import './assets/main.css'

const app = createApp(App)

app.use(store)

app.use(router, axios)

app.use(ElementPlus)

app.use(SmoothScroll({
                        animationTime    : 500 ,
                        accelerationDelta : 100,
                        accelerationMax   : 3,
                        touchpadSupport   : true,
                        pulseScale       : 4,
                        pulseNormalize   : 1,
        }))

app.mount('#app')

// local
app.config.globalProperties.$backendUrl= 'http://localhost:8000'
// prod
//app.config.globalProperties.$hostname = 'https://kajimacode.com'

// local
app.config.globalProperties.$frontendUrl= 'http://localhost:5173'
// prod
//app.config.globalProperties.$hostname = 'https://kajimacode.com'

// local
axios.defaults.baseURL = 'http://localhost:8000'
// prod
// axios.defaults.baseURL = 'https://kajimacode.com'

