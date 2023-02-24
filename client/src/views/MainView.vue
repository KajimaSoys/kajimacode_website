<template>
      <Navbar :frontendUrl="frontendUrl"/>

      <MainSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl"/>

      <IntroduceSection :frontendUrl="frontendUrl"/>

      <ProjectSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl"/>

      <StagesSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl"/>

      <TechnologiesSection :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl"/>

      <ContactSection/>

      <ReviewSection :frontendUrl="frontendUrl"/>

      <Footer :scrollToAnchor="scrollToAnchor" :frontendUrl="frontendUrl"/>

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
// TODO make back to top component
// TODO make navbar sticky
// TODO make IntoduceSection going up when scroll instead of MainSection
// TODO All objects should appear with animation using scrolling

export default {
  name: "MainView",
  data (){
    return {
      frontendUrl: this.$frontendUrl,
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
    }
  },

  // mounted() {
  //   document.addEventListener('wheel', event => {
  //     event.preventDefault();
  //
  //     console.log(event)
  //     const delta = event.deltaY;
  //     const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  //
  //     // window.requestAnimationFrame(() => {
  //     //   document.documentElement.scrollTop = scrollTop + delta * 5;
  //     //   document.body.scrollTop = scrollTop + delta * 5;
  //     // });
  //   }, {passive:false});
  // }
  // directives: {
  //   smoothScroll: {
  //     inserted(el) {
  //       function smoothScroll(e) {
  //
  //         e.preventDefault();
  //         const delta = Math.max(-1, Math.min(1, e.wheelDelta || -e.detail));
  //         const scrollTop = el.scrollTop;
  //         window.requestAnimationFrame(() => {
  //           el.scrollTop = scrollTop + delta * 30;
  //         });
  //       }
  //       el.addEventListener('mousewheel', smoothScroll, { passive: false });
  //       el.addEventListener('DOMMouseScroll', smoothScroll, { passive: false });
  //     },
  //     unbind(el) {
  //       el.removeEventListener('mousewheel', smoothScroll);
  //       el.removeEventListener('DOMMouseScroll', smoothScroll);
  //     }
  //   }
  // }
}
</script>

<style scoped>
  /*.navbar07_component:deep(.footer04_social-link:hover)  {*/
  /*  color: #ffffff!important;*/
  /*}*/

  /*.navbar07_component:deep(.footer04_social-link)  {*/
  /*  color: #cdd1d8!important;*/

  /*}*/

  /*#scroll-area {*/
  /*  width: 500px;*/
  /*  height: 500px;*/
  /*}*/

  /*#content {*/
  /*  width: 2000px;*/
  /*  height: 2000px;*/
  /*}*/
</style>