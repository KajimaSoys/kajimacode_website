<template>
  <section class="section_layout18">
    <div class="page-padding-2">
      <div class="container-large-2">
        <div class="padding-vertical-xhuge">
          <h1 class="heading-xlarge appear">{{ text.technologies_title }}</h1>
          <div class="space-large"></div>
          <div class="space-large"></div>
          <div class="w-layout-grid layout18_component">
            <div class="layout18_content">
              <div class="w-layout-grid layout18_item-list">
                <div class="layout18_item appear from-left">
                  <div class="layout18_item-icon-wrapper">
                    <div class="icon-featured-outline-large-2">
                      <img :src="`${frontendURL}/src/assets/icons/gear.svg`" loading="lazy" alt=""
                           class="technologies-icon"/>
                    </div>
                  </div>
                  <div class="layout18_item-text-wrapper">
                    <h2 class="heading-xsmall">{{ text.django_title }}</h2>
                    <div class="text-size-medium">{{ text.django_description }}</div>
                    <div class="space-xxsmall"></div>
                  </div>
                </div>
                <div class="layout18_item  from-left">
                  <div class="layout18_item-icon-wrapper">
                    <div class="icon-featured-outline-large-2">
                      <img :src="`${frontendURL}/src/assets/icons/database.svg`" loading="lazy" alt=""
                           class="technologies-icon db-icon"/>
                    </div>
                  </div>
                  <div class="layout18_item-text-wrapper">
                    <h2 class="heading-xsmall">{{ text.postgresql_title }}</h2>
                    <div class="space-xxsmall"></div>
                    <div class="text-size-medium">{{ text.postgresql_description }}</div>
                  </div>
                </div>
                <div class="layout18_item appear from-left">
                  <div class="layout18_item-icon-wrapper">
                    <div class="icon-featured-outline-large-2">
                      <img :src="`${frontendURL}/src/assets/icons/tab.svg`" loading="lazy" alt=""
                           class="technologies-icon"/>
                    </div>
                  </div>
                  <div class="layout18_item-text-wrapper">
                    <h2 class="heading-xsmall">{{ text.vue_title }}</h2>
                    <div class="space-xxsmall"></div>
                    <div class="text-size-medium">{{ text.vue_description }}</div>
                  </div>
                </div>
              </div>
              <div class="button-row is-reverse-mobile-landscape">
                <div class="button-wrapper max-width-full-mobile-landscape">
                  <a @click="scrollToAnchor('contact-section')" class="button-secondary-gray w-inline-block">
                    <div>{{ text.get_started_button }}</div>
                  </a>
                </div>
                <div class="button-wrapper max-width-full-mobile-landscape">
                  <router-link to="/skills" class="button-3 w-inline-block">
                    <div>{{ text.learn_more_button }}</div>
                  </router-link>
                </div>
              </div>
            </div>
            <img :src="`${frontendURL}/src/assets/technologies2.gif`" loading="lazy"
                 sizes="(max-width: 479px) 100vw, (max-width: 767px) 92vw, (max-width: 991px) 43vw, 45vw"
                 alt="Technologies i use" class="from-right"/>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "TechnologiesSection",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  props: [
    'scrollToAnchor',
    'text'
  ],
}
</script>

<style scoped>

</style>