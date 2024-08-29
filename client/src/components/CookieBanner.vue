<template>
  <section v-if="!$store.state.cookies.hasAcceptedCookies" :style="{opacity: bannerDisplay}"
           class="banner07_component cookie-banner-action">
    <div :style="{transform: bannerPosition}" style="transform-style: preserve-3d" class="banner07_wrapper banner-move">
      <div class="banner07_content">
        <div class="banner07_icon-wrapper">
          <div class="icon-featured-square-large">
            <div class="icon-1x1-xsmall w-embed">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M14.0913 6.72222H20.0451C20.5172 6.72222 20.7533 6.72222 20.8914 6.82149C21.0118 6.9081 21.0903 7.04141 21.1075 7.18877C21.1272 7.35767 21.0126 7.56403 20.7833 7.97677L19.3624 10.5343C19.2792 10.684 19.2376 10.7589 19.2213 10.8381C19.2069 10.9083 19.2069 10.9806 19.2213 11.0508C19.2376 11.13 19.2792 11.2049 19.3624 11.3545L20.7833 13.9121C21.0126 14.3248 21.1272 14.5312 21.1075 14.7001C21.0903 14.8475 21.0118 14.9808 20.8914 15.0674C20.7533 15.1667 20.5172 15.1667 20.0451 15.1667H12.6136C12.0224 15.1667 11.7268 15.1667 11.501 15.0516C11.3024 14.9504 11.1409 14.7889 11.0397 14.5903C10.9247 14.3645 10.9247 14.0689 10.9247 13.4778V10.9444M7.23023 21.5L3.00801 4.61111M4.59139 10.9444H12.4024C12.9936 10.9444 13.2892 10.9444 13.515 10.8294C13.7136 10.7282 13.8751 10.5667 13.9763 10.3681C14.0913 10.1423 14.0913 9.84672 14.0913 9.25556V4.18889C14.0913 3.59772 14.0913 3.30214 13.9763 3.07634C13.8751 2.87773 13.7136 2.71625 13.515 2.61505C13.2892 2.5 12.9936 2.5 12.4024 2.5H4.6433C3.90597 2.5 3.53731 2.5 3.28515 2.65278C3.06415 2.78668 2.89995 2.99699 2.82364 3.24387C2.73659 3.52555 2.82601 3.88321 3.00484 4.59852L4.59139 10.9444Z"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
        </div>
        <div class="banner07_text-wrapper">
          <div class="banner07_text">{{ text.element_text }}</div>
          <div class="banner07_supporting-text">
            <router-link to="/cookies">
              {{ text.link }}
            </router-link>
          </div>
        </div>
      </div>
      <div class="button-row-cookie">
        <div class="button-wrapper" @click="cookieAccept">
          <a class="button-secondary is-button-small cookie-banner-action w-inline-block">
            <div class="text-block-3">{{ text.button }}</div>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {mapState, mapMutations} from 'vuex'
import axios from "axios";

export default {
  name: "CookieBanner",
  inject: [
      'backendURL'
  ],
  data() {
    return {
      text: {
        'element_text': 'This website uses cookies.',
        'link': 'Learn more',
        'button': 'Allow',
      },

      bannerPosition: 'translate3d(0px, 0vh, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)',
      bannerDisplay: '1',
    }
  },

  methods: {
    cookieAccept() {
      this.bannerDisplay = '0'
      this.$store.commit('cookies/cookieAccept')
    },

    async get_text(lang) {
      await axios
          .get(`${this.backendURL}/api/v1/pages/cookie-element/?language=${lang}`)
          .then(response => {
            this.text = response.data[0]
          })
          .catch(error => {
            console.log('Ошибка при загрузке локализации для Cookie-element')
            console.log('retrying..')
            setTimeout(() => {
              this.get_text()
            }, 5000)
          })
    }
  },

  beforeCreate() {
    this.$store.commit('cookies/initializeStore')
  },

  created() {
    this.get_text(this.$store.state.language.language)
  },

  mounted() {
    setTimeout(() => {
      this.bannerPosition = 'translate3d(0px, -15vh, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)'
    }, 2000)
  },
}
</script>

<style scoped>
.banner-move {
  transition: transform ease 0.5s;
}

.cookie-banner-action {
  transition: opacity ease 0.2s;
}

.banner07_supporting-text a {
  color: white;
}

.button-secondary.is-button-small.cookie-banner-action:hover {
  transition: background-color 0.2s ease-in-out;
}
</style>