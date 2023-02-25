<template>
  <header  @mousemove="updateFontVariation" class="section_heroheader07">
      <div class="page-padding">
        <div class="container-large">
          <div class="padding-vertical-xhuge">
            <div class="w-layout-grid heroheader07_component">
              <div class="heroheader07_content z-index-1">
                <h1 class="main-text">
                  <p data-splitting ref="text">I<br>DEVELOP<br>WEBSITES</p>
                </h1>
                <div class="space-small-main"></div>
                <div class="max-width-small-main"></div>
                <div id="w-node-ce1876c0-0d11-fbee-deef-74e9829160f6-9f429e46" class="button-row-main is-reverse-mobile-landscape">
                  <div class="button-wrapper max-width-full-mobile-landscape">
                    <a @click="scrollToAnchor('contact-section')" class="button is-button-large w-inline-block"> <!--href="#contact-section"-->
                      <div class="text-block-2">Contact me!</div>
                    </a>
                  </div>
                </div>
              </div>
              <div class="heroheader07_image-wrapper">
                <img :src="`${frontendUrl}/src/assets/images/light_orig.png`" loading="lazy" alt="Colorful gradient" class="heroheader07_light-overlay" />
<!--                <spline scene="https://prod.spline.design/DAnBj2USRzWxm2jA/scene.splinecode" />-->
                <ascii-render/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
</template>

<script>
import AsciiRender from "@/components/mainPage/AsciiRender.vue";
import Splitting from 'splitting';
// import Spline from 'vue-spline';

export default {
  name: "MainSection",

  components: {
    AsciiRender,
    // Spline
  },
  props: [
    'scrollToAnchor',
    'frontendUrl'
  ],
  data(){
    return {
      spans: [],
    }
  },
  computed: {

  },
  mounted() {
    Splitting({
      target: this.$refs.text,
    });
    this.spans = this.$el.querySelectorAll('.char');
  },
  methods: {
    updateFontVariation(event) {
      let multiplierWidth = event.clientX / window.innerWidth;
      let randomWeight =  multiplierWidth * (270 - 12) + 12;
      for (let i = 0; i<16; i++){
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

.main-text{
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

</style>