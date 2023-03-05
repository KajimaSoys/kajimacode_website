<template>

  <Navbar :frontendUrl="frontendUrl" :text="navbar"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl" :text="privacyPage"/>

  <Footer :frontendUrl="frontendUrl" :text="footer"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/privacyPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import store from "../store";

export default {
  name: "PrivacyView",
  data (){
    return {
      backendUrl: this.$backendUrl,
      frontendUrl: this.$frontendUrl,

      navbar: {},
      privacyPage: {},
      footer: {},
    }
  },
  components: {
    Navbar,
    MainSection,
    Footer,
  },
  methods: {
    get_text(lang){

    Promise.all([
        axios.get(`http://localhost:8000/api/v1/pages/navbar/?language=${lang}`),
        axios.get(`http://localhost:8000/api/v1/pages/privacy/?language=${lang}`),
        axios.get(`http://localhost:8000/api/v1/pages/footer/?language=${lang}`)
      ])
      .then(response => {
        this.navbar = response[0].data[0]
        this.privacyPage = response[1].data[0]
        this.footer = response[2].data[0]
      })
      .catch(error => {
        console.log('Ошибка при загрузке локализации')
      })
    }
  },
  created() {
    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage'){
        this.get_text(state.language.language)
      }
    })
  },
  beforeMount() {
    this.get_text(this.$store.state.language.language)
  }
}
</script>

<style scoped>
.navbar07_component{
    background-color: transparent;
    backdrop-filter: blur(4px) brightness(50%);
    width: 100vw;
    position: fixed;
  }
</style>