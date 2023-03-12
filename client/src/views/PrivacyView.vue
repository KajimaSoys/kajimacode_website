<template>

  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Navbar :frontendUrl="frontendUrl" :text="navbar"/>

  <MainSection :backendUrl="backendUrl" :frontendUrl="frontendUrl" :text="privacyPage"/>

  <Footer :frontendUrl="frontendUrl" :text="footer"/>

</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MainSection from "@/components/privacyPage/MainSection.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import store from "../store";
import { useMeta } from 'vue-meta'

export default {
  name: "PrivacyView",
  data (){
    return {
      backendUrl: this.$backendUrl,
      frontendUrl: this.$frontendUrl,

      navbar: {},
      privacyPage: {},
      footer: {},
    }
  },
  setup() {
    useMeta({
      title: window.location.hostname.startsWith('ru.')
          ? 'Условия и положения | KajimaCode'
          : 'Terms and Conditions | KajimaCode',
      description: window.location.hostname.startsWith('ru.')
          ? 'Ознакомьтесь с условиями использования услуг KajimaCode'
          : 'Read the terms and conditions for using KajimaCode services.',
      og: {
        title: window.location.hostname.startsWith('ru.')
          ? 'Условия и положения | KajimaCode'
          : 'Terms and Conditions | KajimaCode',
        type: 'website',
        url: 'https://kajimacode.com',
        description: window.location.hostname.startsWith('ru.')
          ? 'Ознакомьтесь с условиями использования услуг KajimaCode'
          : 'Read the terms and conditions for using KajimaCode services.',
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
          ? 'Условия и положения | KajimaCode'
          : 'Terms and Conditions | KajimaCode',
        description: window.location.hostname.startsWith('ru.')
          ? 'Ознакомьтесь с условиями использования услуг KajimaCode'
          : 'Read the terms and conditions for using KajimaCode services.',
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
        axios.get(`http://localhost:8000/api/v1/pages/privacy/?language=${lang}`),
        axios.get(`http://localhost:8000/api/v1/pages/footer/?language=${lang}`)
      ])
      .then(response => {
        this.navbar = response[0].data[0]
        this.privacyPage = response[1].data[0]
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
</style>