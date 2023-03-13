<template>
  <section class="section_contact01">
    <div class="page-padding">
      <div class="container-small">
        <div id="contact-section" class="padding-vertical-xhuge">
          <div class="text-align-center">
            <div class="max-width-large align-center">
              <div class="heading-subheading">{{ text.contact_pretitle }}</div>
              <h1 class="heading-medium">{{ text.contact_title }}</h1>
              <div class="space-xsmall"></div>
              <div class="text-size-large">{{ text.contact_description }}</div>
            </div>
          </div>
          <div class="contact01_component w-form">
            <form @submit.prevent="onSubmit" ref="sendForm" class="contact01_form">
              <div class="form-field-wrapper">
                <label for="Contact-01-name" class="field-label">{{ text.name_label }}</label>
                <input type="text" v-model="name" class="form_input w-input" maxlength="256" name="Contact-01-name" data-name="Contact 01 name" :placeholder="text.name_placeholder" id="Contact-01-name" required="" />
              </div>
              <div class="form-field-wrapper">
                <label for="Contact-01-email" class="field-label">{{ text.email_label }}</label>
                <input type="email" v-model="email" class="form_input w-input" maxlength="256" name="Contact-01-email" data-name="Contact 01 email" :placeholder="text.email_placeholder " id="Contact-01-email" required="" />
              </div>
              <div class="form-field-wrapper">
                <label for="Contact-01-message" class="field-label">{{ text.message_label }}</label>
                <textarea v-model="message" id="Contact-01-message" name="Contact-01-message" maxlength="5000" data-name="Contact 01 message" :placeholder="text.message_placeholder" required="" class="form_input text-area w-input"></textarea>
              </div>
              <label id="Contact-1-Checkbox" class="w-checkbox form-checkbox">
                <div ref="checkbox" class="w-checkbox-input w-checkbox-input--inputType-custom form-checkbox-icon"></div>
                <input type="checkbox" @change="checkChange" v-model="policy" id="Contact-01-checkbox" name="Contact-01-checkbox" data-name="Contact 01 checkbox" required="" style="opacity:0;position:absolute;z-index:-1" />
                <span for="Contact-01-checkbox" class="form-checkbox-label w-form-label">{{ text.privacy_text }} <router-link to="/privacy" class="text-style-link">{{ text.privacy_link }}</router-link>.</span>
              </label>
              <div class="form-button-wrapper">
                <input type="submit" @click="checkForm" :value="text.send_message_button" class="button-2 w-button" />
              </div>
            </form>
            <div class="success-message w-form-done" ref="done">
              <div class="success-text">{{ text.success_message }}</div>
            </div>
            <div class="error-message w-form-fail" ref="fail">
              <div class="error-text" style="text-align: center">{{ text.error_message }}</div>
              <input @click="retryForm" type="button" value="Retry" class="button-secondary-gray" style="position: relative;margin: 0 auto;margin-top: 2rem;">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "ContactSection",
  props: [
      'text'
  ],
  data(){
    return {
      name: '',
      email: '',
      message: '',
      policy: false,
      // sendValue: 'Send message',
    }
  },

  methods: {
    checkForm(){
      var regex = /^[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/

      if(this.name!=='' && regex.test(this.email) && this.policy){
        console.log('Sending request..')
        this.sendValue = 'Please wait..'
        this.sendRequest()
      } else {
        console.log('Form error!')
      }
    },

    async sendRequest(){
      let body = {
        request: {
          name: this.name,
          mail: this.email,
          message: this.message
        }
      }

      await axios
      .post('api/v1/send_request', body)
      .then(response => {
      console.log(response.data.Success)
        this.$refs.done.style.display = 'block'
        this.$refs.sendForm.style.display = 'none'
      })
      .catch(error => {
        console.log('Error during post request')
        this.$refs.fail.style.display = 'block'
        this.$refs.sendForm.style.display = 'none'
      })

      this.sendValue = 'Send message'
    },

    retryForm(){
      this.$refs.fail.style.display = 'none'
      this.$refs.sendForm.style.display = 'grid'
    },

    checkChange(){
      if (this.policy){
        this.$refs.checkbox.classList.value = 'w-checkbox-input w-checkbox-input--inputType-custom form-checkbox-icon w--redirected-checked'
            // 'url(src/assets/icons/check.svg)'
      } else {
        this.$refs.checkbox.classList.value = 'w-checkbox-input w-checkbox-input--inputType-custom form-checkbox-icon'
      }
    }
  }
}
</script>

<style scoped>
@media screen and (max-width: 767px){
  .padding-vertical-xhuge {
      padding-top: 2rem;
  }
  .contact01_component {
    margin-top: 2rem;
}

  .form_input.text-area {
    min-height: 6.25rem;
}
}
</style>