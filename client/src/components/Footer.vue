<template>
  <footer class="footer04_component">
    <div class="page-padding-2 background-color-white">
      <div class="container-large">
        <div class="padding-vertical-xlarge">
          <div class="w-layout-grid footer04_top-wrapper">
            <a v-if="isMainPage" @click="scrollToTop()" class="footer04_logo-link w-inline-block">
              <div class="logo_component">
                <img :src="`${frontendURL}/images/kajimacode_black_orange.svg`" loading="lazy"
                     alt="KajimaCode Black Orange Logo" class="logo_logotype"/>
              </div>
            </a>

            <router-link v-else to="/" class="footer04_logo-link w-inline-block">
              <div class="logo_component">
                <img :src="`${frontendURL}/images/kajimacode_black_orange.svg`" loading="lazy"
                     alt="KajimaCode Black Orange Logo" class="logo_logotype"/>
              </div>
            </router-link>


            <div class="w-layout-grid footer04_link-list">
              <a v-if="isMainPage" @click="scrollToTop()" class="footer04_link w-inline-block">
                <div>{{ text.overview_link }}</div>
              </a>

              <router-link v-else to="/" class="footer04_link w-inline-block">
                <div>{{ text.overview_link }}</div>
              </router-link>

              <router-link to="/projects" class="footer04_link w-inline-block">
                <div>{{ text.projects_link }}</div>
              </router-link>

              <router-link to="/skills" class="footer04_link w-inline-block">
                <div>{{ text.skills_link }}</div>
              </router-link>

              <router-link to="/about" class="footer04_link w-inline-block">
                <div>{{ text.about_link }}</div>
              </router-link>

              <!--              <router-link to="/privacy" class="footer04_link w-inline-block">-->
              <!--                <div>Privacy</div>-->
              <!--              </router-link>-->


            </div>
            <div id="w-node-_8e86dbb8-08f7-b4c9-5aa4-81d1b45d7757-b45d773c" class="w-layout-grid footer04_social-list">
              <a href="https://t.me/OneDudeAdam" target="_blank" class="footer04_social-link w-inline-block">
                <div class="footer04_social-icon w-embed">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path
                        d="M24,2.67v.24L24,3c-.09.42-.17.83-.26,1.25s-.18.88-.28,1.32l-.12.55c-.07.31-.13.63-.19.94s-.13.55-.18.83-.08.39-.12.59-.1.47-.14.7c-.09.38-.17.77-.25,1.15s-.19.9-.28,1.35L22,12.4c-.09.38-.17.75-.25,1.13l-.15.74-.12.54c-.06.32-.12.64-.19.95l-.18.85c-.07.31-.13.62-.19.93s-.14.68-.22,1-.1.51-.16.76-.15.73-.22,1.09-.09.42-.14.64a1.19,1.19,0,0,1-.38.71,1.06,1.06,0,0,1-.47.21,1.42,1.42,0,0,1-.46,0,1.35,1.35,0,0,1-.56-.25l-1.49-1.1-3.4-2.49-.62-.45-.65.61L9.73,20.58a.91.91,0,0,1-.94.22.77.77,0,0,1-.52-.5c-.09-.23-.16-.46-.24-.7l-.48-1.43c-.09-.29-.19-.59-.29-.88-.29-.9-.59-1.79-.88-2.68l-.32-.95s0,0,0-.05l-.55-.18L4,13l-1.35-.42L2,12.37.63,11.93a.77.77,0,0,1-.57-.48L0,11.29V11l0,0a.81.81,0,0,1,.54-.57l1.81-.67,2-.74L6.47,8.2l2.07-.78,2.84-1.06,2.27-.84,2.15-.8,2.26-.84L20.52,3l2.14-.79.5-.18h.2a.94.94,0,0,1,.58.49A.85.85,0,0,1,24,2.67ZM9,18.56l0,0c0-.27,0-.54.08-.81s0-.55.07-.83c0-.08,0-.15,0-.23s0-.23,0-.34l0-.43c0-.25,0-.5.08-.75a.11.11,0,0,1,0-.05l1.86-1.67,1.92-1.74,2-1.77,2.32-2.1,2.18-2a.18.18,0,0,0,.05-.17.26.26,0,0,0-.38-.13l-1.13.7L15.4,8,13,9.49l-2.61,1.67L7.81,12.84l-.43.27Z"
                        fill="currentColor"/>
                  </svg>
                </div>
              </a>
              <a href="https://www.instagram.com/kajimasoys/" target="_blank"
                 class="footer04_social-link w-inline-block">
                <div class="footer04_social-icon w-embed">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M12 2.16094C15.2063 2.16094 15.5859 2.175 16.8469 2.23125C18.0188 2.28281 18.6516 2.47969 19.0734 2.64375C19.6313 2.85938 20.0344 3.12188 20.4516 3.53906C20.8734 3.96094 21.1313 4.35938 21.3469 4.91719C21.5109 5.33906 21.7078 5.97656 21.7594 7.14375C21.8156 8.40937 21.8297 8.78906 21.8297 11.9906C21.8297 15.1969 21.8156 15.5766 21.7594 16.8375C21.7078 18.0094 21.5109 18.6422 21.3469 19.0641C21.1313 19.6219 20.8688 20.025 20.4516 20.4422C20.0297 20.8641 19.6313 21.1219 19.0734 21.3375C18.6516 21.5016 18.0141 21.6984 16.8469 21.75C15.5813 21.8063 15.2016 21.8203 12 21.8203C8.79375 21.8203 8.41406 21.8063 7.15313 21.75C5.98125 21.6984 5.34844 21.5016 4.92656 21.3375C4.36875 21.1219 3.96563 20.8594 3.54844 20.4422C3.12656 20.0203 2.86875 19.6219 2.65313 19.0641C2.48906 18.6422 2.29219 18.0047 2.24063 16.8375C2.18438 15.5719 2.17031 15.1922 2.17031 11.9906C2.17031 8.78438 2.18438 8.40469 2.24063 7.14375C2.29219 5.97187 2.48906 5.33906 2.65313 4.91719C2.86875 4.35938 3.13125 3.95625 3.54844 3.53906C3.97031 3.11719 4.36875 2.85938 4.92656 2.64375C5.34844 2.47969 5.98594 2.28281 7.15313 2.23125C8.41406 2.175 8.79375 2.16094 12 2.16094ZM12 0C8.74219 0 8.33438 0.0140625 7.05469 0.0703125C5.77969 0.126563 4.90313 0.332812 4.14375 0.628125C3.35156 0.9375 2.68125 1.34531 2.01563 2.01562C1.34531 2.68125 0.9375 3.35156 0.628125 4.13906C0.332812 4.90313 0.126563 5.775 0.0703125 7.05C0.0140625 8.33437 0 8.74219 0 12C0 15.2578 0.0140625 15.6656 0.0703125 16.9453C0.126563 18.2203 0.332812 19.0969 0.628125 19.8563C0.9375 20.6484 1.34531 21.3188 2.01563 21.9844C2.68125 22.65 3.35156 23.0625 4.13906 23.3672C4.90313 23.6625 5.775 23.8687 7.05 23.925C8.32969 23.9812 8.7375 23.9953 11.9953 23.9953C15.2531 23.9953 15.6609 23.9812 16.9406 23.925C18.2156 23.8687 19.0922 23.6625 19.8516 23.3672C20.6391 23.0625 21.3094 22.65 21.975 21.9844C22.6406 21.3188 23.0531 20.6484 23.3578 19.8609C23.6531 19.0969 23.8594 18.225 23.9156 16.95C23.9719 15.6703 23.9859 15.2625 23.9859 12.0047C23.9859 8.74688 23.9719 8.33906 23.9156 7.05938C23.8594 5.78438 23.6531 4.90781 23.3578 4.14844C23.0625 3.35156 22.6547 2.68125 21.9844 2.01562C21.3188 1.35 20.6484 0.9375 19.8609 0.632812C19.0969 0.3375 18.225 0.13125 16.95 0.075C15.6656 0.0140625 15.2578 0 12 0Z"
                        fill="currentColor"/>
                    <path
                        d="M12 5.83594C8.59688 5.83594 5.83594 8.59688 5.83594 12C5.83594 15.4031 8.59688 18.1641 12 18.1641C15.4031 18.1641 18.1641 15.4031 18.1641 12C18.1641 8.59688 15.4031 5.83594 12 5.83594ZM12 15.9984C9.79219 15.9984 8.00156 14.2078 8.00156 12C8.00156 9.79219 9.79219 8.00156 12 8.00156C14.2078 8.00156 15.9984 9.79219 15.9984 12C15.9984 14.2078 14.2078 15.9984 12 15.9984Z"
                        fill="currentColor"/>
                    <path
                        d="M19.8469 5.59214C19.8469 6.38902 19.2 7.0312 18.4078 7.0312C17.6109 7.0312 16.9688 6.38433 16.9688 5.59214C16.9688 4.79526 17.6156 4.15308 18.4078 4.15308C19.2 4.15308 19.8469 4.79995 19.8469 5.59214Z"
                        fill="currentColor"/>
                  </svg>
                </div>
              </a>
              <a href="https://github.com/KajimaSoys" class="footer04_social-link w-inline-block" target="_blank">
                <div class="footer04_social-icon w-embed">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path
                        d="M12,0a12.11,12.11,0,0,0-3.8,23.58c.6.12.82-.26.82-.58s0-1.25,0-2.25c-3.34.72-4-1.44-4-1.44a3.11,3.11,0,0,0-1.33-1.76c-1.09-.74.08-.74.08-.74a2.53,2.53,0,0,1,1.85,1.24,2.55,2.55,0,0,0,3.5,1,2.56,2.56,0,0,1,.75-1.62c-2.66-.28-5.47-1.32-5.47-6A4.74,4.74,0,0,1,5.59,8.21,4.36,4.36,0,0,1,5.71,5s1-.32,3.3,1.24a11.29,11.29,0,0,1,3-.4,11.54,11.54,0,0,1,3,.4C17.3,4.69,18.31,5,18.31,5a4.36,4.36,0,0,1,.12,3.2,4.65,4.65,0,0,1,1.24,3.25c0,4.65-2.81,5.67-5.49,6A2.89,2.89,0,0,1,15,19.67c0,1.62,0,2.93,0,3.33s.22.7.82.58A12.11,12.11,0,0,0,12,0Z"
                        fill="currentColor"/>
                  </svg>
                </div>
              </a>
              <a href="https://www.linkedin.com/in/vadim-grishin-95b70a193/" class="footer04_social-link w-inline-block"
                 target="_blank">
                <div class="footer04_social-icon w-embed">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M22.2234 0H1.77187C0.792187 0 0 0.773438 0 1.72969V22.2656C0 23.2219 0.792187 24 1.77187 24H22.2234C23.2031 24 24 23.2219 24 22.2703V1.72969C24 0.773438 23.2031 0 22.2234 0ZM7.12031 20.4516H3.55781V8.99531H7.12031V20.4516ZM5.33906 7.43438C4.19531 7.43438 3.27188 6.51094 3.27188 5.37187C3.27188 4.23281 4.19531 3.30937 5.33906 3.30937C6.47813 3.30937 7.40156 4.23281 7.40156 5.37187C7.40156 6.50625 6.47813 7.43438 5.33906 7.43438ZM20.4516 20.4516H16.8937V14.8828C16.8937 13.5562 16.8703 11.8453 15.0422 11.8453C13.1906 11.8453 12.9094 13.2937 12.9094 14.7891V20.4516H9.35625V8.99531H12.7687V10.5609H12.8156C13.2891 9.66094 14.4516 8.70938 16.1813 8.70938C19.7859 8.70938 20.4516 11.0813 20.4516 14.1656V20.4516Z"
                        fill="currentColor"/>
                  </svg>
                </div>
              </a>
            </div>
          </div>
          <div class="footer04_bottom-wrapper">
            <div class="text-size-small text-color-gray500">© {{ new Date().getFullYear() }} Kajima Code</div>
            <div class="w-layout-grid footer04_legal-list">

              <router-link to="/terms" class="footer04_legal-link">
                {{ text.terms_link }}
              </router-link>

              <router-link to="/privacy" class="footer04_legal-link">
                {{ text.privacy_link }}
              </router-link>

              <router-link to="/cookies" class="footer04_legal-link">
                {{ text.cookies_link }}
              </router-link>

            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  props: [
    'scrollToAnchor',
    'text'
  ],
  computed: {
    isMainPage() {
      return window.location.pathname === '/'
    }
  },
  methods: {
    scrollToTop() {
      const button = document.getElementsByClassName('el-backtop')[0];
      if (button) {
        button.dispatchEvent(new Event('click'));
      }
    }
  },
}
</script>

<style scoped>

</style>