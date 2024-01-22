import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";
import axios from "axios";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import SmoothScroll from 'smoothscroll-for-websites'
import {createMetaManager} from 'vue-meta'

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
    animationTime: 400,
    accelerationDelta: 100,
    accelerationMax: 3,
    touchpadSupport: true,
    pulseScale: 4,
    pulseNormalize: 1,
}))

router.isReady().then(() => {
    app.mount('#app')

    window.ym = window.ym || function () {
        (window.ym.a = window.ym.a || []).push(arguments)
    }
    window.ym.l = 1 * new Date()
    ym(96212078, 'init', {
        clickmap: true,
        trackLinks: true,
        accurateTrackBounce: true,
        // webvisor: true,
    })

    let script = document.createElement('script')
    script.type = 'text/javascript'
    script.async = true
    script.src = 'https://mc.yandex.ru/metrika/tag.js'
    let firstScript = document.getElementsByTagName('script')[0]
    firstScript.parentNode.insertBefore(script, firstScript)
})


let backendURL = import.meta.env.VITE_BACKEND_HOST;
let frontendURL = import.meta.env.VITE_FRONTEND_HOST;

axios.defaults.baseURL = backendURL
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

app.provide('backendURL', backendURL)
app.provide('frontendURL', frontendURL)


app.config.globalProperties.$projectVersion = '3.4.0'

