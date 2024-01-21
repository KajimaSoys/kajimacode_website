import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";
import axios from "axios";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import SmoothScroll from 'smoothscroll-for-websites'
import { createMetaManager } from 'vue-meta'

import './assets/main.css'

const domain = window.location.hostname;
let language = 'en';

if (domain.startsWith('ru.')) {
  language = 'ru';
}

store.commit('language/setLanguage', language)

const app = createApp(App)

app.use(store)
app.use(router, axios)
app.use(ElementPlus)
app.use(createMetaManager())
app.use(SmoothScroll({
                        animationTime    : 400 ,
                        accelerationDelta : 100,
                        accelerationMax   : 3,
                        touchpadSupport   : true,
                        pulseScale       : 4,
                        pulseNormalize   : 1,
        }))
app.mount('#app')


let backendURL = import.meta.env.VITE_BACKEND_HOST;
let frontendURL = import.meta.env.VITE_FRONTEND_HOST;

axios.defaults.baseURL = backendURL
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

app.provide('backendURL', backendURL)
app.provide('frontendURL', frontendURL)


app.config.globalProperties.$projectVersion = '2.9.4'

