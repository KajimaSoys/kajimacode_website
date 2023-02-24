<template>

  <Navbar :backendUrl="backendUrl" :frontendUrl="frontendUrl"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl"/>

  <Footer :backendUrl="backendUrl" :frontendUrl="frontendUrl"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/projectsPage/MainSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "ProjectsView",
  data (){
    return {
      backendUrl: this.$backendUrl,
      frontendUrl: this.$frontendUrl,
    }
  },
  components: {
    Navbar,
    MainSection,
    Footer,
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