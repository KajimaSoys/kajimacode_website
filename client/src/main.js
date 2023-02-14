import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";
import axios from "axios";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import SmoothScroll from 'smoothscroll-for-websites'

import './assets/main.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

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
