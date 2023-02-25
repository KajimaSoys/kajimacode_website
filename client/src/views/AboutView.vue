<template>

  <Navbar :frontendUrl="frontendUrl"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl"/>

  <Footer :frontendUrl="frontendUrl"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/aboutPage/MainSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: 'AboutView',
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
.navbar07_component{
    background-color: transparent;
    backdrop-filter: blur(4px) brightness(50%);
    width: 100vw;
    position: fixed;
  }

  /*.footer04_component {*/
  /*  position: absolute;*/
  /*}*/
</style>
