<template>
  <!--  <InDevelop :frontendURL="frontendURL"/>-->
  <div class="main-block">
    <h1 class="heading-xlarge">{{ text.title }}</h1>
    <div class="skills-container" ref="skillContainer">


      <div ref="backend" @click="expandCard($refs.backend)" class="card-container"
           :class="hidden ? 'hidden' : 'visible'">
        <el-card shadow="hover">
          <h2 class="heading-xxsmall">
            {{ text.backend_title }}
          </h2>

          <div class="primary-text" :class="primary ? 'full-opacity' : 'zero-opacity'">
            <div v-html="text.backend_description" class="text-size-medium"></div>
          </div>

          <div class="secondary-text" :class="!primary ? 'full-opacity' : 'zero-opacity'">
            <el-button class="button"
                       text
                       @click="collapseCard($refs.backend)"
            >
              <!--            :class="!primary ? 'full-opacity' : 'zero-opacity'"-->
              <img :src="`${frontendURL}/src/assets/icons/arrow-left.svg`" loading="lazy" width="30"
                   alt="collapse card"/>
            </el-button>

            <el-collapse v-model="backendActiveName" accordion>
              <el-collapse-item v-for="(skill, key) in backend_skills"
                                :title="lang_ru ? skill.name_ru : skill.name"
                                :name="key.toString()"
                                :number="key.toString()"
                                @mouseenter="backendActiveNameChange"
                                @mouseleave="clearTimer">

                <div v-if="lang_ru" class="collapse-content text-size-medium">
                  {{ skill.description_ru }}
                </div>
                <div v-else class="collapse-content text-size-medium">
                  {{ skill.description }}
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>

        </el-card>
      </div>


      <div ref="frontend" @click="expandCard($refs.frontend)" class="card-container"
           :class="hidden ? 'hidden' : 'visible'">
        <el-card shadow="hover">
          <h1 class="heading-xxsmall">
            {{ text.frontend_title }}
          </h1>

          <div class="primary-text" :class="primary ? 'full-opacity' : 'zero-opacity'">
            <div v-html="text.frontend_description" class="text-size-medium"></div>
          </div>

          <div class="secondary-text" :class="!primary ? 'full-opacity' : 'zero-opacity'">
            <el-button class="button"
                       text
                       @click="collapseCard($refs.frontend)">
              <img :src="`${frontendURL}/src/assets/icons/arrow-left.svg`" loading="lazy" width="30"
                   alt="collapse card"/>
            </el-button>

            <el-collapse v-model="frontendActiveName" accordion>
              <el-collapse-item v-for="(skill, key) in frontend_skills"
                                :title="lang_ru ? skill.name_ru : skill.name"
                                :name="key.toString()"
                                :number="key.toString()"
                                @mouseenter="frontendActiveNameChange"
                                @mouseleave="clearTimer"
              >
                <div v-if="lang_ru" class="collapse-content text-size-medium">
                  {{ skill.description_ru }}
                </div>
                <div v-else class="collapse-content text-size-medium">
                  {{ skill.description }}
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>

        </el-card>
      </div>


      <div ref="other" @click="expandCard($refs.other)" class="card-container" :class="hidden ? 'hidden' : 'visible'">
        <el-card shadow="hover">
          <h1 class="heading-xxsmall">
            {{ text.other_title }}
          </h1>

          <div class="primary-text" :class="primary ? 'full-opacity' : 'zero-opacity'">
            <div v-html="text.other_description" class="text-size-medium"></div>
          </div>

          <div class="secondary-text" :class="!primary ? 'full-opacity' : 'zero-opacity'">
            <el-button class="button"
                       text
                       @click="collapseCard($refs.other)">
              <img :src="`${frontendURL}/src/assets/icons/arrow-left.svg`" loading="lazy" width="30"
                   alt="collapse card"/>
            </el-button>

            <el-collapse v-model="otherActiveName" accordion>
              <el-collapse-item v-for="(skill, key) in other_skills"
                                :title="lang_ru ? skill.name_ru : skill.name"
                                :name="key.toString()"
                                :number="key.toString()"
                                @mouseenter="otherActiveNameChange"
                                @mouseleave="clearTimer"
              >
                <div v-if="lang_ru" class="collapse-content text-size-medium">
                  {{ skill.description_ru }}
                </div>
                <div v-else class="collapse-content text-size-medium">
                  {{ skill.description }}
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>

        </el-card>
      </div>

    </div>

  </div>
</template>

<script>
import InDevelop from "../InDevelop.vue";
import axios from "axios";
import store from "../../store";

export default {
  name: "MainSection",
  inject: [
    'backendURL',
    'frontendURL'
  ],
  components: {
    InDevelop
  },
  props: [
    'text'
  ],
  data() {
    return {
      lang_ru: false,

      hidden: false,
      primary: true,
      frontendActiveName: '0',
      backendActiveName: '0',
      otherActiveName: '0',

      timer: null,
      expanded: false,

      backend_skills: [],
      frontend_skills: [],
      other_skills: [],
    }
  },
  methods: {
    switchLanguage(lang) {
      this.lang_ru = lang === 'ru';
    },

    expandCard(ref) {
      if (!this.hidden) {
        ref.style.height = '100%'
        ref.style.opacity = '1'
        ref.style.cursor = 'inherit'
        this.hidden = true
        this.primary = false
        this.$refs.skillContainer.style.gap = '0'
        window.scrollTo({top: 0, behavior: 'smooth'});
      }
    },

    collapseCard(ref) {
      setTimeout(() => {
        if (this.hidden) {
          ref.style.height = ''
          ref.style.opacity = ''
          ref.style.cursor = 'pointer'
          // this.$refs.collapseButton.style.visibility = 'hidden'
          this.hidden = false
          this.primary = true
          this.$refs.skillContainer.style.gap = '1.5rem'
        }
      }, 0)

    },

    clearTimer() {
      clearTimeout(this.timer);
      this.expanded = false
    },

    backendActiveNameChange: function (event) {
      if (this.hidden) {
        this.timer = setTimeout(() => {
          if (!this.expanded) {
            this.backendActiveName = event.target.getAttribute("number")
            this.expanded = true
          }
        }, 250);
      }
    },

    frontendActiveNameChange: function (event) {
      if (this.hidden) {
        this.timer = setTimeout(() => {
          if (!this.expanded) {
            this.frontendActiveName = event.target.getAttribute("number")
            this.expanded = true
          }
        }, 250);
      }
    },

    otherActiveNameChange: function (event) {
      if (this.hidden) {
        this.timer = setTimeout(() => {
          if (!this.expanded) {
            this.otherActiveName = event.target.getAttribute("number")
            this.expanded = true
          }
        }, 250);
      }
    },

    async get_skills() {
      await axios
          .get(`api/v1/skills/`)
          .then(response => {
            response.data.forEach(item => {
              if (item.skill_type === 'backend') {
                this.backend_skills.push(item)
              } else if (item.skill_type === 'frontend') {
                this.frontend_skills.push(item)
              } else {
                this.other_skills.push(item)
              }
            })
          })
          .catch(error => {
            console.log('Ошибка при загрузке навыков')
            console.log(error)
            console.log('retrying..')
            setTimeout(() => {
              this.get_skills()
            }, 1000)
          })
    }
  },

  created() {
    this.get_skills()

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage') {
        this.switchLanguage(state.language.language)
      }
    })

    if (document.documentElement.clientWidth <= 767) {
      this.backendActiveName = '-1'
      this.frontendActiveName = '-1'
      this.otherActiveName = '-1'
    }
  },

  beforeMount() {
    this.switchLanguage(this.$store.state.language.language)
  },

}
</script>

<style>
.el-collapse-item__header {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  color: #475467 !important;
  font-size: 16px !important;
  font-weight: 600 !important;
}
</style>

<style scoped>
.main-block {
  padding-top: 9vh;
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
}

.skills-container {
  padding: 2rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.heading-xlarge {
  margin-top: 2rem;
  font-size: 2.5rem;
}

.button {
  position: absolute;
  transform: translateY(-44px);
  transition: opacity 0s ease-in-out;
}

.heading-xxsmall {
  text-align: center;
  padding-bottom: 10px;
  font-size: 1.5rem;
}

.text-size-medium {
  text-align: justify;
}

.card-container {
  cursor: pointer;
}

.visible {
  /*height: 30%;*/
  visibility: visible;
}

.hidden {
  height: 0;
  /*visibility: hidden;*/
  opacity: 0;
}

.primary-text, .secondary-text {
  transition: opacity 0.2s ease-in-out;
}

.full-opacity {
  opacity: 1;
}

.zero-opacity {
  opacity: 0;
  height: 0;
  visibility: collapse;
}

.el-card.is-hover-shadow {
  height: 100%;
}

.collapse-content {
  text-align: justify;
}

@media screen and (max-width: 992px) {

  .text-size-medium {
    font-size: 1rem;
  }
}

</style>