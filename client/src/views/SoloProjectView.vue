<template>

  <Navbar v-if="personal" :frontendUrl="frontendUrl"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl" :apiEndpoint="apiEndpoint"/>

  <Footer v-if="personal" :frontendUrl="frontendUrl"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/soloProjectPage/MainSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "SoloProjectView",
  data (){
    return {
      backendUrl: this.$backendUrl,
      frontendUrl: this.$frontendUrl,
      apiEndpoint: "personal",
      personal: true
    }
  },
  components: {
    Navbar,
    MainSection,
    Footer,
  },
  beforeMount() {
    if (window.location.pathname.includes('team')) {
      this.apiEndpoint = 'team'
      this.personal = false
    }
  }
}
</script>

<style scoped>

/*  footer {*/
/*    margin-top: 100vh;*/
/*  }*/

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