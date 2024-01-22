<template>
  <metainfo>
    <template v-slot:title="{ content, metainfo }">{{ content }}</template>
  </metainfo>

  <Navbar :text="navbar"/>

  <MainSection :scrollToAnchor="scrollToAnchor" :text="mainPage"/>

  <IntroduceSection :text="mainPage"/>

  <ProjectSection :scrollToAnchor="scrollToAnchor" :text="mainPage"/>

  <StagesSection :scrollToAnchor="scrollToAnchor" :text="mainPage"/>

  <TechnologiesSection :scrollToAnchor="scrollToAnchor" :text="mainPage"/>

  <ContactSection :text="mainPage"/>

  <!-- TODO ENABLE BLOCK AFTER REAL REVIEW -->
  <!--      <ReviewSection :text="mainPage"/>-->

  <Footer :scrollToAnchor="scrollToAnchor" :text="footer"/>

  <el-backtop :right="50" :bottom="110"/>

  <Rate source="main"/>

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
import Rate from "@/components/Rate.vue";


import axios from "axios";
import store from "../store";
import {useMeta} from 'vue-meta'
import debounce from "lodash/debounce";


export default {
  name: "MainView",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  data() {
    return {
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
    Rate,
  },

  methods: {
    scrollToAnchor(anchor) {
      const target = document.querySelector(`#${anchor}`);
      target.scrollIntoView({behavior: "smooth"});
    },

    get_text(lang) {
      Promise.all([
        axios.get(`${this.backendURL}/api/v1/pages/navbar/?language=${lang}`),
        axios.get(`${this.backendURL}/api/v1/pages/main/?language=${lang}`),
        axios.get(`${this.backendURL}/api/v1/pages/footer/?language=${lang}`)
      ])
          .then(response => {
            this.navbar = response[0].data[0]
            this.mainPage = response[1].data[0]
            this.footer = response[2].data[0]
          })
          .catch(error => {
            console.log('Ошибка при загрузке локализации')
            console.log('retrying..')
            setTimeout(() => {
              this.get_text()
            }, 3000)
          })
    },
    handleScroll() {
      // document.body.style.setProperty('--scroll',window.pageYOffset / (document.body.offsetHeight - window.innerHeight));
      // console.log(document.body.style.getPropertyValue('--scroll'))
      // navbar brightness
      const backdrop = document.querySelector('.navbar07_component');
      const scrollPosition = window.pageYOffset;
      const brightness = Math.max(50, 100 - scrollPosition / 10);
      backdrop.style.backdropFilter = `blur(4px) brightness(${brightness}%)`;
      backdrop.style.webkitBackdropFilter  = `blur(4px) brightness(${brightness}%)`;
      let screenPosition = window.innerHeight / 1.3; // регулирует когда элемент появится на экране

      // opacity
      let elements = document.querySelectorAll('.appear');
      for (let i = 0; i < elements.length; i++) {
        const element = elements[i]
        let elementPosition = element.getBoundingClientRect().top;

        if (elementPosition < screenPosition) {
          element.classList.add('appear-active');
        } /*else {
          element.classList.remove('appear-active');
        }*/
      }

      // transform from left
      elements = document.querySelectorAll('.from-left');
      for (let i = 0; i < elements.length; i++) {
        const element = elements[i]
        let elementPosition = element.getBoundingClientRect().top;

        if (elementPosition < screenPosition) {
          element.classList.add('from-left-active');
        }
      }

      // transform from right
      elements = document.querySelectorAll('.from-right');
      for (let i = 0; i < elements.length; i++) {
        const element = elements[i]
        let elementPosition = element.getBoundingClientRect().top;

        if (elementPosition < screenPosition) {
          element.classList.add('from-right-active');
        }
      }
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
  mounted() {
    this.handleDebouncedScroll = debounce(this.handleScroll, 10);
    window.addEventListener('scroll', this.handleDebouncedScroll, false);
  },
  unmounted() {
    window.removeEventListener('scroll', this.handleDebouncedScroll, false);
  }
}
</script>

<style>
.section_heroheader07 .page-padding {
  margin-top: 9vh;
}

.el-backtop {
  --el-backtop-text-color: #ff5f29 !important;
  --el-backtop-hover-bg-color: #fff4ee !important;
}

.appear {
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

.appear-active {
  opacity: 1;
}

@media screen and (min-width: 992px) {
  .from-left {
    transform: translateX(-1000px);
    transition: transform 0.5s ease-in-out;
  }

  .from-left-active {
    transform: translateX(0px);
  }

  .from-right {
    transform: translateX(1000px);
    transition: transform 0.5s ease-in-out;
  }

  .from-right-active {
    transform: translateX(0px);
  }
}
</style>

<style scoped>
.navbar07_component {
  background-color: transparent;
  backdrop-filter: blur(4px) brightness(100%);
  -webkit-backdrop-filter: blur(4px) brightness(100%);
  width: 100vw;
  position: fixed;
  transition: backdrop-filter 0.05s ease-in-out;

}

.section_heroheader07 {
  height: 100vh;
}

section {
  overflow-x: auto;
}
</style>

