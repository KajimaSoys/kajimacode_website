import {createStore} from 'vuex'
import cookieModule from "./cookie.module";
import languageModule from "./language.module";

export default createStore({
    modules: {
        cookies: cookieModule,
        language: languageModule
    }
})