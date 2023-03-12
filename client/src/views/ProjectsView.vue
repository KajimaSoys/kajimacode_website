<template>

  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Navbar v-if="personal" :frontendUrl="frontendUrl" :text="navbar"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl" :apiEndpoint="apiEndpoint"/>

  <Footer v-if="personal" :frontendUrl="frontendUrl" :text="footer"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/projectsPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import store from "../store";
import { useMeta } from 'vue-meta'

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
  setup() {
    useMeta({
      title: window.location.hostname.startsWith('ru.')
          ? 'Мои проекты | KajimaCode'
          : 'My Projects | KajimaCode',
      description: window.location.hostname.startsWith('ru.')
          ? 'Просмотрите список моих последних проектов и узнайте больше о том, как я могу помочь вам создать уникальный веб-сайт для вашего бизнеса.'
          : 'View a list of my latest projects and learn more about how I can help you create a unique website for your business.',
      og: {
        title: window.location.hostname.startsWith('ru.')
          ? 'Мои проекты | KajimaCode'
          : 'My Projects | KajimaCode',
        type: 'website',
        url: 'https://kajimacode.com',
        description: window.location.hostname.startsWith('ru.')
          ? 'Просмотрите список моих последних проектов и узнайте больше о том, как я могу помочь вам создать уникальный веб-сайт для вашего бизнеса.'
          : 'View a list of my latest projects and learn more about how I can help you create a unique website for your business.',
        site_name: 'KajimaCode',
        locale: window.location.hostname.startsWith('ru.')
          ? 'ru_RU'
          : 'en_GB',
        'locale:alternate': window.location.hostname.startsWith('ru.')
          ? 'en_GB'
          : 'ru_RU',
        image: 'https://kajimacode.com/src/assets/images/main_page.png',
        'image:alt': 'This is the main page of the kajimacode.com website. There is a navigation bar at the top, the inscription "I DEVELOP WEBSITES" on the left, and the button "Contact me!" at the bottom. On the right is a 3d object with the site logo.'
      },
      twitter: {
        card: 'summary',
        title: window.location.hostname.startsWith('ru.')
          ? 'Мои проекты | KajimaCode'
          : 'My Projects | KajimaCode',
        description: window.location.hostname.startsWith('ru.')
          ? 'Просмотрите список моих последних проектов и узнайте больше о том, как я могу помочь вам создать уникальный веб-сайт для вашего бизнеса.'
          : 'View a list of my latest projects and learn more about how I can help you create a unique website for your business.',
        image: 'https://kajimacode.com/src/assets/images/main_page.png',
        'image:alt': 'This is the main page of the kajimacode.com website. There is a navigation bar at the top, the inscription "I DEVELOP WEBSITES" on the left, and the button "Contact me!" at the bottom. On the right is a 3d object with the site logo.'
      },
    })
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
  created() {
    this.get_text(this.$store.state.language.language)

    if (window.location.pathname.includes('team')) {
      this.apiEndpoint = 'team'
      this.personal = false
    }

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage'){
        this.get_text(state.language.language)
      }
    })
  },
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