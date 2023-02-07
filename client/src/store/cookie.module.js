export default {
  namespaced: true,
  state: {
    hasAcceptedCookies: false
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('hasAcceptedCookies')) {
        state.hasAcceptedCookies = true
      } else {
        state.hasAcceptedCookies = false
      }
    },
    cookieAccept(state){
      state.hasAcceptedCookies = true;
      localStorage.setItem('hasAcceptedCookies', true)
    }
  },
}