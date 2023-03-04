<template>
  <header class="section_heroheader24">
    <div class="background-color-white">
      <div class="page-padding-2">
        <div class="container-large">
          <div class="padding-vertical-xhuge">
            <div class="heroheader24_component">
              <div class="max-width-large">
                <h1 class="heading-xlarge">{{ text.introduce_title }}</h1>
                <div class="space-small"></div>
                <div class="text-size-xlarge">{{ text.introduce_description }} <br />
                </div>
                <div class="space-large"></div>
                <div class="space-large"></div>
              </div>
              <div class="heroheader24_image-wrapper">
                <img :src="`${frontendUrl}/src/assets/images/kajimacode_me.png`" loading="lazy" sizes="(max-width: 479px) 100vw, (max-width: 767px) 704px, (max-width: 991px) 100vw, 85vw" :srcset="`${frontendUrl}/src/assets/images/kajimacode_me-p-500.png 500w, ${frontendUrl}/src/assets/images/kajimacode_me-p-800.png 800w, ${frontendUrl}/src/assets/images/kajimacode_me-p-1080.png 1080w, ${frontendUrl}/src/assets/images/kajimacode_me-p-1600.png 1600w, ${frontendUrl}/src/assets/images/kajimacode_me.png 1781w`" alt="" class="heroheader24_image" />
                <div class="heroheader24_image-background"></div>
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
  name: "IntroduceSection",
  props: [
    'frontendUrl',
    'text'
  ],
}
</script>

<style scoped>

</style>