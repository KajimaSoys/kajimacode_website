<template>
  <header @mousemove="updateFontVariation" class="section_heroheader07">
    <div class="page-padding">
      <div class="container-large">
        <div class="padding-vertical-xhuge">
          <div class="w-layout-grid heroheader07_component">
            <div class="heroheader07_content z-index-1">
              <h1 class="main-text">
                <p data-splitting ref="text">{{ textArray[0] }}<br>{{ textArray[1] }}<br>{{ textArray[2] }}</p>
              </h1>
              <div class="space-small-main"></div>
              <div class="max-width-small-main"></div>
              <div class="button-row-main is-reverse-mobile-landscape">
                <div class="button-wrapper max-width-full-mobile-landscape">
                  <a @click="scrollToAnchor('contact-section')" class="button is-button-large w-inline-block">
                    <!--href="#contact-section"-->
                    <div class="text-block-2">{{ text.contact_button }}</div>
                  </a>
                </div>
              </div>
            </div>
            <div class="heroheader07_image-wrapper">
              <img :src="`${frontendURL}/src/assets/images/light_orig.png`" alt="Colorful gradient"
                   class="heroheader07_light-overlay"/>
              <!--                <spline scene="https://prod.spline.design/DAnBj2USRzWxm2jA/scene.splinecode" />-->
              <spline-component/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import SplineComponent from "./SplineComponent.vue";
import Splitting from 'splitting';
// import Spline from 'vue-spline';

export default {
  name: "MainSection",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  components: {
    SplineComponent
  },
  props: [
    'scrollToAnchor',
    'text'
  ],
  data() {
    return {
      spans: [],
      textArray: ['I', 'DEVELOP', 'WEBSITES'],
      // requestd_text: ,
      // splitted: []
    }
  },
  computed: {
    // split_text(){
    //   console.log(this.text.main_title.split(' '))
    //   return this.text.main_title.split(' ')
    // }
  },
  beforeMount() {

  },
  mounted() {
    // this.textArray = this.text.main_title.split(' ')
    Splitting({
      target: this.$refs.text,
    });

    this.spans = this.$el.querySelectorAll('.char');
  },
  methods: {
    updateFontVariation(event) {
      let multiplierWidth = event.clientX / window.innerWidth;
      let randomWeight = multiplierWidth * (270 - 12) + 12;
      for (let i = 0; i < 16; i++) {
        setTimeout(() => {
          this.spans[i].style.fontVariationSettings = `"wght" ${randomWeight}`;
        }, i * 100);
      }
    }
  },
  created() {

  }
}
</script>

<style>

.text-block-2 {
  font-size: 1.125rem;
}

.main-text {
  will-change: font-variation-settings;
  text-rendering: optimizeSpeed;
  user-select: none;
}

p .char {
  --delay: calc(var(--char-index) * 25ms);
  transition: font-variation-settings 0.2s ease-out, color 0.2s ease-out;
  transition-delay: var(--delay), 0;
}

.char:hover {
  color: #ff5f29;
  /*cursor: pointer;*/
}

.heroheader07_image-wrapper {
  border-radius: 25px;
}

@media screen and (max-width: 767px) {
  .button-row-main.is-reverse-mobile-landscape {
    top: 0 !important;
  }

  .heroheader07_content.z-index-1 {
    display: block !important;
  }

  .button-wrapper.max-width-full-mobile-landscape {
    width: 100% !important;
  }

  .main-text {
    font-size: 5rem !important;
  }

  .section_heroheader07 .padding-vertical-xhuge {
    padding-top: 0;
    padding-bottom: 0;
  }

  .heroheader07_component {
    grid-row-gap: 0 !important;
  }
}

@media screen and (max-width: 479px) {
  .heroheader07_light-overlay {
    right: -53% !important;
    bottom: -72% !important;
  }

  .main-text {
    font-size: 16vw !important;
  }

}

</style>