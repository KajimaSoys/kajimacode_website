<template>

  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Navbar :frontendUrl="frontendUrl" :text="navbar"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl" :text="aboutPage"/>

  <Footer :frontendUrl="frontendUrl" :text="footer"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/aboutPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import store from "../store";
import { useMeta } from 'vue-meta'

export default {
  name: 'AboutView',
  data (){
    return {
      backendUrl: this.$backendUrl,
      frontendUrl: this.$frontendUrl,

      navbar: {},
      aboutPage: {},
      footer: {},
    }
  },
  setup() {
    let ru = window.location.hostname.startsWith('ru.')
    useMeta({
      title: ru
          ? 'Обо мне | KajimaCode'
          : 'About me | KajimaCode',
      description: ru
          ? 'Узнайте больше обо мне и моем опыте в веб-разработке. Я готов помочь вам создать превосходный веб-сайт для вашего бизнеса.'
          : 'Learn more about me and my experience in web development. I\'m ready to help you build the perfect website for your business.',
      og: {
        title: ru
          ? 'Обо мне | KajimaCode'
          : 'About me | KajimaCode',
        type: 'website',
        url: ru
          ? 'https://ru.kajimacode.com/about'
          : 'https://kajimacode.com/about',
        description: ru
          ? 'Узнайте больше обо мне и моем опыте в веб-разработке. Я готов помочь вам создать превосходный веб-сайт для вашего бизнеса.'
          : 'Learn more about me and my experience in web development. I\'m ready to help you build the perfect website for your business.',
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
          ? 'https://ru.kajimacode.com/about'
          : 'https://kajimacode.com/about',
        title: ru
          ? 'Обо мне | KajimaCode'
          : 'About me | KajimaCode',
        description: ru
          ? 'Узнайте больше обо мне и моем опыте в веб-разработке. Я готов помочь вам создать превосходный веб-сайт для вашего бизнеса.'
          : 'Learn more about me and my experience in web development. I\'m ready to help you build the perfect website for your business.',
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
    Footer,
  },
  methods: {
    get_text(lang){

    Promise.all([
        axios.get(`http://localhost:8000/api/v1/pages/navbar/?language=${lang}`),
        axios.get(`http://localhost:8000/api/v1/pages/about/?language=${lang}`),
        axios.get(`http://localhost:8000/api/v1/pages/footer/?language=${lang}`)
      ])
      .then(response => {
        this.navbar = response[0].data[0]
        this.aboutPage = response[1].data[0]
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
