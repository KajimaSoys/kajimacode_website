<template>

  <Navbar/>

  <MainSection/>

  <Footer/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/projectsPage/MainSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "ProjectsView",
  components: {
    Navbar,
    MainSection,
    Footer,
  }
}
</script>

<style scoped>
  /*main-section {*/
  /*  height: 100vh;*/
  /*}*/

  footer {
    /*position: fixed;*/
    /*bottom: 0;*/
    /*width: 100vw;*/
    margin-top: 100vh;
  }

  .navbar07_component {
    background-color: transparent;
    backdrop-filter: blur(4px) brightness(50%);
  }
</style>