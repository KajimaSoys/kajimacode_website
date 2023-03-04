<template>

  <Navbar v-if="personal" :frontendUrl="frontendUrl" :text="navbar"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl" :apiEndpoint="apiEndpoint"/>

  <Footer v-if="personal" :frontendUrl="frontendUrl" :text="footer"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/projectsPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";

export default {
  name: "ProjectsView",
  data (){
    return {
      backendUrl: this.$backendUrl,
      frontendUrl: this.$frontendUrl,
      apiEndpoint: "personal",
      personal: true,

      navbar: {},
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
        axios.get(`http://localhost:8000/api/v1/pages/footer/?language=${lang}`)
      ])
      .then(response => {
        this.navbar = response[0].data[0]
        this.footer = response[1].data[0]
      })
      .catch(error => {
        console.log('Ошибка при загрузке локализации')
      })
    }
  },
  beforeMount() {
    // FIXME add language switch
    this.get_text('ru')

    if (window.location.pathname.includes('team')) {
      this.apiEndpoint = 'team'
      this.personal = false
    }
  }
}
</script>

<style scoped>
  .project-container {
    position: static;
  }

 .navbar07_component{
    background-color: transparent;
    backdrop-filter: blur(4px) brightness(50%);
    width: 100vw;
    position: fixed;
  }
</style>