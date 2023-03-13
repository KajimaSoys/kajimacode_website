<template>
      <metainfo>
        <template v-slot:title="{ content, metainfo }">{{ content }}</template>
      </metainfo>

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
import { useMeta } from 'vue-meta'
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
  setup() {
    let ru = window.location.hostname.startsWith('ru.')
    useMeta({
      title: ru
          ? 'KajimaCode | Создание инновационных и качественных веб-сайтов'
          : 'KajimaCode | Building Innovative and High-Quality Websites',
      description: ru
          ? 'KajimaCode - это компания, специализирующаяся на полном цикле разработки веб-сайтов, готовая воплотить ваши уникальные идеи в жизнь с помощью наших навыков в программировании и дизайне. Мы создаем инновационные и качественные веб-сайты, которые будут соответствовать вашим потребностям и привлекать новых клиентов.'
          : 'KajimaCode is a full-service web development company specializing in creating innovative and high-quality websites. Let us bring your digital vision to life with our expertise in coding and design.',
      og: {
        title: ru
          ? 'KajimaCode | Создание инновационных и качественных веб-сайтов'
          : 'KajimaCode | Building Innovative and High-Quality Websites',
        type: 'website',
        url: ru
          ? 'https://ru.kajimacode.com'
          : 'https://kajimacode.com',
        description: ru
          ? 'KajimaCode - это компания, специализирующаяся на полном цикле разработки веб-сайтов, готовая воплотить ваши уникальные идеи в жизнь с помощью наших навыков в программировании и дизайне. Мы создаем инновационные и качественные веб-сайты, которые будут соответствовать вашим потребностям и привлекать новых клиентов.'
          : 'KajimaCode is a full-service web development company specializing in creating innovative and high-quality websites. Let us bring your digital vision to life with our expertise in coding and design.',
        site_name: 'KajimaCode',
        locale: ru
          ? 'ru_RU'
          : 'en_GB',
        'locale:alternate': ru
          ? 'en_GB'
          : 'ru_RU',
        image: 'https://kajimacode.com/src/assets/images/main_page.png',
        'image:alt': 'This is the main page of the kajimacode.com website. There is a navigation bar at the top, the inscription "I DEVELOP WEBSITES" on the left, and the button "Contact me!" at the bottom. On the right is a 3d object with the site logo.'
      },
      twitter: {
        card: 'summary',
        site: ru
          ? 'https://ru.kajimacode.com'
          : 'https://kajimacode.com',
        title: ru
          ? 'KajimaCode | Создание инновационных и качественных веб-сайтов'
          : 'KajimaCode | Building Innovative and High-Quality Websites',
        description: ru
          ? 'KajimaCode - это компания, специализирующаяся на полном цикле разработки веб-сайтов, готовая воплотить ваши уникальные идеи в жизнь с помощью наших навыков в программировании и дизайне. Мы создаем инновационные и качественные веб-сайты, которые будут соответствовать вашим потребностям и привлекать новых клиентов.'
          : 'KajimaCode is a full-service web development company specializing in creating innovative and high-quality websites. Let us bring your digital vision to life with our expertise in coding and design.',
        image: 'https://kajimacode.com/src/assets/images/main_page.png',
        'image:alt': 'This is the main page of the kajimacode.com website. There is a navigation bar at the top, the inscription "I DEVELOP WEBSITES" on the left, and the button "Contact me!" at the bottom. On the right is a 3d object with the site logo.'
      },
      link: [
        {rel: 'canonical', href: ru ? 'https://ru.kajimacode.com' : 'https://kajimacode.com'}
      ]
    })
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
    this.get_text(this.$store.state.language.language)

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage'){
        this.get_text(state.language.language)
      }
    })
  },
}
</script>

<style scoped>

</style>