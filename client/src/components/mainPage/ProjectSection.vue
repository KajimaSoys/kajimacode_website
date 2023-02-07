<template>
  <header class="section_heroheader04">
    <div class="page-padding-2">
      <div class="container-large-2">
        <div class="padding-vertical-xhuge">
          <div class="w-layout-grid heroheader04_component">
            <div class="heroheader04_image-wrapper">
              <img src="src/assets/images/rezal_laptop_mockup.png" loading="lazy" sizes="(max-width: 479px) 100vw, (max-width: 767px) 96vw, (max-width: 991px) 94vw, 1184px" srcset="src/assets/images/rezal_laptop_mockup-p-500.png 500w, src/assets/images/rezal_laptop_mockup-p-800.png 800w, src/assets/images/rezal_laptop_mockup-p-1080.png 1080w, src/assets/images/rezal_laptop_mockup-p-1600.png 1600w, src/assets/images/rezal_laptop_mockup.png 1920w" alt="MacBook mockup" class="heroheader04_image" />
            </div>
            <div class="heroheader04_content">
              <h1 class="heading-xlarge-2">The perfect site for doing business</h1>
              <div class="space-small"></div>
              <div class="max-width-medium">
                <div class="text-size-xlarge-2">My services include responsive design, e-commerce integration, and SEO optimization to ensure your website is not only beautiful but also functional and easy to find. </div>
              </div>
              <div class="space-large"></div>
              <div class="button-row">
                <div class="button-wrapper max-width-full-mobile-landscape">
                  <a @click="scrollToAnchor('contact-section')" class="button-3 is-button-large w-inline-block">
                    <div>Contact me!</div>
                  </a>
                </div>
                <div class="button-wrapper">
                  <router-link to="/projects" class="button-tertiary-gray w-inline-block">
                    <div>See my projects</div>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "ProjectSection",
  props: [
    'scrollToAnchor'
  ],
}
</script>

<style scoped>

</style>