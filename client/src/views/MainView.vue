<template>
      <Navbar :frontendUrl="frontendUrl" :text="navbar"/>

      <MainSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl" :text="mainPage"/>

      <IntroduceSection :frontendUrl="frontendUrl" :text="mainPage"/>

      <ProjectSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl" :text="mainPage"/>

      <StagesSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl" :text="mainPage"/>

      <TechnologiesSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl" :text="mainPage"/>

      <ContactSection :text="mainPage"/>

      <ReviewSection :frontendUrl="frontendUrl" :text="mainPage"/>

      <Footer :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl" :text="footer"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/mainPage/MainSection.vue";
import IntroduceSection from "@/components/mainPage/IntroduceSection.vue";
import ProjectSection from "@/components/mainPage/ProjectSection.vue";
import StagesSection from "@/components/mainPage/StagesSection.vue";
import TechnologiesSection from "@/components/mainPage/TechnologiesSection.vue";
import ContactSection from "@/components/mainPage/ContactSection.vue";
import ReviewSection from "@/components/mainPage/ReviewSection.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import store from "../store";
// TODO make back to top component
// TODO make navbar sticky
// TODO make IntoduceSection going up when scroll instead of MainSection
// TODO All objects should appear with animation using scrolling

export default {
  name: "MainView",
  data (){
    return {
      frontendUrl: this.$frontendUrl,

      navbar: {},
      mainPage: {},
      footer: {},
    }
  },
  components: {
    Navbar,
    MainSection,
    IntroduceSection,
    ProjectSection,
    StagesSection,
    TechnologiesSection,
    ContactSection,
    ReviewSection,
    Footer,
  },

  methods: {
    scrollToAnchor(anchor) {
      const target = document.querySelector(`#${anchor}`);
      target.scrollIntoView({behavior: "smooth"});
    },

    get_text(lang){
      Promise.all([
          axios.get(`http://localhost:8000/api/v1/pages/navbar/?language=${lang}`),
          axios.get(`http://localhost:8000/api/v1/pages/main/?language=${lang}`),
          axios.get(`http://localhost:8000/api/v1/pages/footer/?language=${lang}`)
        ])
        .then(response => {
          this.navbar = response[0].data[0]
          this.mainPage = response[1].data[0]
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

</style>