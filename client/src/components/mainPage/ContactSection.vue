<template>
  <section class="section_contact01">
    <div class="page-padding">
      <div class="container-small">
        <div id="contact-section" class="padding-vertical-xhuge">
          <div class="text-align-center">
            <div class="max-width-large align-center">
              <div class="heading-subheading">Contact me</div>
              <h2 class="heading-medium">Get in touch</h2>
              <div class="space-xsmall"></div>
              <div class="text-size-large">I’d love to hear from you. Please fill out this form.</div>
            </div>
          </div>
          <div class="contact01_component w-form">
            <form @submit.prevent="onSubmit" id="wf-form-Contact-01-form" name="wf-form-Contact-01-form" data-name="Contact 01 form" method="get" class="contact01_form">
              <div class="form-field-wrapper">
                <label for="Contact-01-name" class="field-label">Name</label>
                <input type="text" v-model="name" class="form_input w-input" maxlength="256" name="Contact-01-name" data-name="Contact 01 name" placeholder="Your name" id="Contact-01-name" required="" />
              </div>
              <div class="form-field-wrapper">
                <label for="Contact-01-email" class="field-label">Email</label>
                <input type="email" v-model="email" class="form_input w-input" maxlength="256" name="Contact-01-email" data-name="Contact 01 email" placeholder="you@company.com" id="Contact-01-email" required="" />
              </div>
              <div class="form-field-wrapper">
                <label for="Contact-01-message" class="field-label">Message</label>
                <textarea v-model="message" id="Contact-01-message" name="Contact-01-message" maxlength="5000" data-name="Contact 01 message" placeholder="Tell me what do you want?" required="" class="form_input text-area w-input"></textarea>
              </div>
              <label id="Contact-1-Checkbox" class="w-checkbox form-checkbox">
                <div class="w-checkbox-input w-checkbox-input--inputType-custom form-checkbox-icon"></div>
                <input type="checkbox" v-model="policy" id="Contact-01-checkbox" name="Contact-01-checkbox" data-name="Contact 01 checkbox" required="" style="opacity:0;position:absolute;z-index:-1" />
                <span for="Contact-01-checkbox" class="form-checkbox-label w-form-label">You agree to our friendly <a href="#" class="text-style-link">privacy policy</a>. </span>
              </label>
              <div id="w-node-da303c11-a294-4460-67a2-4c54ae40d5db-9f429e46" class="form-button-wrapper">
                <input type="submit" @click="checkForm" value="Send message" data-wait="Please wait..." id="w-node-da303c11-a294-4460-67a2-4c54ae40d5dc-9f429e46" class="button-2 w-button" />
              </div>
            </form>
            <div class="success-message w-form-done">
              <div class="success-text">Thank you! Your submission has been received!</div>
            </div>
            <div class="error-message w-form-fail">
              <div class="error-text">Oops! Something went wrong while submitting the form.</div>
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
  data(){
    return {
      name: '',
      email: '',
      message: '',
      policy: false
    }
  },
  methods: {
    checkForm(){
      var regex = /^[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/

      if(this.name!=='' && regex.test(this.email) && this.policy){
        console.log('Sending request..')
        this.sendRequest()
      } else {
        console.log('Form error!')
      }
    },

    async sendRequest(){
      let body = {
        name: this.name,
        email: this.email,
        message: this.message
      }

      await axios
      .post('api/v1/send_request', body)
      .then(response => {
      console.log('Success')
      })
      .catch(error => {
        console.log('Error during post request')
      })
    }
  }
}
</script>

<style scoped>

</style>