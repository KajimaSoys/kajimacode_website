<template>
  <header class="section_heroheader24">
    <div>
      <div class="page-padding-2">
        <div class="container-large">
          <div class="padding-vertical-xhuge">
            <div class="heroheader24_component ">
              <div class="max-width-large appear">
                <h1 class="heading-xlarge">{{ text.introduce_title }}</h1>
                <div class="space-small"></div>
                <div class="text-size-xlarge">{{ text.introduce_description }} <br/>
                </div>
                <div class="space-large"></div>
                <div class="space-large"></div>
              </div>
              <div class="heroheader24_image-wrapper appear">
                <picture>
                  <source type="image/webp"
                          sizes="(max-width: 767px) 704px, (max-width: 991px) 120vw, min(85vw, 1152px)"
                          :srcset="`${frontendURL}/images/kajimacode_me-p-500.webp 500w, ${frontendURL}/images/kajimacode_me-p-800.webp 800w, ${frontendURL}/images/kajimacode_me-p-1080.webp 1080w, ${frontendURL}/images/kajimacode_me-p-1600.webp 1600w, ${frontendURL}/images/kajimacode_me.webp 1781w`"/>
                  <img :src="`${frontendURL}/images/kajimacode_me.png`" loading="lazy"
                       sizes="(max-width: 767px) 704px, (max-width: 991px) 120vw, min(85vw, 1152px)"
                       :srcset="`${frontendURL}/images/kajimacode_me-p-500.png 500w, ${frontendURL}/images/kajimacode_me-p-800.png 800w, ${frontendURL}/images/kajimacode_me-p-1080.png 1080w, ${frontendURL}/images/kajimacode_me-p-1600.png 1600w, ${frontendURL}/images/kajimacode_me.png 1781w`"
                       alt="" class="heroheader24_image"/>
                </picture>
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
  inject: [
    'backendURL',
    'frontendURL'
  ],
  props: [
    'text'
  ],
}
</script>

<style scoped>
/* picture only switches the format, the img keeps laying out as a direct flex child */
.heroheader24_image-wrapper picture {
  display: contents;
}


</style>