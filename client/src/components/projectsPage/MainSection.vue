<template>
  <!--  <vue-nprogress :percent="percent" :showSpinner="false"></vue-nprogress>-->
  <div class="project-container">
    <el-carousel :interval="10000" arrow="always" indicator-position="none">
      <el-carousel-item v-for="project in projects" :key="project.id">
        <div class="image-container">
          <div class="blackout"></div>
          <div class="gradient"></div>
          <div class="image">
            <img v-if="project.image_set.length !== 0" :src="`${backendURL}` + project.image_set[0].image" loading="lazy">
            <img class="no-image" v-else :src="`${frontendURL}/assets/images/no-image.jpg`" loading="lazy">
          </div>
        </div>
        <div class="text-container">
          <div class="hover-area"></div>

          <router-link v-if="apiEndpoint==='True'" :to="{ name: 'project', params: { id: project.id } }"
                       class="project-link">
            <h1 v-if="lang_ru" class="title">
              {{ project.name_ru }}
            </h1>

            <h1 v-else class="title">
              {{ project.name }}
            </h1>
          </router-link>

          <router-link v-else :to="{ name: 'teamProject', params: { id: project.id } }" class="project-link">
            <h1 v-if="lang_ru" class="title">
              {{ project.name_ru }}
            </h1>

            <h1 v-else class="title">
              {{ project.name }}
            </h1>
          </router-link>

          <p v-if="lang_ru" class="description">
            {{ project.description_short_ru }}
          </p>
          <p v-else class="description">
            {{ project.description_short }}
          </p>

          <div class="additional">
            <div class="groups">
              {{ project.get_group }}
            </div>
            <div class="links">
              <a v-if="project.git" :href="project.git" class="navbar_social-link w-inline-block" target="_blank">
                <div class="project-icons">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path
                        d="M12,0a12.11,12.11,0,0,0-3.8,23.58c.6.12.82-.26.82-.58s0-1.25,0-2.25c-3.34.72-4-1.44-4-1.44a3.11,3.11,0,0,0-1.33-1.76c-1.09-.74.08-.74.08-.74a2.53,2.53,0,0,1,1.85,1.24,2.55,2.55,0,0,0,3.5,1,2.56,2.56,0,0,1,.75-1.62c-2.66-.28-5.47-1.32-5.47-6A4.74,4.74,0,0,1,5.59,8.21,4.36,4.36,0,0,1,5.71,5s1-.32,3.3,1.24a11.29,11.29,0,0,1,3-.4,11.54,11.54,0,0,1,3,.4C17.3,4.69,18.31,5,18.31,5a4.36,4.36,0,0,1,.12,3.2,4.65,4.65,0,0,1,1.24,3.25c0,4.65-2.81,5.67-5.49,6A2.89,2.89,0,0,1,15,19.67c0,1.62,0,2.93,0,3.33s.22.7.82.58A12.11,12.11,0,0,0,12,0Z"
                        fill="currentColor"/>
                  </svg>
                </div>
              </a>
              <a v-if="project.link" :href="project.link" class="navbar_social-link w-inline-block" target="_blank">
                <div class="project-icons">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path
                        d="M23.7,11.29,21.22,8.87A13.11,13.11,0,0,0,12,5.15,13.09,13.09,0,0,0,2.78,8.87L.3,11.29a1,1,0,0,0,0,1.43l2.48,2.42A13.12,13.12,0,0,0,12,18.85a13.14,13.14,0,0,0,9.22-3.71l2.48-2.42a1,1,0,0,0,0-1.43ZM12,15.42A3.42,3.42,0,1,1,15.42,12,3.42,3.42,0,0,1,12,15.42ZM2.43,12l1.75-1.7A10.91,10.91,0,0,1,8.87,7.58a5.4,5.4,0,0,0,0,8.83A11,11,0,0,1,4.18,13.7L2.43,12Zm17.39,1.71a11.07,11.07,0,0,1-4.69,2.7,5.39,5.39,0,0,0,0-8.82,11,11,0,0,1,4.69,2.71L21.56,12l-1.74,1.7Z"
                        fill="currentColor"/>
                  </svg>
                </div>
              </a>
            </div>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
import axios from "axios";
import store from "../../store";
import {resolveTransitionHooks} from "vue";
// import VueNprogress from 'vue-nprogress'

export default {
  name: "MainSection.vue",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  components: [
    // VueNprogress
  ],
  props: [
    'apiEndpoint',
    'text'
  ],
  data() {
    return {
      projects: [],
      lang_ru: false,
    }
  },

  methods: {
    switchLanguage(lang) {
      this.lang_ru = lang === 'ru';
    },
    async get_projects() {
      await axios
          .get(`api/v1/projects/?personal=${this.apiEndpoint}`)
          .then(response => {
            this.projects = response.data
            // console.log(this.projects)
          })
          .catch(error => {
            console.log('Ошибка при загрузке проектов')
            console.log('retrying..')
            setTimeout(() => {
              this.get_projects()
            }, 1000)
          })
    },
  },

  created() {
    this.get_projects()

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage') {
        this.switchLanguage(state.language.language)
      }
    })
  },

  beforeMount() {
    this.switchLanguage(this.$store.state.language.language)
  },


}
</script>

<style>
.el-carousel__container {
  height: 100vh !important;
}

.project-container {
  position: absolute;
  top: 0;
  width: 100%;
}

.image-container {
  height: 100vh;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.image-container img {
  max-width: inherit;
  min-width: 100vw;
  height: 100vh;
}

.gradient {
  height: 91vh;
  margin-top: 9vh;
  width: 100%;
  position: absolute;
  --tw-gradient-from: #0f1922;
  --tw-gradient-to: rgb(15 25 34 / 0);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
  background-image: linear-gradient(to top, var(--tw-gradient-stops));
  top: 0;
  z-index: 100;
}

.gradient:hover ~ .image {
  transform: scale(1.05);
}

.blackout {
  height: 100vh;
  width: 100%;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 99;
}

.image {
  transition: transform 0.4s ease-out;
}

.no-image {
  max-width: 100% !important;
  height: auto !important;
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
  text-align: center;
}

.hover-area {
  background-color: transparent;
  width: 100%;
  height: 200%;
  bottom: -25%;
  position: absolute;
  z-index: 105;
}

.text-container {
  position: relative;
  max-width: 80rem;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  top: 65%;
  color: white;
}

.text-container:hover .title {
  transform: translateY(-200%);
}

.text-container:hover .description {
  opacity: 1;
}

.text-container:hover .additional {
  transform: translateY(75%);
}

.title {
  font-family: Montserrat, 'sans-serif';
  font-size: 2rem;
  line-height: 1.1;
  font-style: normal;
  font-weight: 700;
  margin: 0 2rem;
}

.project-link {
  color: white;
  position: relative;
  text-decoration: none;
  z-index: 105;
}

.navbar_social-link {
  color: #dadada;
  transition: color 0.2s ease-out;
}

.navbar_social-link:hover {
  color: white;
}

.title, .additional {
  transition: all 0.3s ease-in-out;
}

.description {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  margin: 0 2rem;
  opacity: 0;
  transition: all 0.3s ease-in-out;
  transform: translateY(-50%);
  max-width: 60%;
  /*margin-bottom: -50px;
  */
}

.additional {
  border-bottom: white solid 1px;
  margin: 0 2rem;
  display: flex;
  justify-content: space-between;
  position: inherit;
  z-index: 110;
}

.project-icons {
  padding-left: 20px;
}

.groups {
  padding-bottom: 0.8rem;
}

@media screen and (max-width: 992px) {
  .el-carousel__arrow--left {
    left: 32px !important;
  }

  .el-carousel__arrow--right {
    right: 32px !important;
  }

  .el-carousel__arrow {
    top: 81% !important;
  }

  .text-container:hover .title {
    transform: none;
  }

  .text-container:hover .additional {
    transform: none;
  }

  .text-container {
    top: 35%;
    height: 40vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  .title {
    transform: none;
    padding-bottom: 2rem
  }

  .description {
    opacity: 1;
    max-width: 100%;
    transform: none;
    padding-bottom: 2rem
  }

  .additional {
    transform: none;
    margin-left: 2rem;
  }

  .hover-area {
    visibility: hidden;
  }
}

@media screen and (max-width: 768px) {
}

@media only screen and (min-width: 480px) {
}
</style>