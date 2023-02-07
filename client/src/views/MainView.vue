<template>
  <Navbar/>

  <MainSection :scrollToAnchor="scrollToAnchor"/>

  <CookieBanner/>

  <IntroduceSection/>

  <ProjectSection :scrollToAnchor="scrollToAnchor"/>

  <StagesSection :scrollToAnchor="scrollToAnchor"/>

  <TechnologiesSection :scrollToAnchor="scrollToAnchor"/>

  <ContactSection/>

  <ReviewSection/>

  <Footer :scrollToAnchor="scrollToAnchor"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/mainPage/MainSection.vue";
import CookieBanner from "@/components/CookieBanner.vue";
import IntroduceSection from "@/components/mainPage/IntroduceSection.vue";
import ProjectSection from "@/components/mainPage/ProjectSection.vue";
import StagesSection from "@/components/mainPage/StagesSection.vue";
import TechnologiesSection from "@/components/mainPage/TechnologiesSection.vue";
import ContactSection from "@/components/mainPage/ContactSection.vue";
import ReviewSection from "@/components/mainPage/ReviewSection.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "MainView",
  components: {
    Navbar,
    MainSection,
    CookieBanner,
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
    }
  }
}
</script>

<style>

</style>