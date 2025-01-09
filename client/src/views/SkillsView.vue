<template>

  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Navbar :text="navbar"/>

  <MainSection :text="skillsPage"/>

  <Footer :text="footer"/>

<!--  <Rate source="skills"/>-->

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/skillsPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import Rate from "@/components/Rate.vue";
import axios from "axios";
import store from "../store";
import {useMeta} from 'vue-meta'

export default {
  name: "SkillsView",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  data() {
    return {
      navbar: {},
      skillsPage: {},
      footer: {},
    }
  },
  setup() {
    let ru = window.location.hostname.startsWith('ru.')
    useMeta({
      title: ru
          ? 'Мои навыки | KajimaCode'
          : 'My Skills | KajimaCode',
      description: ru
          ? 'Здесь я рассказываю о своих навыках веб-разработки и дизайна. Узнайте, как я могу помочь вашему бизнесу.'
          : 'Here I talk about my web development and design skills. Find out how I can help your business.',
      keywords: ru
          ? 'KajimaCode, веб-разработка, создание сайтов, Django, Vue.js, full stack разработчик, Python, FastAPI, JavaScript, PostgreSQL, RabbitMQ, Docker, Nginx, Apache, Aiogram, Telethon, разработка на заказ'
          : 'KajimaCode, web development, website creation, Django, Vue.js, full stack developer, Python, FastAPI, JavaScript, PostgreSQL, RabbitMQ, Docker, Nginx, Apache, Aiogram, Telethon, custom development',
      og: {
        title: ru
            ? 'KajimaCode | Создание инновационных и качественных веб-сайтов'
            : 'KajimaCode | Building Innovative and High-Quality Websites',
        type: 'website',
        url: ru
            ? 'https://ru.kajimacode.ru/skills'
            : 'https://kajimacode.ru/skills',
        description: ru
            ? 'Здесь я рассказываю о своих навыках веб-разработки и дизайна. Узнайте, как я могу помочь вашему бизнесу.'
            : 'Here I talk about my web development and design skills. Find out how I can help your business.',
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
            ? 'https://ru.kajimacode.ru/skills'
            : 'https://kajimacode.ru/skills',
        title: ru
            ? 'KajimaCode | Создание инновационных и качественных веб-сайтов'
            : 'KajimaCode | Building Innovative and High-Quality Websites',
        description: ru
            ? 'Здесь я рассказываю о своих навыках веб-разработки и дизайна. Узнайте, как я могу помочь вашему бизнесу.'
            : 'Here I talk about my web development and design skills. Find out how I can help your business.',
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
        axios.get(`${this.backendURL}/api/v1/pages/skills/?language=${lang}`),
        axios.get(`${this.backendURL}/api/v1/pages/footer/?language=${lang}`)
      ])
          .then(response => {
            this.navbar = response[0].data[0]
            this.skillsPage = response[1].data[0]
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

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage') {
        this.get_text(state.language.language)
      }
    })
  },
}
</script>

<style scoped>
.navbar07_component {
  background-color: transparent;
  backdrop-filter: blur(4px) brightness(50%);
  -webkit-backdrop-filter: blur(4px) brightness(50%);
  width: 100vw;
  position: fixed;
}
</style>