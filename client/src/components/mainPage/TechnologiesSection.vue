<template>
  <section class="section_layout18">
    <div class="page-padding-2">
      <div class="container-large-2">
        <div class="padding-vertical-xhuge">
          <h1 class="heading-xlarge">Technologies I use</h1>
          <div class="space-large"></div>
          <div class="space-large"></div>
          <div class="w-layout-grid layout18_component">
            <div class="layout18_content">
              <div class="w-layout-grid layout18_item-list">
                <div id="w-node-_473af96d-fe9a-7583-1058-afd0b4f508bd-9f429e46" class="layout18_item">
                  <div class="layout18_item-icon-wrapper">
                    <div class="icon-featured-outline-large-2">
                      <img :src="`${frontendUrl}/src/assets/icons/gear.svg`" loading="lazy" alt="" class="technologies-icon" />
                    </div>
                  </div>
                  <div class="layout18_item-text-wrapper">
                    <h3 class="heading-xsmall">Django</h3>
                    <div class="text-size-medium">It is a high-level Python web framework that allows for the rapid development of secure and maintainable web applications.</div>
                    <div class="space-xxsmall"></div>
                  </div>
                </div>
                <div id="w-node-_473af96d-fe9a-7583-1058-afd0b4f508c7-9f429e46" class="layout18_item">
                  <div class="layout18_item-icon-wrapper">
                    <div class="icon-featured-outline-large-2">
                      <img :src="`${frontendUrl}/src/assets/icons/database.svg`" loading="lazy" alt="" class="technologies-icon db-icon" />
                    </div>
                  </div>
                  <div class="layout18_item-text-wrapper">
                    <h3 class="heading-xsmall">PostgreSQL</h3>
                    <div class="space-xxsmall"></div>
                    <div class="text-size-medium">PostgreSQL is a powerful relational database management system that offers advanced features for data integrity, scalability and performance.</div>
                  </div>
                </div>
                <div id="w-node-_473af96d-fe9a-7583-1058-afd0b4f508d1-9f429e46" class="layout18_item">
                  <div class="layout18_item-icon-wrapper">
                    <div class="icon-featured-outline-large-2">
                      <img :src="`${frontendUrl}/src/assets/icons/tab.svg`" loading="lazy" alt="" class="technologies-icon" />
                    </div>
                  </div>
                  <div class="layout18_item-text-wrapper">
                    <h3 class="heading-xsmall">Vue.js</h3>
                    <div class="space-xxsmall"></div>
                    <div class="text-size-medium">Vue is a progressive JavaScript framework for building user interfaces that allows for building reusable, composable components and efficient updates, making it a great choice for building dynamic and interactive web applications.</div>
                  </div>
                </div>
              </div>
              <div class="button-row is-reverse-mobile-landscape">
                <div class="button-wrapper max-width-full-mobile-landscape">
                  <a @click="scrollToAnchor('contact-section')" class="button-secondary-gray w-inline-block">
                    <div>Get started</div>
                  </a>
                </div>
                <div class="button-wrapper max-width-full-mobile-landscape">
                  <router-link to="/skills" class="button-3 w-inline-block">
                      <div>Learn more</div>
                  </router-link>
                </div>
              </div>
            </div>
            <img :src="`${frontendUrl}/src/assets/technologies2.gif`" loading="lazy" id="w-node-_45e33f72-7130-365c-f243-d91ee3a0b293-9f429e46" sizes="(max-width: 479px) 100vw, (max-width: 767px) 92vw, (max-width: 991px) 43vw, 45vw" alt="" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "TechnologiesSection",
  props: [
    'scrollToAnchor',
    'frontendUrl'
  ],
}
</script>

<style scoped>

</style>