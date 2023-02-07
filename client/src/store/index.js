import {createStore} from 'vuex'
import cookieModule from "./cookie.module";

export default createStore({
    modules: {
        cookies: cookieModule
    }
})