<template>
  <section class="feedback" @scroll="handleScroll" >
    <div @scroll="handleScroll"></div>
    <div class="page-padding" v-if="showModule">
      <div class="container-small">
        <div id="rate-section" class="padding-vertical-xhuge">
          <div class="text-align-center">
            <div class="rate-block">
              <div class="heading-subheading">{{ !rateState ? rateModule.rate_title : rateModule.rate_title_success }}</div>
              <el-rate v-model="rateValue" :colors="colors" size="large" :disabled="rateState" @change="rateSubmit" />
            </div>
          </div>
          <div class="max-width-large align-center">
            <div class="text-align-center">
              <h1 class="heading-medium">{{ rateModule.feedback_title }}</h1>
              <div class="space-xsmall"></div>
              <div class="text-size-large">{{ rateModule.feedback_description }}</div>
            </div>
          </div>
          <div class="contact01_component w-form">
            <form @submit.prevent="onSubmit" ref="sendRateForm" class="contact01_form">
              <div class="form-field-wrapper">
                <label class="field-label">{{ rateModule.feedback_message_label }}</label>
                <textarea v-model="rateMessage" name="Contact-01-message" maxlength="5000" :placeholder="rateModule.feedback_message_placeholder" required="" class="form_input text-area w-input"></textarea>
              </div>
              <div class="form-button-wrapper">
                <input type="submit" @click="checkRateForm" :value="!this.sending_feedback ? rateModule.send_button : rateModule.send_button_wait" class="button-2 w-button" />
              </div>
            </form>
            <div class="success-message w-form-done" ref="rateDone">
              <div class="success-text">{{ rateModule.feedback_success_message }}</div>
            </div>
            <div class="error-message w-form-fail" ref="rateFail">
              <div class="error-text" style="text-align: center">{{ rateModule.feedback_error_message }}</div>
              <input @click="retryForm" type="button" :value="rateModule.retry_button" class="button-secondary-gray" style="position: relative;margin: 0 auto;margin-top: 2rem;">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import debounce from "lodash/debounce";
import store from "../store";

export default {
  name: "Rate.vue",
  props: [
    'source'
  ],
  data(){
    return {
      showModule: false,
      rateModule: {},

      rateState: false,
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],

      rateValue: 0,
      rateMessage: '',

      sending_feedback: false,
    }
  },
  methods: {
    async getText(lang){
      await axios
          .get(`http://localhost:8000/api/v1/pages/rate/?language=${lang}`)
          .then(response => {
            this.rateModule = response.data[0]
          })
          .catch(error => {
            console.log('Ошибка при загрузке локализации')
          })
    },

    rateSubmit(){
      this.rateState = true
      console.log('Sending request..')
      this.sendRate()
    },

    async sendRate(){
      let rateBody = {
        request: {
          source: this.source,
          rate_value: parseInt(this.rateValue),
          project_version: this.$projectVersion,
          user_agent: navigator.userAgent,
          screen_resolution: `${window.screen.width}x${window.screen.height}`,
          browser_language: navigator.language,
          timezone: new Date().getTimezoneOffset(),
        }
      }

      await axios
          .post('api/v1/send_rate', rateBody)
          .then(response => {
            console.log(response.data.success)
          })
          .catch(() => {
            console.log('Error during post request')
          })
    },

    checkRateForm(){
      if(this.rateMessage){
        console.log('Sending request..')
        this.sending_feedback = true
        this.sendFeedback()
      } else {
        console.log('Form error!')
      }
    },

    async sendFeedback(){
      let feedbackBody = {
        request: {
          source: this.source,
          rate_message: this.rateMessage,
          project_version: this.$projectVersion,
          user_agent: navigator.userAgent,
          screen_resolution: `${window.screen.width}x${window.screen.height}`,
          browser_language: navigator.language,
          timezone: new Date().getTimezoneOffset(),
        }
      }

      await axios
          .post('api/v1/send_feedback', feedbackBody)
          .then(response => {
            console.log(response.data.success)
            this.$refs.rateDone.style.display = 'block'
            this.$refs.sendRateForm.style.display = 'none'
          })
          .catch(() => {
            console.log('Error during post request')
            this.$refs.rateFail.style.display = 'block'
            this.$refs.sendRateForm.style.display = 'none'
          })

      this.sending_feedback = false
    },

    retryForm(){
      this.$refs.rateFail.style.display = 'none'
      this.$refs.sendRateForm.style.display = 'grid'
    },


    handleScroll(){
      const scrollPosition = window.pageYOffset + window.innerHeight
      const documentHeight = document.documentElement.scrollHeight
      if (scrollPosition === documentHeight) {
        setTimeout(() => {
          if(window.pageYOffset + window.innerHeight === documentHeight){
            this.showModule = true
          }
        },500)
      }
    },
  },
  created() {
    this.getText(this.$store.state.language.language)

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage'){
        this.getText(state.language.language)
      }
    })
  },
  mounted() {
    this.handleDebouncedScroll = debounce(this.handleScroll, 500);
    window.addEventListener('scroll', this.handleDebouncedScroll, false);
  },
  unmounted() {
    window.removeEventListener('scroll', this.handleDebouncedScroll, false);
  }
}
</script>

<style scoped>

.rate-block {
  padding: 30px 0;
  text-align: center;
  display: inline-block;
  box-sizing: border-box;
}

#rate-section {
  padding-bottom: 10rem;
}

.el-icon svg {
    height: 1.2em;
    width: 1.2em;
}

.contact01_component {
    max-width: 30rem;
    margin: 3rem auto 0px;
}

.max-width-large.align-center {
  padding-top: 3rem;
}

</style>