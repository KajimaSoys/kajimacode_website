<template>

  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Navbar v-if="personal" :text="navbar"/>

  <MainSection :apiEndpoint="apiEndpoint" :text="projectsPage"/>

  <Footer v-if="personal" :text="footer"/>

<!--  <Rate source="soloproj"/>-->

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/soloProjectPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import Rate from "@/components/Rate.vue";
import axios from "axios";
import store from "../store";
import {useMeta} from 'vue-meta'

export default {
  name: "SoloProjectView",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  data() {
    return {
      apiEndpoint: "True",
      personal: true,

      navbar: {},
      projectsPage: {},
      footer: {},
    }
  },
  setup() {
    let ru = window.location.hostname.startsWith('ru.')
    useMeta({
      title: ru
          ? 'Мои проекты | KajimaCode'
          : 'My Projects | KajimaCode',
      description: ru
          ? 'Просмотрите список моих последних проектов и узнайте больше о том, как я могу помочь вам создать уникальный веб-сайт для вашего бизнеса.'
          : 'View a list of my latest projects and learn more about how I can help you create a unique website for your business.',
      keywords: ru
          ? 'KajimaCode, веб-разработка, создание сайтов, Django, Vue.js, full stack разработчик, Python, FastAPI, JavaScript, PostgreSQL, RabbitMQ, Docker, Nginx, Apache, Aiogram, Telethon, разработка на заказ'
          : 'KajimaCode, web development, website creation, Django, Vue.js, full stack developer, Python, FastAPI, JavaScript, PostgreSQL, RabbitMQ, Docker, Nginx, Apache, Aiogram, Telethon, custom development',
      og: {
        title: ru
            ? 'Мои проекты | KajimaCode'
            : 'My Projects | KajimaCode',
        type: 'website',
        url: ru
            ? 'https://ru.kajimacode.ru/projects'
            : 'https://kajimacode.ru/projects',
        description: ru
            ? 'Просмотрите список моих последних проектов и узнайте больше о том, как я могу помочь вам создать уникальный веб-сайт для вашего бизнеса.'
            : 'View a list of my latest projects and learn more about how I can help you create a unique website for your business.',
        site_name: 'KajimaCode',
        locale: ru
            ? 'ru_RU'
            : 'en_GB',
        'locale:alternate': ru
            ? 'en_GB'
            : 'ru_RU',
        image: 'https://kajimacode.ru/images/meta-img.png',
        'image:alt': 'This is the main page of the kajimacode.ru website. There is a navigation bar at the top, the inscription "I DEVELOP WEBSITES" on the left, and the button "Contact me!" at the bottom. On the right is a 3d object with the site logo.'
      },
      twitter: {
        card: 'summary',
        site: ru
            ? 'https://ru.kajimacode.ru/projects'
            : 'https://kajimacode.ru/projects',
        title: ru
            ? 'Мои проекты | KajimaCode'
            : 'My Projects | KajimaCode',
        description: ru
            ? 'Просмотрите список моих последних проектов и узнайте больше о том, как я могу помочь вам создать уникальный веб-сайт для вашего бизнеса.'
            : 'View a list of my latest projects and learn more about how I can help you create a unique website for your business.',
        image: 'https://kajimacode.ru/images/meta-img.png',
        'image:alt': 'This is the main page of the kajimacode.ru website. There is a navigation bar at the top, the inscription "I DEVELOP WEBSITES" on the left, and the button "Contact me!" at the bottom. On the right is a 3d object with the site logo.'
      },
      link: [
        {rel: 'canonical', href: ru ? 'https://ru.kajimacode.ru' : 'https://kajimacode.ru'}
      ]
    })
  },
  components: {
    Navbar,
    MainSection,
    Footer,
    Rate,
  },
  methods: {
    get_text(lang) {

      Promise.all([
        axios.get(`${this.backendURL}/api/v1/pages/navbar/?language=${lang}`),
        axios.get(`${this.backendURL}/api/v1/pages/projects/?language=${lang}`),
        axios.get(`${this.backendURL}/api/v1/pages/footer/?language=${lang}`)
      ])
          .then(response => {
            this.navbar = response[0].data[0]
            this.projectsPage = response[1].data[0]
            this.footer = response[2].data[0]

            window.ym(96212078, 'hit', window.location.href);
          })
          .catch(error => {
            console.log('Ошибка при загрузке локализации')
            console.log('retrying..')
            setTimeout(() => {
              this.get_text()
            }, 3000)
          })
    }
  },
  created() {
    this.get_text(this.$store.state.language.language)

    if (window.location.pathname.includes('team')) {
      this.apiEndpoint = 'False'
      this.personal = false
    }

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage') {
        this.get_text(state.language.language)
      }
    })
  },
  beforeMount() {

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


.navbar07_component {
  background-color: transparent;
  backdrop-filter: blur(4px) brightness(50%);
  -webkit-backdrop-filter: blur(4px) brightness(50%);
  width: 100vw;
  position: fixed;
}


</style>